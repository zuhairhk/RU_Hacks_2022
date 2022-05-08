# Import Statements
import os
import nextcord
from nextcord.ext import commands
from nextcord import Intents, Interaction
from cogs import light_controller, search_func

#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot Invite Link: https://discord.com/api/oauth2/authorize?client_id=972281781564887052&permissions=8&scope=bot%20applications.commands

intents = Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

# On Ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="$help"))
    print('Ready!')

# Light On/Off Slash Command
@bot.slash_command(
    name="light",
    description="State of Bulb (On/Off)",
    guild_ids=[852057773478641664, 793978686822154240, 972607047084429322]
)
async def State(interaction: Interaction, mode):
    light_controller.state(mode=mode)
    await interaction.response.send_message(f"Light State Set To --> {mode}")

# Light Colour Change Slash Command
@bot.slash_command(
    name= "colour_set",
    description = "Red, Orange, Yellow, Green, Cyan, Blue, Pink",
    guild_ids=[852057773478641664, 793978686822154240, 972607047084429322]
)
async def colour_set(interaction: Interaction, colour):
    light_controller.colourSet(colour=colour)
    await interaction.response.send_message(f"Light State Set To --> {colour}")

# Light Mode Change Slash Command
@bot.slash_command(
    name= "mode",
    description = "White, Colour, Scene, Music",
    guild_ids=[852057773478641664, 793978686822154240, 972607047084429322]
)
async def mode(interaction: Interaction, mode):
    light_controller.lightMode(mode=mode)
    await interaction.response.send_message(f"Light State Set To --> {mode}")

# Google Search Slash Command
@bot.slash_command(
    name= "search",
    description = "Enter Query",
    guild_ids=[852057773478641664, 793978686822154240, 972607047084429322]
)
async def search(interaction: Interaction, query):
    response = search_func.searcher(query=query)
    await interaction.response.send_message(f"Google Response --> {response}")

# Driver Code
if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
    
    bot.run(TOKEN)