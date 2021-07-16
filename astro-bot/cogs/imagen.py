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
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from datetime import datetime

class imagen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def wanted(self, ctx, user : discord.Member = None):
      if user is None:
        user = ctx.author

      wanted = Image.open("wantedimg.jpg")
      asset = user.avatar_url_as(size = 128)
      data = BytesIO(await asset.read())
      pfp = Image.open(data)
      pfp = pfp.resize((180, 180))

      wanted.paste(pfp, (228, 309))

      wanted.save("profile.jpg")

      await ctx.send(file = discord.File("profile.jpg"))

    @commands.command()
    async def tweet(self, ctx, *,text = 'Enter some text dork'):
      img = Image.open('ttow.png')
      draw = ImageDraw.Draw(img)
      font = ImageFont.truetype('arial.ttf', 80)
      font1 = ImageFont.truetype('arial.ttf', 30)
      userid = f'@{ctx.author.name}'
      draw.text((180, 21), userid, (255,255,255), font=font)
      draw.text((180, 120), userid, (128,128,128), font=font1)
      img.save('text.png')
      await ctx.send(file = discord.File("text.png"))

    

    
def setup(client):
    client.add_cog(imagen(client))
