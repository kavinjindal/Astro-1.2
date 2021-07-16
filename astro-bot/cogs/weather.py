import discord
from discord.ext import commands
from discord import DMChannel
import random
import time
import keep_alive
import webbrowser
import json
import os
from discord.utils import get
import praw
from discord.voice_client import VoiceClient
import time, datetime
from discord.ext.commands import Bot
from multiprocessing.connection import Client
from discord.ext.commands.cooldowns import BucketType
import platform
import asyncio
from datetime import datetime
import requests

class Weather(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def weather(self, ctx, *, city: str):

      api_key = 'eff13faf06cc6f21306fad08f4b4a3c0'
      base_url = "http://api.openweathermap.org/data/2.5/weather?"
      city_name = city
      complete_url = base_url + "appid=" + api_key + "&q=" + city
      response = requests.get(complete_url)
      x = response.json()
      channel = ctx.message.channel
      if x["cod"] != "404":
        async with channel.typing():
          y = x["main"]
          current_temperature = y["temp"]
          current_temperature_celsiuis = str(round(current_temperature - 273.15))
          current_pressure = y["pressure"]
          current_humidity = y["humidity"]
          z = x["weather"]
          weather_description = z[0]["description"]
          weather_description = z[0]["description"]
          embed = discord.Embed(title=f"Weather in {city_name}",
                            color=ctx.guild.me.top_role.color,
                            timestamp=ctx.message.created_at,)
          embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
          embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
          embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
          embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
          embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
          embed.set_footer(text=f"Requested by {ctx.author.name}")
          await ctx.send(embed=embed)
      else:
        await ctx.send("City not found, please enter a valid city.")

    

def setup(client):
    client.add_cog(Weather(client))
