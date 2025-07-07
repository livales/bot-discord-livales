import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import openai
from datetime import datetime
import json

# Memuat variabel dari file .env
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Mengecek apakah token berhasil dimuat
if DISCORD_TOKEN is None:
    print("Error: Discord Token tidak ditemukan. Pastikan Anda sudah membuat file .env dan mengisinya dengan benar.")
    exit()

if OPENAI_API_KEY is None:
    print("Error: OpenAI API Key tidak ditemukan. Pastikan Anda sudah menambahkan OPENAI_API_KEY ke file .env.")
    exit()

# Setup OpenAI
openai.api_key = OPENAI_API_KEY

# Mengatur intents (izin) yang dibutuhkan bot
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True  # Untuk menerima DM
bot = discord.Bot(intents=intents)

# Dictionary untuk menyimpan catatan pengguna (dalam implementasi nyata, gunakan database)
user_notes = {}

# Konteks tentang Livales
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

# Template response untuk DM
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

@bot.event
async def on_ready():
    """Fungsi yang dijalankan saat bot berhasil terhubung ke Discord."""
    print(f"Bot sudah online sebagai {bot.user}!")
    print("Bot siap menerima perintah.")
    
    # Mengatur status bot
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="Your Heart💓"
        )
    )
    
    # Update bot bio/description jika memungkinkan
    try:
        # Discord bot tidak bisa mengubah bio sendiri melalui API
        # Bio harus diubah manual di Discord Developer Portal
        print("📝 Bio Bot (Set manual di Discord Developer Portal):")
        print("🚀 Official Bot dari Livales | Connecting Hearts, Building Memories")
        print("🌐 Website: https://livales.netlify.app")
        print("💬 Gunakan /help untuk melihat semua perintah")
    except Exception as e:
        print(f"Info: {e}")

@bot.event
async def on_message(message):
    """Event handler untuk pesan masuk"""
    # Abaikan pesan dari bot sendiri
    if message.author == bot.user:
        return
    
    # Cek apakah pesan adalah DM ke bot
    if isinstance(message.channel, discord.DMChannel):
        # Buat embed untuk response yang lebih menarik
        embed = discord.Embed(
            title="🤖 Livales Bot - Pesan Otomatis",
            description=DM_TEMPLATE_RESPONSE.format(username=message.author.name),
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="📱 Aplikasi Livales",
            value="Coming Soon - All-in-one app untuk pasangan & sahabat",
            inline=False
        )
        
        embed.add_field(
            name="🔗 Link Penting",
            value="• [Website Resmi](https://livales.netlify.app/)\n• [Join Server Discord](https://discord.gg/Py2WaQSB)",
            inline=False
        )
        
        embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None)
        embed.set_footer(text="Livales - Startup teknologi untuk hubungan yang lebih bermakna")
        
        # Kirim embed sebagai balasan
        await message.channel.send(embed=embed)
        
        # Log DM untuk monitoring (opsional)
        print(f"📨 DM dari {message.author}: {message.content[:50]}...")

@bot.slash_command(name="halo", description="Bot akan menyapa balik!")
async def halo(ctx):
    """Perintah slash sederhana untuk menyapa pengguna."""
    embed = discord.Embed(
        title="👋 Halo!",
        description=f"Halo juga, {ctx.author.name}! Saya adalah Livales Bot, siap membantu Anda!",
        color=discord.Color.green()
    )
    embed.add_field(
        name="💡 Tips",
        value="Gunakan `/help` untuk melihat semua perintah yang tersedia!",
        inline=False
    )
    embed.set_footer(text="Livales Bot - Your Digital Companion")
    
    await ctx.respond(embed=embed)
    
@bot.slash_command(name="vale", description="Command terlarang!")
async def vale(ctx):
    """Perintah terlarang."""
    await ctx.respond(f"Halo sayanggkuuu, {ctx.author.name}! 😻")

