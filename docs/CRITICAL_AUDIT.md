# MirBeton ERP — Tanqidiy tahlil (Software Audit)

**Sana:** 2026-03-16  
**Maqsad:** Loyihani mutaxassis sifatida to'liq tanqidiy tahlil qilish (docs/cursor_contex.md va kod asosida).

---

## 1. Loyiha maqsadi va stak

- **Maqsad:** MirBeton zavodi uchun ishlab chiqarish, sotuv va logistika jarayonlarini avtomatlashtiruvchi ERP (Telegram Bot + Mini App).
- **Stak:** FastAPI (Python), Aiogram 3.x, Supabase (PostgreSQL), Vanilla JS + Tailwind, Telegram WebApp, Vercel Serverless.

---

## 2. Arxitektura va routing

- **Vercel:** `vercel.json` da barcha ` /api/(.*) ` → ` /api/index.py ` ga yo'naltirilgan. Demak, `api/order.js` va `api/prices.js` (Node.js serverless) **hech qachon chaqirilmaydi**, chunki barcha `/api/*` so'rovlar Python `index.py` ga tushadi.
- **Natija:** Landing (`index.html`) `/api/prices` va `/api/order` dan foydalanadi, lekin bu endpoint'lar `index.py` da **yo'q**. Landing narxlari va buyurtma yuborish hozir **ishlamaydi** (404 yoki xato).
- **Tavsiya:** `index.py` ga `GET /api/prices` (CSV proxy) va `POST /api/order` (Google Script proxy) qo'shish — yoki `vercel.json` da faqat backend route'larini `index.py` ga, qolganini Node function'larga yo'naltirish.

---

## 3. Backend (api/index.py)

**Mavjud:**
- Bot: `/start`, kontakt, `/narxlar`, WebApp havolasi.
- API: `POST /api/webhook`, `POST /api/prod/pour`, `POST /api/driver/event`, `GET /api/admin/users`, `POST /api/admin/update-user`.

**Kamchiliklar:**
- **Auth:** Faqat admin endpoint'larida `user_id` va `role` tekshiriladi. `prod_pour` va `driver_event` da **foydalanuvchi/rol tekshiruvi yo'q** — har kim `trip_id` yuborib status yangilashi mumkin.
- **Xavfsizlik (cursor_contex):** URL/body dan keladigan `user_id` har bir API da Supabase orqali rolni tekshirish talab qilinadi — hozircha to'liq qo'llanmagan.
- **Concurrency:** Bir xil `trip_id` ni bir vaqtda bir nechta operator/haydovchi yangilashi (race condition) hisobga olinmagan.
- **Error handling:** Try/except va foydalanuvchiga tushunarli xabar (raw traceback ko'rsatmaslik) hamma joyda yo'q.
- **Yetishmayotgan API:** `/api/prices`, `/api/order`, `/api/sales/clients`, `/api/orders/upsert` — ulardan frontend foydalanadi.

---

## 4. Frontend (public/)

| Sahifa | Holat | Muammo |
|--------|--------|--------|
| **admin.html** | Yarim tayyor | Statistika va foydalanuvchi bloki bo'sh; `/api/admin/users` chaqirilmaydi, dizayn (grid, Tailwind) ishlatilmagan. |
| **sales.html** | Ishlamaydi | `/api/sales/clients` va `/api/orders/upsert` backend da yo'q; `loadPending()` bo'sh. |
| **driver.html** | Mock | `trip_id: 1` va buyurtma ma'lumotlari qattiq yozilgan; real reys ro'yxati yo'q. |
| **prod_ops.html** | Mock | Navbat va haydovchilar statik; real trip/driver API yo'q. |
| **app.html** | Mock | Faqat prod_ops va driver view; sales/admin/client view yo'q; trip_id=1 qattiq. |
| **prices.html** | Format noto'g'ri | `fetch('/api/prices')` dan keyin `data.map(p => p.Marka)` — backend CSV qaytarsa, JSON emas; format mos emas. |
| **core.js** | Minimal | Faqat `apiCall()` va WebApp expand; role/user_id asosida route yoki xabar ko'rsatish yo'q. |

**Dizayn:** `style.css` da Tailwind o'xshash class'lar (`border-l-4`, `grid`, `text-lime-500`) ishlatilgan, lekin Tailwind CDN ulangan emas — bu class'lar **ishlamaydi** (faqat `app.html` da Tailwind CDN bor).

---

## 5. Tashqi modul (o'zgartirilmasin)

- **index.html:** Landing + kalkulyator + buyurtma formasi. `/api/prices` (CSV), `/api/order` (POST JSON) dan foydalanadi.
- **api/order.js, api/prices.js:** Node.js handler'lar; Vercel rewrites tufayli chaqirilmaydi. Mantiq (Google Sheets / Apps Script) backend da takrorlanishi yoki routing o'zgartirilishi kerak.

---

## 6. Xavfsizlik va cheklovlar (cursor_contex dan)

- **RLS (Supabase):** Loyihada RLS qoidalari va jadval sxemasi ko'rinmayapti — tekshirish va hujjatlash kerak.
- **Raw traceback:** Hech qachon foydalanuvchiga ko'rsatilmasligi kerak — API da try/except va bitta formatlangan xabar qaytarish kerak.
- **Timeout/xotira:** Vercel Serverless 10s timeout; uzoq operatsiyalar va long-polling taqiqlangan.

---

## 7. Qisqa xulosa

| Yo'nalish | Baho | Asosiy muammo |
|----------|------|----------------|
| Routing / Deployment | Yomon | `/api/*` faqat index.py ga boradi; /api/prices va /api/order yo'q, landing ishlamaydi. |
| Backend API | Yarom | Asosiy flow (buyurtma, sotuv, reys) uchun endpoint'lar yetishmaydi; auth/concurrency qo'llanmagan. |
| Frontend (rol sahifalari) | Yarom | Ko'p sahifa mock yoki bo'sh; real API va rolni tekshirish yo'q. |
| Bot | Yaxshi | Start, kontakt, narxlar, WebApp havolasi ishlaydi. |
| Dizayn tizimi | Aralash | style.css bor; ba'zi sahifalarda Tailwind class'lar CSS da yo'q (Tailwind ulilmagan). |

**Birinchi ustuvorlik:** Landing va buyurtma lead'ini ishlatish uchun `index.py` da `GET /api/prices` va `POST /api/order` ni qo'shish; keyin sales va boshqa rollar uchun API va UI ni to'ldirish.
