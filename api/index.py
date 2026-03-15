import os
import csv
import logging
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from supabase import create_client, Client
from datetime import datetime
from dateutil import parser

# LOGGING
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ENV
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SITE_URL = os.getenv("SITE_URL")
CSV_URL = os.getenv("GOOGLE_SHEETS_CSV_URL")

# INIT
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# --- BOT HANDLERS ---
@dp.message(F.text == "/start")
async def cmd_start(message: types.Message):
    tg_id = message.from_user.id
    res = supabase.table("users").select("*").eq("tg_id", tg_id).execute()
    user = res.data[0] if res.data else None

    if not user:
        kb = [[KeyboardButton(text="📱 Kontaktni ulash", request_contact=True)]]
        markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
        await message.answer("<b>Xush kelibsiz!</b>\nMirBeton tizimida ishlash uchun telefon raqamingizni yuboring:", reply_markup=markup, parse_mode="HTML")
    elif not user.get("secondary_phone"):
        await message.answer("Rahmat! Endi hayotda bog'lanish uchun doimiy raqamingizni yozib yuboring (Masalan: 998901234567):")
    else:
        role = user['role']
        app_url = f"{SITE_URL}/app.html?role={role}&user_id={user['id']}"
        kb = [[KeyboardButton(text="🚀 Tizimni ochish", web_app=WebAppInfo(url=app_url))]]
        kb.append([KeyboardButton(text="📊 Narxlar", web_app=WebAppInfo(url=f"{SITE_URL}/app.html?role=prices"))])
        await message.answer(f"Siz tizimga <b>{role.upper()}</b> sifatida kirdingiz.", reply_markup=ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True), parse_mode="HTML")

@dp.message(F.contact)
async def handle_contact(message: types.Message):
    supabase.table("users").upsert({
        "tg_id": message.from_user.id, 
        "full_name": message.from_user.full_name,
        "phone": message.contact.phone_number,
        "role": "client"
    }).execute()
    await message.answer("Telegram raqam saqlandi. Endi qo'shimcha raqamingizni yozing:", reply_markup=ReplyKeyboardRemove())

@dp.message(F.text.regexp(r'^\d+$'))
async def handle_phone2(message: types.Message):
    supabase.table("users").update({"secondary_phone": message.text}).eq("tg_id", message.from_user.id).execute()
    await message.answer("✅ Ro'yxatdan o'tish tugadi. /start bosing.")

# --- API ROUTES ---
@app.post("/api/webhook")
async def webhook(request: Request):
    body = await request.json()
    await dp.feed_update(bot=bot, update=Update(**body))
    return {"ok": True}

@app.get("/api/prices")
async def get_prices():
    async with httpx.AsyncClient() as client:
        r = await client.get(CSV_URL)
        lines = r.text.splitlines()
        return list(csv.DictReader(lines))

@app.post("/api/driver-event")
async def driver_event(request: Request):
    data = await request.json()
    order_id, step = data.get("order_id"), data.get("step")
    lat, lng = data.get("lat"), data.get("lng")

    # 1. Log update
    supabase.table("order_logs").insert({"order_id": order_id, "event_type": step, "location_lat": lat, "location_lng": lng}).execute()

    # 2. Status update
    st_map = {"en_route": "en_route", "arrived": "arrived", "pouring": "pouring", "done": "completed"}
    if step in st_map:
        supabase.table("orders").update({"status": st_map[step]}).eq("id", order_id).execute()

    # 3. Notify Client
    order_res = supabase.table("orders").select("*, client_id(tg_id)").eq("id", order_id).single().execute()
    client_tg = order_res.data['client_id']['tg_id']
    
    msgs = {"en_route": "🚚 Mikser yo'lga chiqdi!", "arrived": "📍 Mikser yetib keldi.", "done": "🏁 Buyurtma yakunlandi!"}
    if step in msgs:
        await bot.send_message(client_tg, msgs[step])
        if step == "done": await send_invoice(order_id, client_tg, order_res.data)

    return {"ok": True}

async def send_invoice(order_id, tg_id, order):
    inv = f"🧾 <b>INVOYS #{order_id}</b>\n\nMarka: {order['grade']}\nHajm: {order['volume']} m³\nJami: {order['total_amount']:,} so'm"
    await bot.send_message(tg_id, inv, parse_mode="HTML")

@app.get("/api/health")
def health(): return {"status": "ok"}