# Cursor-01 va Cursor-06 bo'yicha qisqa note (Cursor-04)

**Sana:** 2026-03-16

## Cursor-01
- Loyiha kodi to'liq o'rganildi: `api/index.py`, `public/*.html`, `public/JS/core.js`, `public/CSS/style.css`, `vercel.json`, `index.html`, `api/order.js`, `api/prices.js`.
- Yakunlanmagan / noto'g'ri tasklar aniqlandi va `docs/TASKS.md` ga yozildi (Cursor, MT, GPS, NOTIF, backend/frontend yetishmovchiliklari).
- Tanqidiy tahlil: `docs/CRITICAL_AUDIT.md`.

## Cursor-06 (1-xomaki versiya — qisman)
- **Qilingan:** Landing ishlashi uchun backend da yetishmayotgan API lar qo'shildi:
  - `GET /api/prices` — narxlar CSV (Google Sheets proxy yoki default).
  - `POST /api/order` — buyurtma arizasi Google Apps Script ga proxy.
- **Env:** `GOOGLE_SHEETS_CSV_URL` (mavjud), `GOOGLE_ORDER_SCRIPT_URL`, `GOOGLE_ORDER_SECRET` (ixtiyoriy, default bor).
- **Hali qilinmagan:** Sales/Admin/Driver/Prod_ops uchun API va UI to'ldirish, auth/concurrency, main branch commit & push.

## Keyingi qadamlar
- Cursor-05: `.cursorrules` yaratildi.
- Cursor-06 davomi: sales API, keyin boshqa rollar va commit/push.
