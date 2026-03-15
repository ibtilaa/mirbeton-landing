"""Loyiha sozlamalari va umumiy dependency'lar (Supabase, Bot)."""
import os
import logging
from supabase import create_client, Client
from aiogram import Bot, Dispatcher

logger = logging.getLogger(__name__)

# Env
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SITE_URL = os.getenv("SITE_URL", "")
CSV_URL = os.getenv("GOOGLE_SHEETS_CSV_URL", "")
ORDER_SCRIPT_URL = os.getenv(
    "GOOGLE_ORDER_SCRIPT_URL",
    "https://script.google.com/macros/s/AKfycbzJsFs5smnHLMDSqkud4CCC9aVu2_eEvw_LBUJbbIFRU9-TM1Ci6BB3FYMwdMdj2K05rw/exec",
)
ORDER_SECRET = os.getenv("GOOGLE_ORDER_SECRET", "MirBeton_Safe_2026")

# Supabase (xatosiz ishlashi uchun URL/KEY bo‘lishi shart)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) if (SUPABASE_URL and SUPABASE_KEY) else None

# Bot
bot = Bot(token=BOT_TOKEN) if BOT_TOKEN else None
dp = Dispatcher()
