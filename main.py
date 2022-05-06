# Import Statements
import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands
from nextcord import Intents

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)