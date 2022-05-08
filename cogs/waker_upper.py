# Import Statments
from nextcord.ext import commands
from nextcord import Client
import NextcordUtils
import asyncio
import eye_detection
from cogs.light_controller import lightMode

class WakerUpper(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command(name='join', help='Joins Users Voice Channel')
    async def join(self, ctx):
        voicetrue = ctx.author.voice
        if voicetrue is None:
            return await ctx.send('Cannot join unless you are in a vc :pensive:')
        await ctx.author.voice.channel.connect()
        await ctx.send('Joined vc :tired_face:')

    @commands.command(name='leave', help='Leaves Voice Channel')
    async def leave(self, ctx):
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        if voicetrue is None:
            return await ctx.send('Gaymer cannot join unless you are in a vc :pensive:')
        if mevoicetrue is None:
            return await ctx.send('I am currently not in a vc :cry:')
        await ctx.voice_client.disconnect()
        await ctx.send('Left vc :smirk_cat:')

    @commands.command(name='alert', help='Activates Wake Up Scenario')
    async def alert(self, ctx):
        state = eye_detection.main()
        if state == True:
            lightMode('scene')
            await alerter(ctx)
        else:
            pass
    

# Cog Setup Function
def setup(bot):
    bot.add_cog(WakerUpper(bot))

@commands.command()
async def alerter(ctx):
    music = NextcordUtils.Music()

    await ctx.send('https://tenor.com/view/wakeup-gif-19924898')
    
    voicetrue = ctx.author.voice
    if voicetrue is None:
        return await ctx.send('Cannot join unless you are in a vc :pensive:')
    await ctx.author.voice.channel.connect()

    url = 'https://www.youtube.com/watch?v=W3AeO32y28s&ab_channel=memesbycowbelly'
    player = music.get_player(guild_id = ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        for i in range(10):
            await player.queue(url, search=True)
            await player.play()
            await asyncio.sleep(12)