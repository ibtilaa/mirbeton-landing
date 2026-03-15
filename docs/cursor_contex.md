# ⬡ MirBeton ERP — Project Context & Cursor Agent Instructions

## 1. LOYIHA MAQSADI (Project Mission)
Samarqanddagi "MirBeton" zavodi uchun ishlab chiqarish, sotuv va logistika jarayonlarini to'liq avtomatlashtiruvchi kompleks ERP tizimi. Tizim Telegram Bot (Aiogram) va Telegram Mini App (MPA - Multi Page Application) arxitekturasida ishlaydi.

## 2. TEXNOLOGIK STAK (Tech Stack)
- **Backend:** FastAPI (Python 3.10+), Vercel Serverless Functions.
- **Bot Framework:** Aiogram 3.x (Webhook mode).
- **Database:** Supabase (PostgreSQL) + PostgREST.
- **Frontend:** Vanilla JS, Tailwind CSS, Telegram WebApp API.
- **Design System:** "Dark Industrial" (Black, Lime, Slate palette, Optional). Dark/Light

## 3. FOYDALANUVCHI ROLLARI VA FLOWLAR
1. **Admin:** Foydalanuvchi huquqlari (Role management), umumiy statistika, ruxsatlar, tizim sozlamalari, bot yuboradigan eslatma xabarlarni yuborish/yubormaslik va yuborish vaqtlari yoqish/o'chirish, bepul kutish daqiqasini sozlash pullik daqiqalar narxini sozlash va boshqa biznes tizim talabrini hisobga olishi kerak.
2. **Sales (Sotuv):** Buyurtma kiritish, buyurtma tafsilotlarini ko'rish, tahrirlash, chegirma berish bermaslik, yakuniy narxlarni belgilash, mijoz arizalarini tasdiqlash/bekor qilish. Har bir buyurtma va mijozlarni boshqarish
3. **Prod Ops (Operator):** Buyurtmani ko'rish, ishlab chiqarishni boshlash, mikserga quyish, haydovchi biriktirish, navbatni boshqarish, ko'p reysli buyurtmalarni boshqarish.
4. **Driver (Haydovchi):** Reys statuslari (mahsulot yuklandi (prod Ops tominidan xabar): jonadim -> manzildaman -> quyishni boshladim -> tugatdim -> to'lovni qabul qildim(mijoz haydovchi orqali to'laganda)), GPS kuzatuv.
5. **Client (Mijoz):** Buyurtma berish, reyslarni kuzatish, avtomatik invoys olish, qisman/to'liq/keyinroq to'lash tugma orqali (bunda mijoz to'lov qildi lekin haydovchi keyinroq to'layman dedi deyishini oldini olish uchun).

## 4. TANQIDIY TAHLIL VA TEKSHIRUV NUQTALARI (Critical Audit Areas)
Cursor agenti kodni o'qiyotganda quyidagi xavfsizlik va mantiqiy xatolarni qidirishi shart:

- **Auth & Security:** URL parametrlaridan kelayotgan `user_id` ni har bir API so'rovda Supabase orqali rolni (role-based access) tekshirish.
- **Concurrency:** Bir vaqtning o'zida bir nechta haydovchi yoki operator bir xil reysni yangilashga urinishi (Race conditions).
- **Error Handling:** Vercel Serverless bo'lgani uchun 10 soniyalik timeout va xotira cheklovlarini hisobga olish.
- **Supabase RLS:** Row Level Security qoidalarini bazada va kodda to'g'ri qo'llash.
- **Internet aloqosa uzilib qolsa nima qilinadi** Internetsiz hududlarda tizim nima qiladi va rollar nima qiladi mantiqni ishlab chiqish.

