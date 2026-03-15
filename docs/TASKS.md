# MirBeton ERP — Task ro'yxati (Cursor-01 natijasi)

## Manba
`docs/cursor_contex.md` va loyiha kodi tahlilidan kelib chiqqan. Yakunlanmagan yoki noto'g'ri bajarilgan ishlar ro'yxati.

---

## Cursor agent tasklari

| ID | Vazifa | Holat | Izoh |
|----|--------|-------|------|
| **Cursor-01** | Loyiha kodini o'qib, yakunlanmagan/noto'g'ri tasklarni aniqlash | ✅ Bajarildi | Ushbu TASKS.md |
| **Cursor-02** | Har bir rol uchun UI dizayn talablari va dizayn | ⬜ Ochiq | Zamonaviy biznes, UX, moslashuvchan, O'zbekiston foydalanuvchilari |
| **Cursor-03** | "Keyin qilamiz" o'rniga keyin bajariladigan tasklar ro'yxatini saqlab borish | ⬜ Ochiq | Vaqti kelganda bajarish |
| **Cursor-04** | Har taskdan keyin qisqa note (qaysi task, nima qilindi) | ⬜ Ochiq | Alohida md fayllar yoki ushbu hujjat |
| **Cursor-05** | `.cursorrules` yaratish, kerakli diqqat qilinadigan narsalar | ⬜ Ochiq | Loyiha konvensiyalari |
| **Cursor-06** | Kod chalkashligi va ishlamaslikni tuzatish, 1-xomaki versiya main branch commit & push | 🔄 Jarayonda | Backend API qo'shildi, keyingi qadamlar |
| **Cursor-07** | Xalqaro tajribadan tizimda bo'lishi kerak bo'lgan modullarni tavsiya qilish | ⬜ Ochiq | Audit hisobotida qisqacha |

---

## Biznes tasklari (MT, GPS, NOTIF)

| ID | Vazifa | Holat |
|----|--------|-------|
| **MT-01** | Mijoz tomonidan reyslarni to'xtatish (Stop-at-trip) so'rov funksiyasi | ⬜ Ochiq |
| **MT-02** | To'xtatilgan vaqtdagi hajm uchun Partial Invoice (qisman hisob) | ⬜ Ochiq |
| **MT-03** | Stop-at-trip so'rovini tasdiqlash, qisman hisob yaratish | ⬜ Ochiq |
| **MT-04** | Buyurtma hajmini oshirish so'rovi (Stop-at-trip teskarisi), mantiq va UI | ⬜ Ochiq |
| **GPS-01** | Admin panelda barcha aktiv mikserlarni xaritada ko'rsatish | ⬜ Ochiq |
| **GPS-02** | Admin: aktiv mikserlar yo'lda/bo'sh/yetib borgan/qaytyapti, taxminiy qaytish vaqti, dashboard | ⬜ Ochiq |
| **GPS-03** | Haydovchiga mijoz manzilini 1 tugma orqali tashqi xaritada ochish | ⬜ Ochiq |
| **NOTIF-01** | Har bir status o'zgarganda tegishli rolga Telegram orqali inline-buttonli xabarlar | ⬜ Ochiq |

---

## Backend/Frontend yetishmayotgan qismlar (tahlil natijasi)

- ~~**API yo'q:** `GET /api/prices`, `POST /api/order`~~ — **Cursor-06 da qo'shildi** (api/routes/landing.py).
- ~~**API yo'q:** `GET /api/sales/clients`, `POST /api/orders/upsert`~~ — **Cursor-06 da qo'shildi** (api/routes/sales.py).
- **Admin:** `admin.html` — statistika va foydalanuvchi boshqaruvi bo'sh (JS/API ulanmagan).
- **Driver/Prod_ops:** `trip_id`, buyurtma ma'lumotlari hardcoded (1, #MB-2603-01); real ro'yxat va API dan kelishi kerak.
- **Auth:** Har bir API da `user_id` va rol tekshiruvi (RLS yoki backend) hali to'liq qo'llanmagan.
- **Supabase:** Jadval struktura (orders, order_trips, users, logs) va RLS hujjatlari loyihada ko'rinmayapti — tekshirish kerak.

---

## Keyinroq bajariladigan ishlar (Cursor-03)

- [ ] Multi-trip mantiqi (hajm > 10 m³ → bir nechta reys).
- [ ] Overtime hisoblash (quyish 60 daqiqadan oshsa qo'shimcha haq).
- [ ] Markazdan uzoq buyurtmalar uchun qo'shimcha yo'l haqi va operator tasdiqlashi.
- [ ] Internet uzilganda (offline) mantiq va rollar uchun yo'riqnoma.
- [ ] Concurrency: bir xil reysni bir nechta operator/haydovchi yangilashda race condition oldini olish.

---

*Yakunlandi: Cursor-01. Keyingi qadam: Cursor-06 (ishlaydigan 1-xomaki versiya) va Cursor-05 (.cursorrules).*
