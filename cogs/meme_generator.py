# Import Statments
from cgitb import text
from email.mime import image
import nextcord
from nextcord.ext import commands
from nextcord import Client
from PIL import Image, ImageDraw, ImageFont
import textwrap


class MemeGenerator(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command(name='create', help='Creates Custom Server Memes')
    async def create(self, ctx, image, topText, botText):
        await memeGen(ctx, image=image, topText=topText, botText=botText)



# Cog Setup Function
def setup(bot):
    bot.add_cog(MemeGenerator(bot))

async def memeGen(ctx, image, topText, botText):
    # Load Image
    img = Image.open('./assets/images/' + image + '.jpeg')
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Load Font
    fontSize = 9
    font = ImageFont.truetype(font='./assets/impact.ttf', size=int(height * fontSize) // 75)

    # Text Wrapping
    topText = topText.upper()
    botText = botText.upper()
    
    charWidth, charHeight = font.getsize('A')
    charsPerLine = width // charWidth

    topLines = textwrap.wrap(topText, width=charsPerLine)
    botLines = textwrap.wrap(botText, width=charsPerLine)

    # Drawing Lines
    y = 10
    for line in topLines:
        lineWidth, lineHeight = font.getsize(line)
        x = (width - lineWidth) / 2
        draw.text((x,y), line, fill='white', font=font)
        y += lineHeight

    y = height - charHeight * len(botLines) - 15
    for line in botLines:
        lineWidth, lineHeight = font.getsize(line)
        x = (width - lineWidth) / 2
        draw.text((x,y), line, fill='white', font=font)
        y += lineHeight

    # Send Image
    img.save('test.jpg')
    await ctx.send(file=nextcord.File(r'test.jpg'))