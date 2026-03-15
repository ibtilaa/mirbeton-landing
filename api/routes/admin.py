"""Admin API: foydalanuvchilar ro'yxati, tahrirlash. Faqat admin."""
import logging
from fastapi import APIRouter, Body, Query
from api.config import supabase

router = APIRouter()
logger = logging.getLogger(__name__)


def _is_admin(user_id: str) -> bool:
    if not supabase:
        return False
    try:
        r = supabase.table("users").select("role").eq("id", user_id).single().execute()
        return bool(r.data and r.data.get("role") == "admin")
    except Exception:
        return False


@router.get("/admin/users")
async def admin_get_users(user_id: str = Query(..., alias="user_id")):
    """Barcha foydalanuvchilar (faqat admin)."""
    if not _is_admin(user_id):
        return {"error": "Ruxsat berilmagan"}
    try:
        r = supabase.table("users").select("*").order("created_at").execute()
        return r.data or []
    except Exception as e:
        logger.warning("admin_get_users: %s", str(e))
        return {"error": "Ro'yxat yuklanmadi."}


@router.post("/admin/update-user")
async def admin_update_user(data: dict = Body(...)):
    """Foydalanuvchi ma'lumotlarini tahrirlash (role, phone, is_active)."""
    admin_id = data.get("admin_id")
    target_id = data.get("target_id")
    if not admin_id or not target_id:
        return {"error": "admin_id va target_id kerak"}
    if not _is_admin(admin_id):
        return {"error": "Ruxsat yo'q"}
    try:
        payload = {
            "role": data.get("role"),
            "full_name": data.get("full_name"),
            "phone": data.get("phone"),
            "secondary_phone": data.get("secondary_phone"),
            "is_active": data.get("is_active", True),
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        supabase.table("users").update(payload).eq("id", target_id).execute()
        return {"success": True}
    except Exception as e:
        logger.warning("admin_update_user: %s", str(e))
        return {"error": "O'zgartirish saqlanmadi."}
