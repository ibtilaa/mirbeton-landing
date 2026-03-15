# UI dizayn talablari — har bir rol uchun (Cursor-02)

**Maqsad:** Zamonaviy biznes turi, yaxshi UX, moslashuvchanlik, O‘zbekiston foydalanuvchilari va grafik uslub (Dark Industrial) asosida har bir rol uchun talablar.

---

## Umumiy printsiplar

- **Design system:** Dark Industrial — fon `#0b0d0a` / `#121511`, chegaralar `#242a20`, asosiy rang lime `#9dc45a`, admin binafsha `#9b78f0`, haydovchi to‘q sariq `#f07840`. Ixtiyoriy light theme.
- **Tipografiya:** Syne (sarlavhalar), JetBrains Mono (matn, raqamlar). Lotin o‘zbek.
- **UX:** Minimal bosishlar, katta tugmalar (barmoq uchun), statuslar aniq, xato xabarlari tushunarli.
- **Moslashuvchanlik:** Mobil birinchi (Telegram Mini App), kichik ekranlar uchun bitta ustun, katta ekranlarda grid.
- **Grafik:** Sodda chiziqlar, yumaloq burchaklar (card 20px), badge va status ranglari izchil.

---

## 1. Admin

- **Sahifa:** `admin.html` (yoki app.html?role=admin).
- **Talablar:**
  - Dashboard: bugungi/haftalik quyilgan m³, aktiv buyurtmalar soni, tasdiqlash kutilayotganlar (statistik kartochkalar).
  - Foydalanuvchilar boshqaruvi: ro‘yxat (ism, telefon, rol, faol), tahrirlash (rol, telefon, is_active). Rol tanlash: client / sales / prod_ops / driver / admin.
  - Tizim sozlamalari (keyinroq): eslatma vaqtlari, bepul daqiqa, qo‘shimcha daqiqa narxi.
- **Komponentlar:** Kartochkalar (industrial-card), jadval yoki ro‘yxat, select/input, saqlash tugmasi. Admin rang binafsha (border-left yoki badge).

---

## 2. Sales (Sotuv)

- **Sahifa:** `sales.html`.
- **Talablar:**
  - Yangi buyurtma: mijoz tanlash (select), marka (M300 va b.), hajm, 1m³ narx, manzil. Saqlash tugmasi.
  - Tasdiqlash kutilmoqda: ro‘yxat (buyurtma ID, mijoz, hajm, manzil, tasdiqlash/bekor qilish tugmalari).
  - Tahrirlash: chegirma, yakuniy narx, status (pending / confirmed / cancelled).
- **Komponentlar:** Forma (input-field, btn-prime), kartochkalar ro‘yxati, status badge (rang: kutilmoqda — sariq, tasdiqlandi — yashil).

---

## 3. Prod Ops (Ishlab chiqarish operatori)

- **Sahifa:** `prod_ops.html` / app.html?role=prod_ops.
- **Talablar:**
  - Navbat: buyurtma/reys ro‘yxati (ID, mijoz, marka, hajm, status). Ketma-ketlik aniq.
  - Har bir reys uchun: haydovchi tanlash (select), “Betonni quyish” tugmasi — status poured va haydovchiga xabar.
  - Ko‘p reysli buyurtmalar (keyinroq): bir buyurtma bir nechta reys — har biri alohida boshqariladi.
- **Komponentlar:** Kartochka (border-left ko‘k yoki lime), select, bitta asosiy harakat tugmasi. Status: kutilmoqda / quyildi / yo‘lda / tugadi.

---

## 4. Driver (Haydovchi)

- **Sahifa:** `driver.html` / app.html?role=driver.
- **Talablar:**
  - Faol reys: buyurtma ID, mijoz (ism, tel), manzil. Tugmalar: “Manzilni xaritada ochish” (GPS-03), “Qo‘ng‘iroq”.
  - Status tugmalari (katta, bitta ustunda): Jo‘nadim → Manzildaman → Tugatdim (va ixtiyoriy “To‘lovni qabul qildim”). Har bir bosishda GPS (lat/lng) yuboriladi.
- **Komponentlar:** Bitta katta kartochka (faol reys), 3–4 ta aniq tugma. Ranglar: jo‘nadim — lime/orange, manzilda — ko‘k, tugatdim — oq/qora.

---

## 5. Client (Mijoz)

- **Sahifa:** Mini App da mijoz ko‘rinishi (buyurtma berish bot orqali, reyslarni kuzatish).
- **Talablar:**
  - Mening buyurtmalarim: ro‘yxat (ID, sana, status, hajm, narx). Tanlash → tafsilot.
  - Reys statusi: yo‘lda / yetib keldi / quyilmoqda / tugadi. Invoyt (keyinroq), to‘lov tugmalari (qisman / to‘liq / keyinroq).
- **Komponentlar:** Sodda ro‘yxat, status badge, to‘lov va invoys (NOTIF-01 va INV-01 bilan).

---

## 6. Texnik qoidalar (public/)

- Barcha sahifalarda `public/CSS/style.css` ulangan bo‘lsin; Tailwind ishlatilsa CDN yoki style.css da ekvivalent (grid, gap, border-l-*, text-*) qo‘shilsin.
- Telegram WebApp: `Telegram.WebApp` expand, themeParams ixtiyoriy. Tugmalar uchun `:active` scale (0.96–0.98).
- Ranglar CSS variables orqali (`:root` da); light theme uchun `[data-theme="light"]` (ixtiyoriy).

---

**Keyingi qadam:** Ushbu talablar asosida admin.html va sales.html da minimal ishlov (statistika API, foydalanuvchilar ro‘yxati, grid/badge ko‘rinishi) — keyin boshqa sahifalar ketma-ket yangilanadi.
