"""Haydovchi API: reys statuslari (en_route, arrived, completed)."""
import logging
from datetime import datetime
from fastapi import APIRouter, Body
from api.config import supabase, bot

router = APIRouter()
logger = logging.getLogger(__name__)

STATUS_MAP = {"en_route": "en_route", "arrived": "arrived", "completed": "completed"}
FIELD_MAP = {"en_route": "departed_at", "arrived": "arrived_at", "completed": "completed_at"}
MSGS = {
    "en_route": "🚚 Buyurtmangiz yo'lga chiqdi! Mikser manzilga qarab kelmoqda.",
    "arrived": "📍 Mikser manzilga yetib keldi!",
    "completed": "✅ Buyurtma muvaffaqiyatli yakunlandi. Rahmat!",
}


@router.post("/driver/event")
async def driver_event(data: dict = Body(...)):
    """Haydovchi statusi: en_route, arrived, completed. GPS ixtiyoriy."""
    if not supabase:
        return {"error": "Baza ulanishi yo'q"}
    trip_id = data.get("trip_id")
    event = data.get("event")
    if not trip_id or event not in STATUS_MAP:
        return {"error": "trip_id va event (en_route/arrived/completed) kerak"}
    try:
        update_field = FIELD_MAP[event]
        payload = {
            "status": STATUS_MAP[event],
            update_field: datetime.now().isoformat(),
            "last_lat": data.get("lat"),
            "last_lng": data.get("lng"),
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        supabase.table("order_trips").update(payload).eq("id", trip_id).execute()
        if bot and supabase:
            trip = supabase.table("order_trips").select("*, orders(*)").eq("id", trip_id).single().execute()
            if trip.data and trip.data.get("orders") and trip.data["orders"].get("client_id"):
                client_id = trip.data["orders"]["client_id"]
                client = supabase.table("users").select("tg_id").eq("id", client_id).single().execute()
                if client.data and client.data.get("tg_id"):
                    await bot.send_message(client.data["tg_id"], MSGS[event])
        return {"success": True}
    except Exception as e:
        logger.warning("driver_event: %s", str(e))
        return {"error": "Status yangilanmadi. Qayta urinib ko'ring."}
