from nextcord.ext import commands
from nextcord import Client

class PomodoroHandeler(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

# Cog Setup Function
def setup(bot):
    bot.add_cog(PomodoroHandeler(bot))