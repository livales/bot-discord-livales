def register_events(bot):
    """Register semua events ke bot"""
    from bot.events.ready import setup as setup_ready
    from bot.events.message import setup as setup_message
    
    setup_ready(bot)
    setup_message(bot)