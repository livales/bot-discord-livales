import discord
from bot.config import DM_TEMPLATE_RESPONSE, WEBSITE_URL
from bot.utils.embeds import create_embed

def setup(bot):
    @bot.event
    async def on_message(message):
        """Event handler untuk pesan masuk"""
        # Abaikan pesan dari bot sendiri
        if message.author == bot.user:
            return
        
        # Cek apakah pesan adalah DM ke bot
        if isinstance(message.channel, discord.DMChannel):
            # Buat embed untuk response yang lebih menarik
            embed = create_embed(
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
                value=f"• [Website Resmi]({WEBSITE_URL})\n• [Join Server Discord](https://discord.gg/your-invite-link)",
                inline=False
            )
            
            embed.set_footer(text="Livales - Startup teknologi untuk hubungan yang lebih bermakna")
            
            # Kirim embed sebagai balasan
            await message.channel.send(embed=embed)
            
            # Log DM untuk monitoring (opsional)
            print(f"📨 DM dari {message.author}: {message.content[:50]}...")
    
    @bot.event
    async def on_application_command_error(ctx, error):
        """Handle error pada slash commands."""
        if isinstance(error, discord.errors.CheckFailure):
            await ctx.respond("❌ Anda tidak memiliki izin untuk menggunakan perintah ini.", ephemeral=True)
        else:
            error_embed = create_embed(
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