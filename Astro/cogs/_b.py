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

class bot_b(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.command()
    async def update(self, ctx):
        update = discord.Embed(title = 'Updates for the bot', colour=discord.Colour.orange(), timestamp=datetime.utcnow())
        update.add_field(name = 'Recent additions in the bot', value=
        '--> Cooldowns on Economy command added'
        '\n' '--> Error handling updated'
        '\n' '--> Error logs added'
        '\n' '--> `a!work` command added'
        '\n' '--> `a!daily` command added'
        '\n' '--> `a!leaderboard` command added'
        '\n' '--> Help for all commands added'
        '\n' '--> Cooldowns updated'
        '\n' '--> Bot added on Top.GG')
        update.set_footer(text = 'Last Updated at : ')
        await ctx.send(embed = update)
        

    @commands.command()
    async def devop(self, ctx):
        devo = discord.Embed(
                title = 'Astro Developer', 
                colour = discord.Colour.green())
        devo.add_field(name='Developer Info', 
                value=':small_blue_diamond: Developed by     : Kavin Jindal <@!452737276812984330>  '
                '\n' 
                '\n'  ':small_blue_diamond: Github           : https://github.com/kavinjindal'
                '\n' 
                '\n'  ':small_blue_diamond: Email ID         : kavinsjindal@gmail.com'
                '\n' 
                '\n'  ':small_blue_diamond: Discord ID       : KJ#7320'
                '\n' 
                )
        await ctx.send(embed = devo)

    @commands.command()
    async def credits(self, ctx):
        credits = discord.Embed(
                title = 'Credits for Astro 999 Bot', 
                colour = discord.Colour.orange()
            )
        credits.add_field(name = 'Developer & Owner', value='<@!452737276812984330>')
        credits.add_field(name = 'Ideas & suggestions', value='<@!748881940425342996>')

        await ctx.send(embed = credits)

    @commands.command()
    async def add(self, ctx):
        add = discord.Embed(
                title = 'Add Astro to your server', 
                colour = discord.Colour.orange(), 
                url = 'https://discord.com/api/oauth2/authorize?client_id=795861753627672607&permissions=0&scope=bot'
            )
        await ctx.send(embed = add)

    @commands.command()
    async def info(self, ctx):
        info = discord.Embed(
                title = 'Astro Bot',
                #url = 'https://github.com/kavinjindal/Bruh-Bot',
                #description=[Add Bot to your server]('https://discord.com/api/oauth2/authorize?client_id=705634848584368178&permissions=0&scope=bot'),
                colour=discord.Colour.green())

        info.add_field(name='Development Info', 
                value=':small_orange_diamond: Developed In   : Python  '
                '\n' 
                '\n' f':small_orange_diamond: Python Version : {platform.python_version()}'
                '\n'
                '\n' f':small_orange_diamond: Discord.py     : {discord.__version__}'
                '\n' 
                '\n'  ':small_orange_diamond: App Version    : v1.2.0'
                '\n' 
                '\n'  ':small_orange_diamond: Hosted on      : Repl.it'
                '\n' 
                '\n'  ':small_orange_diamond: Open Source?   : No'
                '\n')
        await ctx.send(embed = info)

    @commands.command()
    async def stats(self, ctx):
        stats = discord.Embed(
            title = 'Stats for Astro 1.2', 
            colour = discord.Colour.blue()
        )
        stats.add_field(name = ':speech_balloon: Servers : ', value=f'{len(self.client.guilds)}', inline=False)
        stats.add_field(name = ':family: Users   : ', value=f'{len(self.client.guilds)}', inline=False)
        stats.add_field(name = ':regional_indicator_c: Commands   : ', value=f'{len(self.client.commands)}', inline=False)


        stats.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/800269388372508692/802434552063590420/Slide1.jpg')
        await ctx.send(embed = stats)

    @commands.command()
    async def github(self, ctx):
        github = discord.Embed(
            title = 'Astro 999 on Github', 
            url = 'https://github.com/kavinjindal/Astro-999', 
            colour = discord.Colour.blue()
        ) 
        github.add_field(name = 'Official Gituhb Repo', value='You can get the latest updates about the Bot on the official Repository.The bot has not been kept open source.')
        github.set_footer(text = 'Astro v1.2.0', icon_url='https://cdn.discordapp.com/attachments/800269388372508692/800357311679692800/invert.png')
        github.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/800269388372508692/800357324757794816/1_zm5NLjdhGd3VVTA2u-xEPg.gif')
        await ctx.send(embed = github)

    @commands.command()
    async def support(self, ctx):
        await ctx.send('Join the Official Support Server of Astro bot''\n\n''https://discord.gg/ryKpjTkVK2')

    @commands.command()
    async def vote(self, ctx):
        vote = discord.Embed(title = 'Vote Astro on..', colour=discord.Colour.teal())
        vote.add_field(name = '**Top.gg**', value='[Vote for Astro](https://top.gg/bot/795861753627672607)', inline=False)
        vote.set_thumbnail(url = self.client.user.avatar_url)
        await ctx.send(embed = vote)

def setup(client):
    client.add_cog(bot_b(client))
