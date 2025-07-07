import discord
from bot.utils.embeds import create_embed
from bot.config import WEBSITE_URL

def setup(bot):
    @bot.slash_command(name="halo", description="Bot akan menyapa balik!")
    async def halo(ctx):
        """Perintah slash sederhana untuk menyapa pengguna."""
        embed = create_embed(
            title="👋 Halo!",
            description=f"Halo juga, {ctx.author.name}! Saya adalah Livales Bot, siap membantu Anda!",
            color=discord.Color.green()
        )
        embed.add_field(
            name="💡 Tips",
            value="Gunakan `/help` untuk melihat semua perintah yang tersedia!",
            inline=False
        )
        
        await ctx.respond(embed=embed)
        
    @bot.slash_command(name="vale", description="Command terlarang!")
    async def vale(ctx):
        """Perintah terlarang."""
        await ctx.respond(f"Halo sayanggkuuu, {ctx.author.name}! 😻")

    @bot.slash_command(name="help", description="Lihat semua perintah yang tersedia")
    async def help_command(ctx):
        """Menampilkan semua perintah yang tersedia."""
        embed = create_embed(
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
            ("🌐 `/website`", "Dapatkan link website Livales")
            ("🤫 `/vale`", "Sapa seseorang")
        ]
        
        for cmd, desc in commands_list:
            embed.add_field(name=cmd, value=desc, inline=False)
        
        embed.add_field(
            name="🌐 Website",
            value=f"[livales.netlify.app]({WEBSITE_URL})",
            inline=True
        )
        
        embed.add_field(
            name="💬 Support",
            value="DM bot untuk bantuan otomatis",
            inline=True
        )
        
        await ctx.respond(embed=embed)

    @bot.slash_command(name="website", description="Dapatkan link website Livales")
    async def website(ctx):
        """Menampilkan link website Livales dengan preview."""
        embed = create_embed(
            title="🌐 Website Resmi Livales",
            description="Kunjungi website kami untuk informasi lebih lengkap tentang produk dan layanan Livales!",
            color=discord.Color.blue(),
            url=WEBSITE_URL
        )
        
        embed.add_field(
            name="🔗 Link Website",
            value=f"[{WEBSITE_URL}]({WEBSITE_URL})",
            inline=False
        )
        
        embed.add_field(
            name="📱 Apa yang ada di website?",
            value="• Informasi lengkap tentang perusahaan\n• Preview aplikasi Livales\n• Blog dan artikel menarik\n• Kontak dan partnership",
            inline=False
        )
        
        await ctx.respond(embed=embed)