@bot.slash_command(name="help", description="Lihat semua perintah yang tersedia")
async def help_command(ctx):
    """Menampilkan semua perintah yang tersedia."""
    embed = discord.Embed(
        title="📚 Panduan Penggunaan Livales Bot",
        description="Berikut adalah daftar perintah yang dapat Anda gunakan:",
        color=discord.Color.gold()
    )
    
    commands_list = [
        ("👋 `/halo`", "Sapa bot dan dapatkan sambutan hangat"),
        ("📝 `/take-note [catatan]`", "Simpan catatan pribadi Anda"),
        ("📖 `/my-notes`", "Lihat semua catatan yang tersimpan"),
        ("🗑️ `/clear-notes`", "Hapus semua catatan Anda"),
        ("❓ `/ask [pertanyaan]`", "Tanyakan apa saja tentang Livales"),
        ("🏢 `/about-livales`", "Informasi lengkap tentang perusahaan"),
        ("📚 `/help`", "Tampilkan menu bantuan ini"),
        ("🤫 `/vale`", "Sapa seseorang")
    ]
    
    for cmd, desc in commands_list:
        embed.add_field(name=cmd, value=desc, inline=False)
    
    embed.add_field(
        name="🌐 Website",
        value="[livales.netlify.app](https://livales.netlify.app/)",
        inline=True
    )
    
    embed.add_field(
        name="💬 Support",
        value="DM bot untuk bantuan otomatis",
        inline=True
    )
    
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text="Livales Bot v1.0 - Connecting Hearts, Building Memories")
    
    await ctx.respond(embed=embed)

@bot.slash_command(name="take-note", description="Simpan catatan pribadi Anda")
async def take_note(ctx, catatan: str):
    """Menyimpan catatan dari pengguna."""
    user_id = str(ctx.author.id)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Inisialisasi list catatan untuk user jika belum ada
    if user_id not in user_notes:
        user_notes[user_id] = []
    
    # Simpan catatan
    note_data = {
        "timestamp": timestamp,
        "note": catatan
    }
    user_notes[user_id].append(note_data)
    
    # Buat embed untuk response yang lebih menarik
    embed = discord.Embed(
        title="📝 Catatan Tersimpan!",
        description=f"Catatan Anda telah berhasil disimpan.",
        color=discord.Color.green()
    )
    embed.add_field(name="⏰ Waktu", value=timestamp, inline=False)
    embed.add_field(name="📄 Catatan", value=catatan[:1024], inline=False)
    embed.set_footer(text=f"Total catatan Anda: {len(user_notes[user_id])}")
    
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="my-notes", description="Lihat semua catatan Anda")
async def my_notes(ctx):
    """Menampilkan semua catatan pengguna."""
    user_id = str(ctx.author.id)
    
    if user_id not in user_notes or len(user_notes[user_id]) == 0:
        embed = discord.Embed(
            title="📭 Tidak Ada Catatan",
            description="Anda belum memiliki catatan tersimpan.",
            color=discord.Color.yellow()
        )
        embed.add_field(
            name="💡 Tips",
            value="Gunakan `/take-note [catatan]` untuk membuat catatan baru!",
            inline=False
        )
        await ctx.respond(embed=embed, ephemeral=True)
        return
    
    # Buat embed untuk menampilkan catatan
    embed = discord.Embed(
        title="📚 Catatan Anda",
        description=f"Total: {len(user_notes[user_id])} catatan tersimpan",
        color=discord.Color.blue()
    )
    
    # Tampilkan maksimal 5 catatan terakhir
    for note in user_notes[user_id][-5:]:
        embed.add_field(
            name=f"📅 {note['timestamp']}",
            value=note['note'][:256] + "..." if len(note['note']) > 256 else note['note'],
            inline=False
        )
    
    if len(user_notes[user_id]) > 5:
        embed.set_footer(text="📌 Menampilkan 5 catatan terakhir")
    
    await ctx.respond(embed=embed, ephemeral=True)

