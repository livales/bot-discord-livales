import os
import discord
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Mengecek apakah token berhasil dimuat
if DISCORD_TOKEN is None:
    print("Error: Token tidak ditemukan. Pastikan Anda sudah membuat file .env dan mengisinya dengan benar.")
    exit() # Keluar dari program jika token tidak ada

# Mengatur intents (izin) yang dibutuhkan bot
intents = discord.Intents.default()
intents.message_content = True # Diperlukan untuk beberapa jenis interaksi pesan
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    """Fungsi yang dijalankan saat bot berhasil terhubung ke Discord."""
    print(f"Bot sudah online sebagai {bot.user}!")
    print("Bot siap menerima perintah.")

@bot.slash_command(name="halo", description="Bot akan menyapa balik!")
async def halo(ctx):
    """Perintah slash sederhana untuk menyapa pengguna."""
    await ctx.respond(f"Halo juga, {ctx.author.name}! 👋")

# Menjalankan bot dengan token yang sudah dimuat
bot.run(DISCORD_TOKEN)