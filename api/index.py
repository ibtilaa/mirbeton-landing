"""
MirBeton ERP — yagona kirish nuqtasi.
Vercel barcha /api/* so'rovlarni shu faylga yo'naltiradi.
"""
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from aiogram.types import Update

from api.config import bot, dp
from api.bot_handlers import *  # noqa: F401,F403 — bot handler'lar ro'yxatdan o'tadi
from api.routes import landing, sales, admin, prod, driver

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Router'lar (prefix /api)
app.include_router(landing.router, prefix="/api", tags=["landing"])
app.include_router(sales.router, prefix="/api", tags=["sales"])
app.include_router(admin.router, prefix="/api", tags=["admin"])
app.include_router(prod.router, prefix="/api", tags=["prod"])
app.include_router(driver.router, prefix="/api", tags=["driver"])


@app.post("/api/webhook")
async def webhook(request: Request):
    """Telegram webhook: barcha update'lar shu yerga tushadi."""
    try:
        body = await request.json()
        await dp.feed_update(bot=bot, update=Update(**body))
        return {"ok": True}
    except Exception as e:
        logger.warning("webhook: %s", str(e))
        return {"ok": False, "error": "Xato yuz berdi."}