@bot.slash_command(name="ask", description="Tanyakan apa saja kepada Livales Bot")
async def ask(ctx, pertanyaan: str):
    """Menjawab pertanyaan menggunakan ChatGPT API."""
    # Defer response karena API call mungkin memakan waktu
    await ctx.defer()
    
    try:
        # Panggil OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": LIVALES_CONTEXT + "\nSelalu sertakan link website https://livales.netlify.app/ dalam jawaban jika relevan."},
                {"role": "user", "content": pertanyaan}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        answer = response.choices[0].message.content
        
        # Buat embed untuk response
        embed = discord.Embed(
            title="🤖 Livales Bot Menjawab",
            color=discord.Color.purple()
        )
        embed.add_field(name="❓ Pertanyaan", value=pertanyaan[:256], inline=False)
        embed.add_field(name="💬 Jawaban", value=answer[:1024], inline=False)
        
        # Tambahkan link website jika tidak ada dalam jawaban
        if "livales.netlify.app" not in answer.lower():
            embed.add_field(
                name="🌐 Info Lebih Lanjut",
                value="[Kunjungi Website Livales](https://livales.netlify.app/)",
                inline=False
            )
        
        embed.set_footer(text="Powered by OpenAI GPT-3.5 | Livales Bot")
        
        await ctx.followup.send(embed=embed)
        
    except Exception as e:
        error_embed = discord.Embed(
            title="❌ Error",
            description=f"Maaf, terjadi kesalahan saat memproses pertanyaan Anda.",
            color=discord.Color.red()
        )
        error_embed.add_field(
            name="💡 Saran",
            value="Coba lagi nanti atau hubungi admin server.",
            inline=False
        )
        error_embed.set_footer(text="Livales Bot")
        await ctx.followup.send(embed=error_embed, ephemeral=True)

@bot.slash_command(name="about-livales", description="Informasi tentang Livales")
async def about_livales(ctx):
    """Menampilkan informasi tentang Livales."""
    embed = discord.Embed(
        title="🚀 Tentang Livales",
        description="Startup teknologi yang membangun jembatan digital untuk hubungan manusia yang lebih bermakna",
        color=discord.Color.teal(),
        url="https://livales.netlify.app/"
    )
    
    embed.add_field(
        name="🎯 Misi Kami",
        value="Menciptakan ekosistem digital yang memperkaya dan memperdalam ikatan emosional antarmanusia",
        inline=False
    )
    
    embed.add_field(
        name="🎯 Bidang Usaha",
        value="• 🌱 Pertumbuhan Hubungan (Relationship Growth)\n• 📸 Kenangan Bersama (Shared Experiences)\n• 🎮 Hiburan Interaktif (Interactive Entertainment)",
        inline=False
    )
    
    embed.add_field(
        name="✨ Produk Unggulan",
        value="**Aplikasi Livales** - All-in-one app untuk pasangan dan sahabat",
        inline=False
    )
    
    embed.add_field(
        name="📱 Fitur yang Akan Hadir",
        value="• 📔 Shared Journals & Goals\n• 🖼️ Memory Timeline\n• ❓ Interactive Quizzes\n• 🎮 Fun Games for Two",
        inline=False
    )
    
    embed.add_field(
        name="🌐 Website Resmi",
        value="[livales.netlify.app](https://livales.netlify.app/)",
        inline=True
    )
    
    embed.add_field(
        name="📧 Kontak",
        value="livalesofficial@gmail.com",
        inline=True
    )
    
    # Set thumbnail jika bot memiliki avatar
    if bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    
    # Tambahkan image/banner jika ada
    embed.set_image(url="https://livales.netlify.app/banner.png")  # Ganti dengan URL image yang sesuai
    
    embed.set_footer(text="Livales - Connecting Hearts, Building Memories | Est. 2025")
    
    await ctx.respond(embed=embed)

