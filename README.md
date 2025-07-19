📬 Django Contact Form Loyihasi
Ushbu loyiha oddiy aloqa formasini (Contact Form) yaratishga qaratilgan bo‘lib, foydalanuvchi tomonidan yuborilgan xabarlarni ma’lumotlar bazasiga saqlaydi va ularni jadval ko‘rinishida ko‘rsatadi.

📌 Loyihaning asosiy funksiyalari:
Foydalanuvchi: ism, familiya, telefon, email va xabar kiritadi

Forma orqali yuborilgan xabarlar POST orqali serverga jo‘natiladi

Xabarlar SQLite ma’lumotlar bazasida saqlanadi

Admin (yoki har qanday foydalanuvchi) barcha xabarlarni /xabarlar sahifasida ko‘rishi mumkin

Bootstrap yordamida chiroyli frontend dizayni

🛠 Texnologiyalar:
Python 3.10+

Django 5.x

SQLite (default)

Bootstrap 5 (CDN orqali ulangan)

🖥 Sahifalar:

URL	Tavsif

/	Asosiy sahifa, foydalanuvchi kontakt formasini to‘ldiradi
/xabarlar	Hamma yuborilgan xabarlar ro‘yxatini ko‘rsatadi

🔧 Ishga tushirish bo‘yicha ko‘rsatma

bash

git clone https://github.com/bunyod-abdulloh/django_arxiv.git
cd django_arxiv
python -m venv venv
venv\Scripts\activate  # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt

# Migratsiyalarni bajarish
python manage.py makemigrations
python manage.py migrate

# Serverni ishga tushurish
python manage.py runserver

🗃 Ma’lumotlar bazasi modeli
ContactMessage modeli quyidagi maydonlarni o‘z ichiga oladi:

first_name – Foydalanuvchining ismi

last_name – Familiyasi

phone – Telefon raqami

email – Elektron pochta manzili

message – Yuborilgan xabar matni

created_at – Yaratilgan vaqt (avtomatik)

📷 Ekran ko‘rinishlari (ixtiyoriy qo‘shishingiz mumkin):
docs/ papkasiga skrinshotlar joylab, README ichida <img> orqali ulashingiz mumkin.

✍️ Muallif
Ism: Bunyod Abdulloh

Telegram: @muhib_dev

GitHub: github.com/bunyod-abdulloh