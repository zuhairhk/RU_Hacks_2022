# Import Statements
import requests
import urllib
from requests_html import HTML, HTMLSession
from nextcord.ext import commands
from nextcord import Client

class GoogleScraper(commands.Cog):
    
    def __init__(self, bot : Client):
        self.bot = bot

    @commands.command(name='ask', help='Ask any question! (Use slash command `/search`)')
    async def ask(self, ctx, query):
        response = searcher(query=query)
        await ctx.send(f'Google Response --> {response}')

# Cog Setup Function
def setup(bot):
    bot.add_cog(GoogleScraper(bot))

# Function that gets source for searching
def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)

# Function that scrapes google for results
def scrape_google(query):
    #query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    links = list(response.html.absolute_links)
    return links

# Driver Function
def searcher(query):
    results = scrape_google(query=query)
    primaryResult = results[0]
    return primaryResult