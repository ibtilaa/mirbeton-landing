"""Telegram bot: /start, kontakt, /narxlar, WebApp havolasi."""
import csv
import logging
import httpx
from aiogram import types, F
from aiogram.filters import Command
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

from api.config import supabase, bot, dp, SITE_URL, CSV_URL

logger = logging.getLogger(__name__)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    tg_id = message.from_user.id
    try:
        res = supabase.table("users").select("*").eq("tg_id", tg_id).execute()
        user = res.data[0] if res.data else None
    except Exception as e:
        logger.warning("cmd_start users: %s", str(e))
        user = None

    if not user:
        kb = [[KeyboardButton(text="📱 Kontaktni ulash", request_contact=True)]]
        markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
        return await message.answer(
            "<b>MirBeton tizimiga xush kelibsiz!</b>\nRo'yxatdan o'tish uchun telefon raqamingizni yuboring:",
            reply_markup=markup,
            parse_mode="HTML",
        )

    if not user.get("secondary_phone"):
        kb = [
            [KeyboardButton(text="📱 Telegram raqam bilan bir xil")],
            [KeyboardButton(text="❌ Qo'shimcha raqam yo'q")],
        ]
        markup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
        return await message.answer(
            "Endi qo'shimcha bog'lanish raqamingizni yuboring yoki tanlang:",
            reply_markup=markup,
        )

    role = user["role"]
    app_url = f"{SITE_URL}/app.html?role={role}&user_id={user['id']}"
    kb = [[KeyboardButton(text="🏗 Tizimga kirish", web_app=WebAppInfo(url=app_url))]]
    if role in ["admin", "sales"]:
        kb.append([KeyboardButton(text="📊 Narxlar", web_app=WebAppInfo(url=f"{SITE_URL}/app.html?role=prices"))])
    await message.answer(
        f"Xush kelibsiz! Rolingiz: {role.upper()}",
        reply_markup=ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True),
    )


@dp.message(F.contact)
async def handle_contact(message: types.Message):
    phone = "+" + message.contact.phone_number.replace("+", "")
    try:
        supabase.table("users").upsert({
            "tg_id": message.from_user.id,
            "full_name": message.from_user.full_name,
            "phone": phone,
            "role": "client",
        }).execute()
    except Exception as e:
        logger.warning("handle_contact: %s", str(e))
    await cmd_start(message)


@dp.message(Command("narxlar"))
async def show_prices(message: types.Message):
    if not CSV_URL:
        return await message.answer("Narxlar hozircha mavjud emas.")
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(CSV_URL)
            data = list(csv.DictReader(r.text.splitlines()))
        text = "<b>Beton narxlari:</b>\n\n"
        for row in data:
            text += f"• {row.get('Marka', row.get('marka', '—'))}: {row.get('Narx', row.get('narx', '—'))} so'm\n"
        await message.answer(text, parse_mode="HTML")
    except Exception as e:
        logger.warning("show_prices: %s", str(e))
        await message.answer("Narxlar yuklanmadi. Keyinroq urinib ko'ring.")
