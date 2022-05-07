# Import Statements
from tracemalloc import start
from nextcord.ext import commands
from nextcord import Client
import datetime, asyncio

class PomodoroHandeler(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command(name='start', help='Starts Pomodoro Timer')
    async def start(self, ctx: commands.Context, study, pause):
        await starter(ctx, study, pause)

    @commands.command(name='time', help='Checks Time')
    async def time(self, ctx: commands.Context):
        timeLeft = round(seconds / 60, 2)
        await ctx.send(f'Time Left is --> {timeLeft} minute(s)')


# Cog Setup Function
def setup(bot):
    bot.add_cog(PomodoroHandeler(bot))

async def starter(ctx, study, pause):
    await ctx.send(f'Timer set for --> {study} minute(s)\nBreak set for --> {pause} minute(s)')

    global seconds, studySecs, breakSecs
    
    studySecs = 60 * int(study)
    breakSecs = 60 * int(pause)

    while studySecs > 0:
        seconds = studySecs
        if ((studySecs/60) % 10 == 0):
            await ctx.send(f'{studySecs/60} minutes left!')
        if (int(studySecs/60) == 5):
            await ctx.send(f'Five minutes left!')
        if (int(studySecs/60) == 1):
            await ctx.send(f'One minute left!')
        await asyncio.sleep(1)
        studySecs -= 1
    else:
        await ctx.send(f'Break Time!')
        while breakSecs > 0:
            seconds = studySecs
            if (int(studySecs/60) == 5):
                await ctx.send(f'Five minutes left!')
            if (int(studySecs/60) == 1):
                await ctx.send(f'One minute left!')
            await asyncio.sleep(1)
            breakSecs -= 1
    
    await ctx.send('Pomodoro Session Over!')