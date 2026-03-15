# MirBeton ERP — Barcha tasklar reja (ketma-ketlik)

**Manba:** `docs/cursor_contex.md`. Yangilanish: har task bajarilgach [X] qo‘yiladi va `docs/notes/` da note yoziladi.

---

## 1. Cursor agent tasklari (birinchi navbatda bitta-bitta)

- [X] **Cursor-01** — Loyiha kodini o‘qib, yakunlanmagan/noto‘g‘ri tasklarni aniqlash va ro‘yxatga olish.
- [X] **Cursor-02** — Har bir rol uchun UI dizayn talablari va dizayn (zamonaviy biznes, UX, moslashuvchan, O‘zbekiston). 1-bosqich: talablar hujjati, CSS, admin sahifa API bilan.
- [X] **Cursor-03** — “Keyin qilamiz” o‘rniga keyin bajariladigan tasklar ro‘yxatini saqlab borish (vaqt belgilash).
- [X] **Cursor-04** — Har bajarilgan taskdan keyin qisqa note (qaysi task, nima qilindi) — `docs/notes/` da.
- [X] **Cursor-05** — `.cursorrules` yaratish/yangilash, kerakli diqqat qilinadigan narsalar.
- [X] **Cursor-06** — Kod chalkashligi va ishlamaslikni tuzatish; modulli tartib; 1-xomaki versiya main branch commit & push.
- [X] **Cursor-07** — Xalqaro tajribadan tizimda bo‘lishi kerak bo‘lgan modullarni tavsiya qilish va tasklarga qo‘shish.

---

## 2. Biznes tasklari (MT, GPS, NOTIF)

- [ ] **MT-01** — Mijoz tomonidan reyslarni to‘xtatish (Stop-at-trip) so‘rov funksiyasi.
- [ ] **MT-02** — To‘xtatilgan vaqtdagi hajm uchun Partial Invoice (qisman hisob) yaratish.
- [ ] **MT-03** — Stop-at-trip so‘rovini tasdiqlash, qisman hisob yatish.
- [ ] **MT-04** — Buyurtma hajmini oshirish so‘rovi (Stop-at-trip teskarisi), mantiq va UI.
- [ ] **GPS-01** — Admin panelda barcha aktiv mikserlarni xaritada ko‘rsatish.
- [ ] **GPS-02** — Admin: aktiv mikserlar yo‘lda/bo‘sh/yetib borgan/qaytyapti, taxminiy qaytish vaqti, dashboard.
- [ ] **GPS-03** — Haydovchiga mijoz manzilini 1 tugma orqali tashqi xaritada ochish.
- [ ] **NOTIF-01** — Har bir status o‘zgarganda tegishli rolga Telegram orqali inline-buttonli xabarlar.

---

## 3. Keyinroq bajariladigan ishlar (Cursor-03 ro‘yxatida saqlanadi)

- [ ] Multi-trip mantiqi (hajm > 10 m³ → bir nechta reys).
- [ ] Overtime hisoblash (quyish 60 daqiqadan oshsa qo‘shimcha haq).
- [ ] Markazdan uzoq buyurtmalar uchun qo‘shimcha yo‘l haqi va operator tasdiqlashi.
- [ ] Internet uzilganda (offline) mantiq va rollar uchun yo‘riqnoma.
- [ ] Concurrency: bir xil reysni bir nechta operator/haydovchi yangilashda race condition oldini olish.

---

## 4. Cursor-07 tavsiya tasklari (xalqaro tajriba)

- [ ] **AUDIT-01** — Audit log (kim, nima, qachon o‘zgartirdi).
- [ ] **REPORT-01** — KPI dashboard (admin): kunlik/haftalik ko‘rsatkichlar.
- [ ] **INV-01** — Hisob-faktura generatsiyasi (PDF/link, qisman/to‘liq to‘lov).
- [ ] **QUEUE-01** — Navbat boshqaruvi (buyurtma → reys, urg‘ulik).
- [ ] **EXPORT-01** — Buyurtmalar/hisobotlarni CSV/Excel eksport.

Tafsilot: `docs/TAVSIYALAR_Cursor07.md`.

---

## Ketma-ketlik qisqacha

1. **Cursor-01** → **Cursor-05** (qoidalar va reja) → **Cursor-06** (ishlaydigan versiya, modulli kod).
2. Keyin **Cursor-02** (dizayn), **Cursor-04** (har taskdan note), **Cursor-03** (keyinroq ro‘yxati), **Cursor-07** (tavsiyalar).
3. Keyin **MT-01 … MT-04**, **GPS-01 … GPS-03**, **NOTIF-01**.

---

*Har task bajarilgach: bu faylda [X] qo‘ying va `docs/notes/<task_id>_note.md` yozing.*
