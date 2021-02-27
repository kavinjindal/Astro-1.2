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

class meta(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def guild(self, ctx):
        guild = discord.Embed(
                title = f'{ctx.guild} Info', 
                colour=discord.Colour.orange(),
                description = f'**Server Description :** {ctx.guild.description}'
            )
        guild.set_thumbnail(url=ctx.guild.icon_url)
        guild.add_field(name=':large_orange_diamond: **Owner**', value=f':small_blue_diamond: {ctx.guild.owner}', inline=False)
        guild.add_field(name=f':large_orange_diamond: ** Date Created :** ', value=datetime.datetime.strftime(ctx.guild.created_at, "%A %d %B %Y at %H:%M"))

        guild.add_field(name=':large_orange_diamond: **Member Count**', value=f':small_blue_diamond: {ctx.guild.member_count} members', inline=False)
        guild.add_field(name='**:large_orange_diamond: Server Region**', value=f':small_blue_diamond: {ctx.guild.region}', inline=False)
        guild.add_field(name=f':speech_balloon: **Text Channels**', value=f'{len(ctx.guild.text_channels)}', inline=False)
        guild.add_field(name=f':loud_sound: **Voice Channels**', value=f'{len(ctx.guild.voice_channels)}', inline=False)

        guild.set_image(url=ctx.guild.banner_url)
        #guild.add_field(name="**Members' Status**", value=
        #f':green_circle: **Online : **{statuses[discord.Status.online]:,}', inline=False)
        guild.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed = guild)

    @commands.command()
    async def prof(self, ctx, user:discord.Member = None):
        if user is None:
            user = ctx.author
        av = discord.Embed(title=f'User Profile of {user}', colour=discord.Colour.blue())
        av.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        av.add_field(name=f"User Name : ", value=f'{user}')
        av.add_field(name=f"User ID : ", value=f'{user.id}', inline=False)
        av.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=av)

    @commands.command()
    async def av(self, ctx, user:discord.Member = None):
        if user is None:
            user = ctx.author

        av = discord.Embed(title = f"{user}'s avatar", colour=discord.Colour.red())
        av.set_image(url = user.avatar_url)
        av.set_footer(text = f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        await ctx.send(embed = av)

    @commands.command()
    async def ping(self, ctx):
        ping = discord.Embed(title = 'This number is useless btw', description=f'**{round(self.client.latency * 1000)} ms**', colour=discord.Colour.red())
        await ctx.send(embed = ping)


def setup(client):
    client.add_cog(meta(client))
