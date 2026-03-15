"""Ishlab chiqarish operatori API: mikserga quyish."""
import logging
from datetime import datetime
from fastapi import APIRouter, Body
from api.config import supabase, bot

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/prod/pour")
async def prod_pour(data: dict = Body(...)):
    """Operator mikserga quyib bo'lgach: trip status + haydovchiga xabar."""
    if not supabase:
        return {"error": "Baza ulanishi yo'q"}
    trip_id = data.get("trip_id")
    driver_id = data.get("driver_id")
    if not trip_id or not driver_id:
        return {"error": "trip_id va driver_id kerak"}
    try:
        supabase.table("order_trips").update({
            "status": "poured",
            "poured_at": datetime.now().isoformat(),
            "driver_id": driver_id,
        }).eq("id", trip_id).execute()
        if bot:
            r = supabase.table("users").select("tg_id").eq("id", driver_id).single().execute()
            if r.data and r.data.get("tg_id"):
                await bot.send_message(
                    r.data["tg_id"],
                    "✅ <b>Beton tayyor!</b>\nMikseringiz to'ldirildi. Yo'lga chiqishingiz mumkin.",
                    parse_mode="HTML",
                )
        return {"success": True}
    except Exception as e:
        logger.warning("prod_pour: %s", str(e))
        return {"error": "Status yangilanmadi. Qayta urinib ko'ring."}
