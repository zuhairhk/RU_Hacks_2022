import nextcord, json, random
from nextcord.ext import commands

links = json.load(open("memes.json"))

class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user: # Prevents bot from replying to itself
            return
        
        if ("big shoe") in (message.content).lower(): # big shoe lmfao
            await message.channel.send("https://tenor.com/bC1Ll.gif")
        
        elif ("meme") in (message.content).lower(): # Sends random meme from list in .json file
            await message.channel.send(random.choice(links["memes"]))
        
def setup(bot):
    bot.add_cog(Meme(bot))