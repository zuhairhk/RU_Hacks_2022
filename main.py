# Import Statements
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
from nextcord import Intents

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
bot = commands.Bot(command_prefix = "$") #, intents = intents)

@bot.event
async def on_ready():
    print('Ready!')

if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    
    bot.run(TOKEN)