## 5. FUNKSIONAL TALABLAR (Business Logic)
- **Multi-trip Logic:** Buyurtma hajmi (m³) mikser sig'imidan (10m³) oshsa, tizim uni avtomatik reyslarga bo'lishi kerak.
- **Overtime Calculation:** Beton quyish vaqti (`pouring` -> `completed`) 60 daqiqadan oshsa, har belgilangan daqiqa uchun qo'shimcha haq hisoblash.
- **Markazdan uzoqda buyurtmalar:** belgilangan raduisdan uzoqda bo'lgan buyurtmalar uchun operator qo'shimcha yo'l haqini belgilashi kelishishi va buyurtmani tasdiqlashi kerak.
- **GPS Tracking:** Haydovchi harakatlanayotganda `navigator.geolocation/yoki boshqa optimal yechim` orqali koordinatalarni `order_trips` va `order_logs` jadvallariga yozib borish. Mazilga yetib borish va qaytish vaqtlarini taxmin qilish mijozlar va operatorlash uchun navbatni boshqarish uchun muhim ma'lumot.

## 6. YAKUNLASH UCHUN TASKLAR (Pending Tasks)
- [ ] **Cursor-01:** Tasklarni bajarishdan oldin loyiha sourse kodini o'qib chiq va yakunlamagan yoki to'g'ri bajarilmagan tasklarni aniqlab Tasklar ro'yxatiga qo'sh.
- [ ] **Cursor-02:** UI dizayni talablarini ishlab chiqa har bir rol uchun va shu bo'yicha dizayn qil. Dizayn qilishda Zamonaviy biznes turi, UX (rang tanlash va garafikada ayniqsa) talablari, moslashuvchan, maksumal sodda lekin kerakli qismlar, grafik uslubda zamonaviy dunyo tajribasidan kelib chiqib va O'zbekiton foydalanuvchilari hisobga ol.
- [ ] **Cursor-03:** qilinishi kerak bo'lgan ishni qil keyin qilamiz dema. keyin qilinishi kerak bo'lsa keyinroq qilinishi kerak bo'lgan tasklar ro'yxatini tuzib bor qachon qilinishini qayda qilib bor vaqti kelgan bajarish uchun.
- [ ] **Cursor-04:** Har taskdan keyin maxsus md fayli qaysi task bo'yicha nimalar qilgani haqida qisqa note'lar yozib bor. 
- [ ] **Cursor-05:** .cursorrules faylini yaratib kerakli qilish e'tibor qilishing kerak bo'lgan narsalarni yozib qo'y.
- [ ] **Cursor-06:** Loyihaning hozirgi yozilgan kodlari juda chalkash va hozir to'liq ishlamayapt muamoni aniqlab mantiqni tushunib tuzat ishlaydigan qil va 1-xomaki versiya sifatida main branch commit & push qil. agar githubga ulanishda muammo bo'lsa tuzat tuzata olmasang nima qilishni menga ayt.
- [ ] **Cursor-07:** Men hisobga olmagan lekin tizimda bo'lisshi kerak bo'lgan modeullarni xalaqaro tajribani o'rganib menga ayt va ularni ham tasklarga qo'sh. Tavsiya qil. 
- [ ] **MT-01:** Mijoz tomonidan reyslarni to'xtatishga (Stop-at-trip) so'rov funksiyasi.
- [ ] **MT-02:** To'xtatilgan vaqtdagi hajm uchun `Partial Invoice` (qisman hisob) yaratish.
- [ ] **MT-03:** (Stop-at-trip) so'rovini tasdiqlash, qisman hisob yatish. Izoh: 1-holat mijoz buyurtmani shu joyida bekor qilishi. 2-tez-tez ucharaydigan holat. Bunda mijoz keragidan ko'p buyurtma berib qo'yadi va bo'ldi shunchasi yetarkan deyidi (buyurtma hali ishlab chiqarilishida oldin).
- [ ] **MT-04:** MT-03 Stop-at-trip so'rovinig teskarisi mijoz keragidan kam buyurtma qilganini bilib qoladi va buyurtma hajmini oshirishni so'raydi. shu kabi real bo'ladi holatlarrni hisobga olib mantiqni va ui ni yarat. qo'shimchani yangi buyurtma sifatida qayd qilamizmi yoki qo'shimcha bo'ldi kabimi? professional yechim top.
- [ ] **GPS-01:** Admin panelda barcha aktiv mikserlarni xaritada ko'rsatish (Map integration).
[ ] **GPS-02:** Admin panelda barcha aktiv mikserlar yolati yo'lda, bo'sh, yetib borgan yuyapti, qaytyapti taxminiy qaytib kelish vaqti gps ma'lumotlari asosida, kabi pro ui/ux blok (dashboard) yarat.
[ ] **GPS-03** Haydovchiga mijoz agar mijoz geolokatsiya yuborgan bo'lsa, 1ta tugma orqali mazilga marshurt yoki mazilni ko'rish uchun tashqi ilovada manzilni ochib beradigan qil. 
- [ ] **NOTIF-01:** Telegram bot orqali har bir status o'zgarganda tegishli rolga chiroyli Inline-buttonli tabiiy inson va korparativ tushunarli xabarlar yuborish.

