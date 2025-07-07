def register_commands(bot):
    """Register semua commands ke bot"""
    from bot.commands.general import setup as setup_general
    from bot.commands.notes import setup as setup_notes
    from bot.commands.ai import setup as setup_ai
    from bot.commands.about import setup as setup_about
    
    setup_general(bot)
    setup_notes(bot)
    setup_ai(bot)
    setup_about(bot)