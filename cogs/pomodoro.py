# Import Statements
from nextcord.ext import commands
import nextcord
from nextcord import Client
import asyncio


class PomodoroHandeler(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command(name='start', help='Starts Pomodoro Timer')
    async def start(self, ctx: commands.Context, study, pause):
        await starter(ctx, study, pause)

    @commands.command(name='time', help='Checks Time')
    async def time(self, ctx: commands.Context):
        timeLeft = round(seconds / 60, 2)
        embed=nextcord.Embed(title='Pomo Notification', description=f'Time Left is --> {timeLeft} minute(s)', color=0xFF5733)
        await ctx.send(embed=embed)


# Cog Setup Function
def setup(bot):
    bot.add_cog(PomodoroHandeler(bot))

# Starts Pomodoro Timer
async def starter(ctx, study, pause):
    embed=nextcord.Embed(title='Pomo Notification', description=f'Focus set for --> {study} minute(s)\nBreak set for --> {pause} minute(s)', color=0xFF5733)
    await ctx.send(embed=embed)

    global seconds, studySecs, breakSecs
    
    studySecs = 60 * int(study)
    breakSecs = 60 * int(pause)

    while studySecs > 0:
        seconds = studySecs
        if ((studySecs/60) % 10 == 0):
            embed=nextcord.Embed(title='Pomo Notification', description=f'{studySecs/60} minutes left!', color=0xFF5733)
            await ctx.send(embed=embed)
        if ((studySecs/60) == 5):
            embed=nextcord.Embed(title='Pomo Notification', description=f'Five minutes left!', color=0xFF5733)
            await ctx.send(embed=embed)
        if ((studySecs/60) == 1):
            embed=nextcord.Embed(title='Pomo Notification', description=f'One minute left!', color=0xFF5733)
            await ctx.send(embed=embed)
        await asyncio.sleep(1)
        studySecs -= 1
    else:
        embed=nextcord.Embed(title='Pomo Notification', description=f'Break Time!', color=0xFF5733)
        await ctx.send(embed=embed)
        while breakSecs > 0:
            seconds = studySecs
            if ((studySecs/60) == 5):
                embed=nextcord.Embed(title='Pomo Notification', description=f'Five minutes left!', color=0xFF5733)
                await ctx.send(embed=embed)
            if ((studySecs/60) == 1):
                embed=nextcord.Embed(title='Pomo Notification', description=f'One minute left!', color=0xFF5733)
                await ctx.send(embed=embed)
            await asyncio.sleep(1)
            breakSecs -= 1
    
    embed=nextcord.Embed(title='Pomo Notification', description='Pomodoro Session Over!', color=0xFF5733)
    await ctx.send(embed=embed)