'''
Slash command to get current weather
Argument could be degrees C or F
'''

from nextcord.ext import commands
from nextcord import Client

temp = 32

class Weather(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command()
    async def temp(self, ctx: commands.Context):
        await ctx.send(f"Temp is {temp} degrees Celsius")

def setup(bot):
    bot.add_cog(Weather(bot))