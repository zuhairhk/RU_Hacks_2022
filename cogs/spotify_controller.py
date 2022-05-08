# Import Statments
from nextcord.ext import commands
from nextcord import Client

class SpotifyController(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command(name='play', help='Plays Music')
    async def play(self):
        pass

# Cog Setup Function
def setup(bot):
    bot.add_cog(SpotifyController(bot))