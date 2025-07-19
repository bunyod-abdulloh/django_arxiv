# 📬 Django Contact Form Loyihasi

Oddiy kontakt formasini yaratish uchun mo‘ljallangan loyiha. Foydalanuvchi yuborgan xabarlar ma’lumotlar bazasiga saqlanadi va admin tomonidan ko‘riladi.

---

## 📌 Asosiy Funksiyalar

✅ Foydalanuvchi quyidagi maydonlarni to‘ldiradi:
- Ism
- Familiya
- Telefon raqami
- Email manzili
- Xabar matni

✅ Yuborilgan xabarlar:
- `POST` so‘rovi orqali serverga yuboriladi
- `SQLite` bazasiga saqlanadi
- `/xabarlar` sahifasida ro‘yxat ko‘rinishida ko‘rsatiladi

✅ Frontend:
- `Bootstrap 5` yordamida soddaligi va chiroyli interfeys

---

## 🛠 Texnologiyalar

- ⚙️ Python 3.10+
- 🌐 Django 5.x
- 🗄 SQLite (standart)
- 🎨 Bootstrap 5 (CDN orqali ulangan)

---

## 🖥 Sahifalar

| URL            | Tavsif                                                  |
|----------------|----------------------------------------------------------|
| `/`            | Asosiy sahifa. Foydalanuvchi aloqa formasini to‘ldiradi |
| `/xabarlar`    | Admin (yoki foydalanuvchi) barcha xabarlarni ko‘radi     |

---

## 🗃 Ma’lumotlar Bazasi Modeli

### `ContactMessage` modelidagi maydonlar:

| Maydon nomi   | Tavsif                        |
|---------------|-------------------------------|
| `first_name`  | Foydalanuvchining ismi        |
| `last_name`   | Familiyasi                    |
| `phone`       | Telefon raqami                |
| `email`       | Email manzili                 |
| `message`     | Yuborilgan xabar              |
| `created_at`  | Yaratilgan vaqt (avtomatik)   |

---

## 🚀 Ishga tushirish (Local)

```bash
# 1. Loyihani klonlash
git clone https://github.com/bunyod-abdulloh/django_arxiv.git
cd project

# 2. Virtual muhit yaratish
python -m venv venv
venv\Scripts\activate  # Linux/macOS: source venv/bin/activate

# 3. Talablarni o‘rnatish
pip install -r requirements.txt

# 4. Migratsiyalar
python manage.py makemigrations
python manage.py migrate

# 5. Serverni ishga tushurish
python manage.py runserver


✍️ Muallif
👤 Ism: Bunyod Abdulloh
📬 Telegram: @muhib_dev
💻 GitHub: github.com/bunyod-abdulloh