@bot.slash_command(name="clear-notes", description="Hapus semua catatan Anda")
async def clear_notes(ctx):
    """Menghapus semua catatan pengguna."""
    user_id = str(ctx.author.id)
    
    if user_id in user_notes and len(user_notes[user_id]) > 0:
        count = len(user_notes[user_id])
        
        # Buat embed konfirmasi
        confirm_embed = discord.Embed(
            title="⚠️ Konfirmasi Penghapusan",
            description=f"Anda akan menghapus **{count} catatan**. Tindakan ini tidak dapat dibatalkan!",
            color=discord.Color.orange()
        )
        
        # Buat view dengan tombol konfirmasi
        class ConfirmView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=30)
                self.value = None
            
            @discord.ui.button(label="✅ Ya, Hapus", style=discord.ButtonStyle.danger)
            async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == ctx.author.id:
                    user_notes[user_id] = []
                    
                    success_embed = discord.Embed(
                        title="🗑️ Catatan Dihapus",
                        description=f"Berhasil menghapus {count} catatan.",
                        color=discord.Color.green()
                    )
                    await interaction.response.edit_message(embed=success_embed, view=None)
                    self.value = True
                    self.stop()
                else:
                    await interaction.response.send_message("Anda tidak dapat menggunakan tombol ini.", ephemeral=True)
            
            @discord.ui.button(label="❌ Batal", style=discord.ButtonStyle.secondary)
            async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
                if interaction.user.id == ctx.author.id:
                    cancel_embed = discord.Embed(
                        title="✅ Dibatalkan",
                        description="Penghapusan catatan dibatalkan.",
                        color=discord.Color.blue()
                    )
                    await interaction.response.edit_message(embed=cancel_embed, view=None)
                    self.value = False
                    self.stop()
                else:
                    await interaction.response.send_message("Anda tidak dapat menggunakan tombol ini.", ephemeral=True)
        
        view = ConfirmView()
        await ctx.respond(embed=confirm_embed, view=view, ephemeral=True)
        
    else:
        empty_embed = discord.Embed(
            title="📭 Tidak Ada Catatan",
            description="Anda tidak memiliki catatan untuk dihapus.",
            color=discord.Color.yellow()
        )
        await ctx.respond(embed=empty_embed, ephemeral=True)

@bot.slash_command(name="website", description="Dapatkan link website Livales")
async def website(ctx):
    """Menampilkan link website Livales dengan preview."""
    embed = discord.Embed(
        title="🌐 Website Resmi Livales",
        description="Kunjungi website kami untuk informasi lebih lengkap tentang produk dan layanan Livales!",
        color=discord.Color.blue(),
        url="https://livales.netlify.app/"
    )
    
    embed.add_field(
        name="🔗 Link Website",
        value="[https://livales.netlify.app/](https://livales.netlify.app/)",
        inline=False
    )
    
    embed.add_field(
        name="📱 Apa yang ada di website?",
        value="• Informasi lengkap tentang perusahaan\n• Preview aplikasi Livales\n• Blog dan artikel menarik\n• Kontak dan partnership",
        inline=False
    )
    
    embed.set_thumbnail(url=bot.user.avatar.url if bot.user.avatar else None)
    embed.set_footer(text="Livales - Your Digital Companion for Meaningful Relationships")
    
    await ctx.respond(embed=embed)

# Error handler untuk slash commands
@bot.event
async def on_application_command_error(ctx, error):
    """Handle error pada slash commands."""
    if isinstance(error, discord.errors.CheckFailure):
        await ctx.respond("❌ Anda tidak memiliki izin untuk menggunakan perintah ini.", ephemeral=True)
    else:
        error_embed = discord.Embed(
            title="❌ Terjadi Kesalahan",
            description="Maaf, terjadi kesalahan saat memproses perintah Anda.",
            color=discord.Color.red()
        )
        error_embed.add_field(
            name="Error",
            value=str(error)[:1024],
            inline=False
        )
        error_embed.set_footer(text="Hubungi admin jika masalah berlanjut")
        
        await ctx.respond(embed=error_embed, ephemeral=True)
        print(f"Error in command {ctx.command}: {error}")

# Menjalankan bot dengan token yang sudah dimuat
bot.run(DISCORD_TOKEN)