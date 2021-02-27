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

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
        await self.client.change_presence(status = discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='Astro Beta Testing TV' + '|| a!help'))
        c = self.client.get_channel(803142341938118688)
        start = discord.Embed(title = 'Logged In....', colour=discord.Colour.red(),timestamp=datetime.utcnow()
)
        start.add_field(name = self.client.user.name, value=self.client.user.id)
        start.set_thumbnail(url=self.client.user.avatar_url)
        #start.set_footer(text=timestamp)
        await c.send(embed=start)

    @commands.command()
    async def test(self, ctx):
        await ctx.send('a!bag')

    

def setup(client):
    client.add_cog(Start(client))
