from nextcord.ext import commands
from nextcord import Client

class GoogleScraper(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

# Cog Setup Function
def setup(bot):
    bot.add_cog(GoogleScraper(bot))