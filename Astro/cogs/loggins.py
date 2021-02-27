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

class Loggings(commands.Cog):
    def __init__(self, client):
        self.client = client

   
    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def calldevs(self, ctx,*,reason):
        calldevs = discord.Embed(title = 'Your message has been sent', colour=discord.Color.green())
        await ctx.send(embed = calldevs)
        invite = await ctx.channel.create_invite(max_uses = 100)
        channel = self.client.get_channel(804196087615062036)
        embed = discord.Embed(title = 'A user messaged you something', colour=discord.Colour.teal(), timestamp=datetime.utcnow())
        embed.add_field(name = 'Guild', value=f'Guild : {ctx.guild}''\n'f'Guild Id : {ctx.guild.id}''\n'f'{invite}', inline=False)
        embed.add_field(name = 'User', value=f'User {ctx.message.author}''\n'f'User ID : {ctx.author.id}', inline=False)
        embed.add_field(name = 'Text by the user', value=f'{reason}', inline=False)
        embed.set_footer(text='Astro Devs DM System')
        await channel.send(embed = embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setup_logs(self, ctx, text_channel):
        await ctx.send('Hey b** sup')
        





def setup(client):
    client.add_cog(Loggings(client))
