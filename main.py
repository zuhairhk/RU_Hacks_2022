# Import Statements
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
from nextcord import Intents

from tuya_connector import TuyaOpenAPI
# env variables
ACCESS_ID = 'uuphqcm9b7tercbdvdr5'
ACCESS_KEY = '894148e6d6ba4d05905a978c9d422b19'
API_ENDPOINT = 'https://openapi-ueaz.tuyaus.com'
LIGHTBULB_DEVICE_ID = '10063573bcddc2a1c466'
# CONNECTION
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    print('Ready!')

if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    
    bot.run(TOKEN)