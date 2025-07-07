import discord
from bot.config import WEBSITE_URL
from bot.utils.embeds import create_embed

def setup(bot):
    @bot.slash_command(name="about-livales", description="Informasi tentang Livales")
    async def about_livales(ctx):
        """Menampilkan informasi tentang Livales."""
        embed = create_embed(
            title="🚀 Tentang Livales",
            description="Startup teknologi yang membangun jembatan digital untuk hubungan manusia yang lebih bermakna",
            color=discord.Color.teal(),
            url=WEBSITE_URL
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
            value=f"[livales.netlify.app]({WEBSITE_URL})",
            inline=True
        )
        
        embed.add_field(
            name="📧 Kontak",
            value="livalesofficial@gmail.com",
            inline=True
        )
        
        # Tambahkan image/banner jika ada
        embed.set_image(url=f"{WEBSITE_URL}banner.png")  # Ganti dengan URL image yang sesuai
        
        embed.set_footer(text="Livales - Connecting Hearts, Building Memories | Est. 2024")
        
        await ctx.respond(embed=embed)