## 7. CHEKLOVLAR (Constraints)
- Faqat `public/` papkasidagi HTML/JS fayllarni frontend sifatida ishlatish.
- `index.py` fayli o'lchamini optimal saqlash, mantiqni modullarga bo'lish tavsiya etiladi.
- Hech qachon foydalanuvchiga xom xatolikni (Raw Traceback) ko'rsatma, faqat chiroyli xato xabari.
- index.html, order.js, prices.js fayllarini o'zgartirish mumkin emas. Ular hozir loyihamizda tashqari module. biznesning landing sahifasi va web orqali buyurtma lid qabul qilish price haqida ma'lumot beruvchi sahifasi bo'lib uni vercel muhitida ishlab turishini taminlash kerak bizning loyihamiz bilan bir source code ichida. Tahlil qilishing mumkin.

---
**Cursor Agent uchun ko'rsatma:** Ushbu faylni o'qib bo'lgach, loyihani tahlil qil va birinchi navbatda `Cursor-01` (Reysni to'xtatish mantiqi) bo'yicha kodga o'zgartirishlar kiritishni boshla.

# 🚀 DEPLOYMENT & ARCHITECTURE GUIDE (For AI Agent)

## 1. INFRASTRUKTURA (Infrastructure)
Loyiha quyidagi platformalarda "Serverless" va "Cloud-native" prinsiplari asosida ishlaydi:

- **Hosting (Backend & Frontend):** [Vercel](https://vercel.com).
  - Backend `api/index.py` faylida FastAPI orqali boshqariladi.
  - Vercel Serverless Functions cheklovlari: Timeout 10s (Hobby) / 15-30s (Pro). Long-polling taqiqlangan.
- **Database & Auth:** [Supabase](https://supabase.com).
  - PostgreSQL ma'lumotlar bazasi.
  - Ma'lumotlarga to'g'ridan-to'g'ri `supabase-py` SDK orqali ulaniladi.
- **Bot Platform:** Telegram Webhooks.
  - Aiogram 3.x kutubxonasi FastAPI orqali `POST /api/webhook` endpointida ishlaydi.

## 2. ARXITEKTURA STRUKTURASI (Folder Logic)
Loyiha **MPA (Multi-Page Application)** modelida qurilgan:

```text
/
├── api/
│   └── index.py         # Yagona backend kirish nuqtasi (FastAPI + Aiogram)
├── public/              # Statik frontend (Vercel buni / orqali xizmat qiladi)
│   ├── css/             # Umumiy Industrial Dark dizayn (style.css)
│   ├── js/              # Client-side mantiq (core.js)
│   ├── admin.html       # Admin boshqaruv paneli
│   ├── sales.html       # Sotuv va buyurtma tahrirlash
│   ├── driver.html      # Haydovchi logistikasi
│   ├── prod_ops.html    # Ishlab chiqarish operatori
│   └── prices.html      # Umumiy narxlar jadvali
├── vercel.json          # Routing va rewrites (API vs Static)
└── requirements.txt     # Python dependencielari