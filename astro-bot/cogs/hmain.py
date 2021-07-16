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

class h(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.command()
    async def about(self, ctx):
    

        about = discord.Embed(
            title = 'Astro', 
            colour = discord.Colour.green()
        )
        about.set_author(name = f'{ctx.author}', icon_url=ctx.author.avatar_url)
        about.add_field(name = 'About', value='I am Astro, a bot made by <@!452737276812984330>, I have moderation commands, fun game commands, utility commands and also economy commands.', inline=False)
        #help.add_field(name = 'Commands', value='`a!cd for commands`', inline=False)
        about.add_field(name = 'Bot Prefix', value=f'a!', inline=False)
        about.add_field(name = 'Bot Version', value=f'v2.0', inline=False)
        about.add_field(name = 'Note', value=f'Make sure to give the bot admin permissions or else some of its features wont work', inline=False)

        about.set_footer(text = f'Astro v2', icon_url=self.client.user.avatar_url)
        
        about.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/800269388372508692/802434552063590420/Slide1.jpg')
        await ctx.message.add_reaction('✔️')
        await ctx.send(embed = about)

    
    
   

def setup(client):
    client.add_cog(h(client))
