import discord
from discord.ext import commands
from discord import DMChannel
from discord import Intents
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
 # https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client
        intents = Intents.all()

    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
        await self.client.change_presence(status = discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='The Chainsmokers|| a!'))
        c = self.client.get_channel(848434199022927892)
        start = discord.Embed(title = 'Logged In....', colour=discord.Colour.red(),timestamp=datetime.utcnow()
)
        start.add_field(name = self.client.user.name, value=self.client.user.id)
        start.set_thumbnail(url=self.client.user.avatar_url)
        #start.set_footer(text=timestamp)
        await c.send(embed=start)

    @commands.Cog.listener()
    async def on_member_join(self, member):
      for channel in member.guild.channels:
        if str(channel) == "welcome":
          embed = discord.Embed(color=0x4a3d9a)
          embed.add_field(name="Welcome", value=f"{member.name} has joined {member.guild.name}", inline=False)
          embed.set_image(url="https://newgitlab.elaztek.com/NewHorizon-Development/discord-bots/Leha/-/raw/master/res/welcome.gif")
          await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
      for channel in member.guild.channels:
        if str(channel) == "goodbye":
          embed = discord.Embed(color=0x4a3d9a)
          embed.add_field(name="Goodbye", value=f"{member.name} has left {member.guild.name}", inline=False)
          embed.set_image(url="https://newgitlab.elaztek.com/NewHorizon-Development/discord-bots/Leha/-/raw/master/res/welcome.gif")
          await channel.send(embed=embed)

    @commands.command()
    async def test(self, ctx):
        await ctx.send('a!bag')

    @commands.is_owner()
    @commands.command()
    async def sms(self, ctx, *, message):
      c = self.client.get_channel(846257107337478164)
      await c.send(message)

    @commands.is_owner()
    @commands.command()
    async def rule(self, ctx):
      embed = discord.Embed(
      title = 'Rules for Server '
    ,description = '----' 
    , colour = discord.Colour.teal())

      embed.add_field(
          name = 'All rules should be followed while on the server.'
          , value='''1) Follow the Discord Terms of Service and Community Guidelines \n 
      2) Don't be a jerk \n Do not spam, pinging people without any reason, disrespecting the members or carrying out raids on the server. You will be warned in the beginning and will be banned immediately. \n 
      3) Rules Regarding Promotion: \n The #promotion channel has been setup for self-promotion. IF any kind of DM promotion or doing self promotion in any other channels is noticed, you will be given a server mute and won't be able to access the server for a given period of time. \n 
      4) NSFW Content is prohibited \n Nothing that comes under **NSFW** category will be accepted on the server INCLUDING NSFW memes and jokes. You will be warned once and will be banned permanently if you do this again. \n 
      5) No religious, political or depressive discussion \n No discussion like the ones mentioned will be tolerated. \n 
      ''')
      embed.add_field(
        name = '---------', 
      value= '''
      6) Privacy \n Do not share any private information or images without anyone's consent or do not ask or give any private info to anyone. \n 
      7) Contact Admin: \n If you feel anything wrong is going on in the server contact the admin using `a!sms [your message]` to send your message to the admin, you will be replied within the next 24 hours. \n ''', inline=False)
        

      

      embed.add_field(name = '--------------------', value='If you feel any of the rules mentioned are being overstepped, then feel free to ping the admin <@452737276812984330> or dm your problem with relevant evidence.', inline=False)
      await ctx.send(embed = embed)

    
      

    

def setup(client):
    client.add_cog(Start(client))
