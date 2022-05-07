from nextcord.ext import commands
from nextcord import Client
import datetime, asyncio

class PomodoroHandeler(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot
    
    timerState = False

    @commands.command(name='start', help='Starts Pomodoro Timer')
    async def start(self, ctx: commands.Context, study, pause):
        if timerState == False:
            timerState = True
            await ctx.send(f'Timer set for --> {study}\nBreak set for -> {pause}')

            studySecs = 60 * int(study)
            breakSecs = 60 * int(pause)

            while studySecs > 0:
                timer = datetime.timedelta(seconds = studySecs)
                await asyncio.sleep(1)
                studySecs -= 1
            
            await ctx.send('Timer Over')
        else:
            await ctx.send(f'Timer already running!')

# Cog Setup Function
def setup(bot):
    bot.add_cog(PomodoroHandeler(bot))