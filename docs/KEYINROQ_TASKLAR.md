# Keyinroq bajariladigan tasklar (Cursor-03)

**Maqsad:** "Keyin qilamiz" o‘rniga barcha keyinroq ishlar bitta ro‘yxatda, qachon va qayerda bajarilishi aniq.

**Yangilanish:** Vaqt kelganda bu faylda status o‘zgartiriladi va PLAN.md da [X] qo‘yiladi.

---

## Ro‘yxat (qachon / qayerda)

| Task | Qachon bajariladi | Qayerda (PLAN / modul) | Holat |
|------|-------------------|------------------------|-------|
| Multi-trip mantiqi (hajm > 10 m³ → bir nechta reys) | MT-01…NOTIF-01 dan keyin yoki parallel | PLAN §3, backend order_trips | [ ] |
| Overtime hisoblash (quyish 60 dk oshsa qo‘shimcha haq) | Multi-trip dan keyin | PLAN §3, backend + hisob-faktura | [ ] |
| Markazdan uzoq buyurtmalar (qo‘shimcha yo‘l haqi, operator tasdiqlashi) | Overtime yoki MT-04 bilan | PLAN §3, sales/operator UI | [ ] |
| Internet uzilganda (offline) mantiq va rollar yo‘riqnomasi | NOTIF-01 dan keyin | PLAN §3, docs + frontend cache | [ ] |
| Concurrency (bir xil reysni bir nechta yangilash, race condition) | Backend stabil holatda | PLAN §3, api/routes/driver.py va prod.py | [ ] |

---

## Qisqa izoh

- **Qachon:** MT, GPS, NOTIF asosiy flow ishlagach, keyinroq ishlar ustuvorlik bo‘yicha shu jadvalda sanaladi.
- **Qayerda:** PLAN.md ning "3. Keyinroq bajariladigan ishlar" bo‘limi va kerak bo‘lsa alohida task (masalan NOTIF-02) sifatida qo‘shiladi.
- Vaqti kelganda yangi "keyinroq" tasklar ham shu jadvalga qo‘shiladi.
