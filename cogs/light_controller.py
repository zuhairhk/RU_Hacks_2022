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

    @commands.command()
    async def light_state(self, ctx, mode):
        if mode.lower() == 'on':
            state = True
        elif mode.lower() == 'off':
            state = False
        commands = {'commands': [{'code': 'switch_led', 'value': state}]}
        openapi.post(f'/v1.0/iot-03/devices/{LIGHTBULB_DEVICE_ID}/commands', commands)
        await ctx.send(f'Light is now {mode}')
    
    @commands.command()
    async def set_colour(self, ctx, colour):
        commands = {'commands': [{ 'code': 'colour_data_v2', 'value': {'h': colour, 's': 1000, 'v': 1000} }]}
        openapi.post(f'/v1.0/iot-03/devices/{LIGHTBULB_DEVICE_ID}/commands', commands)
        await ctx.send(f'Light changed to {colour}')

def setup(bot):
    bot.add_cog(LightController(bot))