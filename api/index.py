import os
import json
import logging
import httpx
from fastapi import FastAPI, Request, HTTPException
from supabase import create_client, Client
from aiogram import Bot, Dispatcher, types
from aiogram.types import Update
from datetime import datetime

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Muhit o'zgaruvchilari
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initsializatsiya
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

app = FastAPI()

# --- 1. TELEGRAM WEBHOOK ---
@app.post("/api/webhook")
async def telegram_webhook(request: Request):
    try:
        body = await request.json()
        update = Update(**body)
        await dp.feed_update(bot=bot, update=update)
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Webhook error: {str(e)}")
        return {"status": "error"}

# --- 2. LANDING PAGE ORDER (order.js o'rniga) ---
@app.post("/api/order")
async def create_order(request: Request):
    try:
        data = await request.json()
        # Landingdan kelgan ma'lumotni Supabasega saqlash
        order_id = f"MB-{datetime.now().strftime('%y%m%d-%H%M')}"
        
        # Mijozni tekshirish yoki yaratish
        # (Sodda mantiq: telefon bo'yicha)
        
        new_order = {
            "id": order_id,
            "grade": data.get("grade"),
            "volume": float(data.get("volume", 0)),
            "address": data.get("address"),
            "status": "pending"
        }
        
        supabase.table("orders").insert(new_order).execute()
        
        # Operatorga xabar yuborish
        await bot.send_message(os.getenv("NOTIFY_ID"), f"🏗 Yangi Buyurtma: {order_id}\nMarka: {data['grade']}\nHajm: {data['volume']} m3")
        
        return {"success": True, "orderId": order_id}
    except Exception as e:
        logger.error(f"Order error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# --- 3. PRICE FETCH (prices.js o'rniga) ---
@app.get("/api/prices")
async def get_prices():
    # Bu funksiya Google Sheets CSV yoki Supabase'dan narxlarni oladi
    # Hozircha CSV dan redirect qilishni qoldiramiz
    CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKAi5cvDHmLR7_yKQhatpE0g2kfwuU6z9V_V_IISI1HPpwm3D1GJKGxAngF/pub?gid=61862596&single=true&output=csv"
    async with httpx.AsyncClient() as client:
        resp = await client.get(CSV_URL)
        return resp.text

# --- 4. MINI APP: DRIVER EVENTS ---
@app.post("/api/driver-event")
async def driver_event(request: Request):
    try:
        data = await request.json()
        order_id = data.get("order_id")
        step = data.get("step")
        
        # Log yozish
        supabase.table("order_logs").insert({"order_id": order_id, "event_type": step}).execute()
        
        # Statusni yangilash
        status_map = {"en_route": "en_route", "arrived": "arrived", "pouring_start": "pouring", "pouring_end": "completed"}
        if step in status_map:
            supabase.table("orders").update({"status": status_map[step]}).eq("id", order_id).execute()
            
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Bot komandasi
@dp.message()
async def start_handler(message: types.Message):
    if message.text == "/start":
        await message.answer("MirBeton Tizimiga xush kelibsiz! 🏗")
