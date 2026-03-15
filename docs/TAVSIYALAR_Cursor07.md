# Xalqaro tajriba asosida tavsiyalar (Cursor-07)

**Maqsad:** Tizimda bo‘lishi kerak bo‘lgan modullar va funksiyalar — xalqaro ERP/logistika tajribasiga ko‘ra.

---

## 1. Audit va hisobotlar

- **KPI dashboard:** Kunlik/haftalik/hoy o‘rtacha reys, quyilgan m³, o‘rtacha yetkazish vaqti, overtime foizi.
- **Mijoz va operator faoliyati hisoboti:** Kim qancha buyurtma berdi, qaysi operator qancha reys boshqardi.
- **Eksport:** Buyurtmalar va hisobotlarni CSV/Excel ga eksport (narxlar, soliqlar, auditoriya uchun).

---

## 2. To‘lov va moliya

- **Hisob-faktura (invoice) generatsiyasi:** Har bir buyurtma/reys uchun avtomatik hisob-faktura (PDF yoki link), qisman to‘lov va to‘liq to‘lov holatlari.
- **To‘lov holati:** Mijoz to‘ladi / haydovchi qabul qildi / keyinroq — bitta joyda ko‘rinishi va NOTIF orqali xabar.
- **Chegirma va narx sozlamalari:** Admin tomonidan marka/zonaga qarab chegirma va “bepul daqiqa” sozlashi (cursor_contex da eslatilgan).

---

## 3. Navbat va kapacitet

- **Navbat boshqaruvi (queue):** Buyurtmalar navbatida ketma-ketlik, urg‘ulik (VIP / muddat) va mikser bandligi asosida reyslarni avtomatik yoki yarim avtomatik tayinlash.
- **Mikser/transport kapaciteti:** Qaysi mikser qachon bo‘sh, taxminiy qaytish vaqti (GPS-02 bilan bog‘liq).

---

## 4. Xavfsizlik va audit

- **Audit log:** Kim, qachon, qanday o‘zgartirish qilgani (buyurtma statusi, narx, rol) — jadval yoki log fayl.
- **RLS (Supabase):** Har bir jadval uchun rol asosida o‘qish/yozish qoidalari (cursor_contex da ta’kidlangan).
- **Session/timeout:** Mini App da uzoq vaqt ishlatmasa yoki rol o‘zgarsa, qayta kirish so‘rashi.

---

## 5. Qo‘shimcha modullar (task sifatida qo‘shish mumkin)

| Yangi ID | Tavsiya | Izoh |
|----------|---------|------|
| **AUDIT-01** | Audit log (kim, nima, qachon) | Backend + Supabase jadval |
| **REPORT-01** | KPI dashboard (admin) | Kunlik/haftalik ko‘rsatkichlar |
| **INV-01** | Hisob-faktura generatsiyasi | PDF yoki link, qisman/to‘liq to‘lov |
| **QUEUE-01** | Navbat boshqaruvi (buyurtma → reys) | Operator uchun navbat va urg‘ulik |
| **EXPORT-01** | Buyurtmalar/hisobotlarni CSV/Excel eksport | Admin/Sales uchun |

Ushbu modullar `docs/PLAN.md` ga "4. Cursor-07 tavsiya tasklari" bo‘limi sifatida qo‘shilishi mumkin.
