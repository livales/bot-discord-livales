import discord

def setup(bot):
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
                name="Your Heart 💓"
            )
        )
        
        # Info tentang bio bot
        print("📝 Bio Bot (Set manual di Discord Developer Portal):")
        print("🚀 Official Bot dari Livales | Connecting Hearts, Building Memories")
        print("🌐 Website: https://livales.netlify.app")
        print("💬 Gunakan /help untuk melihat semua perintah")