import discord
import openai
from bot.config import DISCORD_TOKEN, OPENAI_API_KEY

# Setup OpenAI
openai.api_key = OPENAI_API_KEY

# Setup Discord Bot
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True

bot = discord.Bot(intents=intents)

def run():
    """Jalankan bot"""
    # Import dan register semua commands dan events
    from bot.commands import register_commands
    from bot.events import register_events
    
    register_commands(bot)
    register_events(bot)
    
    # Jalankan bot
    bot.run(DISCORD_TOKEN)