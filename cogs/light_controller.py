from nextcord.ext import commands
from nextcord import Client

class LightController(commands.Cog):
    def __init__(self, bot : Client):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send("testy testets")


def setup(bot):
    bot.add_cog(LightController(bot))