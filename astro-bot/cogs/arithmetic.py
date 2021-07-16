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

class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def sqr(self, ctx, number):
      no = int(number)
      answer = no * no
      await ctx.send(f'Square of {no} is' '\n' '===========' '\n' f'`{answer}`')

    @commands.command()
    async def cube(self, ctx, number):
      no = int(number)
      answer = no * no * no
      await ctx.send(f'Cube of {no} is' '\n' '===========' '\n' f'`{answer}`')

    @sqr.error
    async def sqrt_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Write a valid number for squaring it. ')

    @commands.command()
    async def addit(self, ctx, dig, *,digsec):
      no1 = int(dig)
      no2 = int(digsec)
      ans = no1 + no2
      answer = discord.Embed(
        title = 'Addition', 
        colour = discord.Colour.red()
      )
      answer.add_field(name = f'{dig} + {digsec}', value=f'{ans}')
      answer.set_footer(text='This command is under development')
      await ctx.send(embed = answer)
    
    @commands.command()
    async def subit(self, ctx, dig, *,digsec):
      no1 = int(dig)
      no2 = int(digsec)
      ans = no1 - no2
      answer = discord.Embed(
        title = 'Subtraction', 
        colour = discord.Colour.red()
      )
      answer.add_field(name = f'{dig} - {digsec}', value=f'{ans}')
      answer.set_footer(text='This command is under development')
      await ctx.send(embed = answer)

    

    

def setup(client):
    client.add_cog(Math(client))
