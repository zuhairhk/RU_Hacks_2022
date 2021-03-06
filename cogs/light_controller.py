# Import Statments
from nextcord.ext import commands
from nextcord import Client
from tuya_connector import TuyaOpenAPI
import os

# env variables
ACCESS_ID = os.environ['ACCESS_ID']
ACCESS_KEY = os.environ['ACCESS_KEY']
API_ENDPOINT = os.environ['API_ENDPOINT']
LIGHTBULB_DEVICE_ID = os.environ['LIGHTBULB_DEVICE_ID']

# CONNECTION
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()


class LightController(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command(name='light_state', help='Changes state of bulb (On/Off)')
    async def light_state(self, ctx, mode):
        state(mode=mode)
    
    @commands.command(name='set_colour', help='Sets Colour: Red, Orange, Yellow, Green, Cyan, Blue, Pink')
    async def set_colour(self, ctx, colour):
        colourSet(colour=colour)
    
    @commands.command(name='set_mode', help='Sets mode: White, Colour, Scene, Music')
    async def set_mode(self, ctx, mode):
        colourSet(mode=mode)

# Cog Setup Function
def setup(bot):
    bot.add_cog(LightController(bot))

# State of Light Function
def state(mode):
        if mode.lower() == 'on':
            state = True
        elif mode.lower() == 'off':
            state = False
        commands = {'commands': [{'code': 'switch_led', 'value': state}]}
        openapi.post(f'/v1.0/iot-03/devices/{LIGHTBULB_DEVICE_ID}/commands', commands)

# Colour Set Function
def colourSet(colour):
    colors = {
            'red' : 0,
            'orange' : 30,
            'yellow' : 45,
            'green' : 120,
            'cyan' : 180,
            'blue' : 245,
            'pink' : 300
        }
    commands = {'commands': [{ 'code': 'colour_data_v2', 'value': {'h': colors[colour], 's': 1000, 'v': 1000} }]}
    openapi.post(f'/v1.0/iot-03/devices/{LIGHTBULB_DEVICE_ID}/commands', commands)

# Light Mode Set Function
def lightMode(mode):
    commands = {'commands': [{'code': 'work_mode', 'value': mode}] }
    openapi.post(f'/v1.0/iot-03/devices/{LIGHTBULB_DEVICE_ID}/commands', commands)
