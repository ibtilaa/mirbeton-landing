# Cursor-06 bo'yicha note

**Sana:** 2026-03-16

## Nima qilindi

1. **Modulli tuzilish**
   - `api/config.py` — env o‘zgaruvchilar, Supabase, Bot, Dispatcher.
   - `api/routes/landing.py` — `GET /api/prices`, `POST /api/order` (landing uchun).
   - `api/routes/sales.py` — `GET /api/sales/clients`, `POST /api/orders/upsert` (rol tekshiruvi bilan).
   - `api/routes/admin.py` — `GET /api/admin/users`, `POST /api/admin/update-user`.
   - `api/routes/prod.py` — `POST /api/prod/pour`.
   - `api/routes/driver.py` — `POST /api/driver/event`.
   - `api/bot_handlers.py` — /start, kontakt, /narxlar, WebApp havolasi.
   - `api/index.py` — FastAPI app, router’lar ulash, webhook.

2. **Sales API**
   - `/api/sales/clients` — `user_id` query bilan; faqat sales/admin.
   - `/api/orders/upsert` — buyurtma kiritish/yangilash; body da user_id va rol tekshiruvi.

3. **Xavfsizlik va xato**
   - Baza ulanishi yo‘q bo‘lsa (supabase None) xabar: "Baza ulanishi yo‘q".
   - Barcha API’larda try/except, foydalanuvchiga tushunarli `{"error": "..."}` (raw traceback yo‘q).

4. **Frontend**
   - `public/sales.html` — `/api/sales/clients?user_id=...` chaqiruvi, javobda xato bo‘lsa ko‘rsatish, saveOrder da out.error tekshiruvi.

5. **1-xomaki versiya**
   - Commit & push keyingi qadam (foydalanuvchi GitHub ulanishini tekshiradi).
