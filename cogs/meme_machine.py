import nextcord
from nextcord.ext import commands

class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user: # Prevents bot from replying to itself
            return
        
        if ("big shoe") in message.content: # big shoe lmfao
            await message.channel.send("https://tenor.com/bC1Ll.gif")
        
def setup(bot):
    bot.add_cog(Meme(bot))