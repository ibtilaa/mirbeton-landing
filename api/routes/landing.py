"""Landing API: narxlar (CSV), buyurtma arizasi (lead). index.html o'zgartirilmasin."""
import logging
import httpx
from fastapi import APIRouter, Body
from fastapi.responses import PlainTextResponse

from api.config import CSV_URL, ORDER_SCRIPT_URL, ORDER_SECRET

router = APIRouter()
logger = logging.getLogger(__name__)

DEFAULT_CSV = "Marka,Narx,Min\nM300,650000,7"


@router.get("/prices", response_class=PlainTextResponse)
async def api_prices():
    """Narxlar jadvali (CSV). Landing index.html shu endpoint dan foydalanadi."""
    if not CSV_URL:
        return PlainTextResponse(DEFAULT_CSV, media_type="text/csv")
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(CSV_URL)
            r.raise_for_status()
            return PlainTextResponse(r.text, media_type="text/csv")
    except Exception as e:
        logger.warning("api_prices: %s", str(e))
        return PlainTextResponse(DEFAULT_CSV, media_type="text/csv")


@router.post("/order")
async def api_order(data: dict = Body(...)):
    """Buyurtma arizasi (lead). Landing index.html POST qiladi; Google Apps Script ga proxy."""
    if not ORDER_SCRIPT_URL:
        return {"success": False, "error": "Sozlamalar to'liq emas"}
    try:
        payload = {**data, "secret_token": ORDER_SECRET}
        async with httpx.AsyncClient(timeout=10.0) as client:
            r = await client.post(ORDER_SCRIPT_URL, json=payload)
            ct = r.headers.get("content-type", "")
            out = r.json() if "application/json" in ct else {"success": r.ok}
        return out
    except Exception as e:
        logger.warning("api_order: %s", str(e))
        return {
            "success": False,
            "error": "Tarmoq xatosi. Qayta urinib ko'ring yoki +998 90 000 44 55 ga qo'ng'iroq qiling.",
        }
