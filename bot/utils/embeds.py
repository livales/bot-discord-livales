import discord
from bot.bot_instance import bot

# Lanjutan bot/utils/embeds.py
def create_embed(title="", description="", color=discord.Color.blue(), url=None):
    """Helper function untuk membuat embed dengan style konsisten"""
    embed = discord.Embed(
        title=title,
        description=description,
        color=color
    )
    
    if url:
        embed.url = url
    
    # Set thumbnail dengan avatar bot jika tersedia
    if bot.user and bot.user.avatar:
        embed.set_thumbnail(url=bot.user.avatar.url)
    
    # Set footer default
    embed.set_footer(text="Livales Bot - Your Digital Companion")
    
    return embed