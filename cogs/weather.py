from nextcord.ext import commands
import nextcord, os, requests

API_KEY = os.environ["API_KEY"] # Using OpenWeather API    
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def weather(ctx, *, city: str):

            city_name = city
            complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            channel = ctx.message.channel

            if x["cod"] != "404":

                    y = x["main"]
                    current_temperature = y["temp"]
                    current_temperature_celsiuis = str(round(current_temperature - 273.15))
                    current_pressure = y["pressure"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]

                    embed = nextcord.Embed(
                        title=f"Weather forecast - {city_name}",
                        color=0x7289DA,
                        timestamp=ctx.message.created_at,
                    )
                    embed.add_field(
                        name="Description",
                        value=f"**{weather_description}**",
                        inline=False)
                    embed.add_field(
                        name="Temperature(C)",
                        value=f"**{current_temperature_celsiuis}°C**",
                        inline=False)
                    embed.add_field(
                        name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
                    embed.add_field(
                        name="Atmospheric Pressure(hPa)",
                        value=f"**{current_pressure}hPa**",
                        inline=False)
                    embed.set_footer(text=f"Requested by {ctx.author.name}")

                    await channel.send(embed=embed)

            else:
                    await channel.send(
                        f"There was no results about this place!")

def setup(bot):
    bot.add_cog(Weather(bot))