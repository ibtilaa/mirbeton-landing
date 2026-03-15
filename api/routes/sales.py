"""Sales API: mijozlar ro'yxati, buyurtma kiritish/tahrirlash. Rol tekshiruvi kerak."""
import logging
from datetime import datetime
from fastapi import APIRouter, Body, Query
from api.config import supabase

router = APIRouter()
logger = logging.getLogger(__name__)


def _check_role(user_id: str, allowed_roles: list) -> tuple[bool, str]:
    """user_id bo'yicha rolni tekshir. (success, error_message)."""
    if not supabase:
        return False, "Baza ulanishi yo'q"
    try:
        r = supabase.table("users").select("role").eq("id", user_id).single().execute()
        if not r.data or r.data.get("role") not in allowed_roles:
            return False, "Ruxsat berilmagan"
        return True, ""
    except Exception as e:
        logger.warning("_check_role: %s", str(e))
        return False, "Foydalanuvchi tekshirilmadi"


@router.get("/sales/clients")
async def sales_clients(user_id: str = Query(..., alias="user_id")):
    """Mijozlar ro'yxati (sales yoki admin uchun)."""
    ok, err = _check_role(user_id, ["sales", "admin"])
    if not ok:
        return {"error": err}
    try:
        r = supabase.table("users").select("id, full_name, phone").eq("role", "client").order("full_name").execute()
        return r.data or []
    except Exception as e:
        logger.warning("sales_clients: %s", str(e))
        return {"error": "Ro'yxat yuklanmadi. Keyinroq urinib ko'ring."}


@router.post("/orders/upsert")
async def orders_upsert(data: dict = Body(...)):
    """Buyurtma kiritish yoki yangilash (sales)."""
    user_id = data.get("user_id") or data.get("sales_id")
    if not user_id:
        return {"error": "user_id kerak"}
    ok, err = _check_role(str(user_id), ["sales", "admin"])
    if not ok:
        return {"error": err}
    client_id = data.get("client_id")
    grade = data.get("grade")
    volume = data.get("volume")
    price_per_m3 = data.get("price_per_m3") or data.get("price")
    address = data.get("address")
    if not all([client_id, grade, volume, price_per_m3, address]):
        return {"error": "client_id, grade, volume, price_per_m3, address to'ldirilishi kerak"}
    try:
        payload = {
            "client_id": client_id,
            "grade": str(grade),
            "volume": float(volume),
            "price_per_m3": float(price_per_m3),
            "address": str(address),
            "status": "pending",
            "created_by": user_id,
            "updated_at": datetime.now().isoformat(),
        }
        if data.get("id"):
            supabase.table("orders").update(payload).eq("id", data["id"]).execute()
            return {"success": True, "updated": data["id"]}
        payload["created_at"] = datetime.now().isoformat()
        r = supabase.table("orders").insert(payload).execute()
        row = (r.data or [{}])[0]
        return {"success": True, "id": row.get("id")}
    except Exception as e:
        logger.warning("orders_upsert: %s", str(e))
        return {"error": "Buyurtma saqlanmadi. Ma'lumotlarni tekshiring."}
