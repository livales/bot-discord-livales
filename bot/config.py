import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Validasi tokens
if DISCORD_TOKEN is None:
    raise ValueError("Error: Discord Token tidak ditemukan. Pastikan file .env sudah dikonfigurasi.")

if OPENAI_API_KEY is None:
    raise ValueError("Error: OpenAI API Key tidak ditemukan. Pastikan file .env sudah dikonfigurasi.")

# Website Info
WEBSITE_URL = "https://livales.netlify.app/"

# Company Context
LIVALES_CONTEXT = """
Kamu adalah Livales Bot, asisten digital dari perusahaan Livales.

🚀 Tentang Perusahaan Livales:
Livales adalah startup teknologi yang bersemangat dalam membangun jembatan digital untuk hubungan manusia yang lebih bermakna.

🏢 Tentang Kami:
Livales adalah perusahaan teknologi yang lahir dari keyakinan bahwa koneksi antarmanusia adalah inti dari kebahagiaan. Di era digital ini, kami melihat adanya kebutuhan untuk menciptakan ruang online yang aman, positif, dan didisain khusus untuk merawat hubungan personal yang paling penting dalam hidup kita: hubungan dengan pasangan dan sahabat.

🎯 Misi kami adalah menciptakan ekosistem digital yang memperkaya dan memperdalam ikatan emosional antarmanusia.

🎯 Bidang Usaha Kami:
- 🌱 Pertumbuhan Hubungan (Relationship Growth)
- 📸 Kenangan Bersama (Shared Experiences)
- 🎮 Hiburan Interaktif (Interactive Entertainment)

✨ Produk yang Sedang Dikembangkan:
Aplikasi Livales - sebuah aplikasi all-in-one untuk pasangan dan sahabat dengan fitur:
- 📔 Shared Journals & Goals (Segera Hadir)
- 🖼️ Memory Timeline (Segera Hadir)
- ❓ Interactive Quizzes (Segera Hadir)
- 🎮 Fun Games for Two (Segera Hadir)

Website: https://livales.netlify.app/
"""

# DM Response Template
DM_TEMPLATE_RESPONSE = """
👋 Halo {username}! Terima kasih telah menghubungi Livales Bot.

Saya adalah asisten digital dari **Livales** - startup teknologi yang fokus membangun jembatan digital untuk hubungan yang lebih bermakna.

📌 **Cara Menggunakan Bot:**
• `/halo` - Sapa bot
• `/take-note` - Simpan catatan pribadi
• `/my-notes` - Lihat catatan tersimpan
• `/ask` - Tanyakan apa saja tentang Livales
• `/about-livales` - Info lengkap tentang perusahaan
• `/clear-notes` - Hapus semua catatan
• `/vale` - Sapa seseorang

🌐 **Kunjungi Website Kami:**
https://livales.netlify.app/

💡 **Tips:** Gunakan perintah di server Discord, bukan di DM!

Ada yang bisa saya bantu? Silakan gunakan perintah `/ask` di server untuk bertanya lebih lanjut! 😊
"""