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

reddit = praw.Reddit(client_id = "3q63UFvTo37o7g", 
                    client_secret = 'zdMd1AFE1gZXlUNA4gaoO71mrRLUYA', 
                    username = 'Freezee17',
                    password = 'kjsupremo', 
                    user_agent = 'memepraw')
class meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
        subreddit = reddit.subreddit('memes')
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        mem = discord.Embed(title = 'r/memes',description=name, colour = discord.Colour.teal())
        mem.set_image(url = url)
        await ctx.send(embed = mem)

    @commands.command()
    async def ph(self, ctx):
        subreddit = reddit.subreddit('ProgrammerHumor')
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        mem = discord.Embed(title = 'r/ProgrammerHumor',description=name, colour = discord.Colour.teal())
        mem.set_image(url = url)
        await ctx.send(embed = mem)

    #wholesomememes
    @commands.command()
    async def whm(self, ctx):
        subreddit = reddit.subreddit('wholesomememes')
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        mem = discord.Embed(title = 'r/wholesomememes',description=name, colour = discord.Colour.teal())
        mem.set_image(url = url)
        await ctx.send(embed = mem)

    @commands.command()
    async def dank(self, ctx):
        subreddit = reddit.subreddit('dankmemes')
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        mem = discord.Embed(title = 'r/dankmemes',description=name, colour = discord.Colour.teal())
        mem.set_image(url = url)
        await ctx.send(embed = mem)

    @commands.command()
    async def pewds(self, ctx):
        subreddit = reddit.subreddit('PewdiepieSubmissions')
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        mem = discord.Embed(title = 'r/PewdiepieSubmissions',description=name, colour = discord.Colour.teal())
        mem.set_image(url = url)
        await ctx.send(embed = mem)

    @commands.command()
    async def fb(self, ctx):
        subreddit = reddit.subreddit('terriblefacebookmemes')
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        mem = discord.Embed(title = 'r/terriblefacebookmemes',description=name, colour = discord.Colour.teal())
        mem.set_image(url = url)
        await ctx.send(embed = mem)

    @commands.command()
    async def animal(self, ctx):
        subreddit = reddit.subreddit('AdviceAnimals')
        all_subs = []

        top = subreddit.top(limit = 50)

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        mem = discord.Embed(title = 'r/AdviceAnimals',description=name, colour = discord.Colour.teal())
        mem.set_image(url = url)
        await ctx.send(embed = mem)

    

def setup(client):
    client.add_cog(meme(client))
