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
def leadingZero(self, time: str):
    if len(time) > 1:
        return time

        return "0" + time
class Error_h(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(error)
                 
        elif isinstance(error, commands.CommandOnCooldown):
            #er = discord.Embed(title = error, colour = discord.Colour.red())
            print("Error cooldown")
            await ctx.reply(error)
            
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f'{error}')
            raise error
        elif isinstance(error, commands.NotOwner):
            await ctx.reply('Thats a Owner only command.. lol you cant use that')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply(error)
        elif isinstance(error, commands.CheckFailure):
            await ctx.reply(error)
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.reply(error)
            raise error
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.reply(error)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.reply(error)
        #elif isinstance(error, commands.CommandError):
        #    await ctx.send(error)
        elif isinstance(error, commands.UserNotFound):
            await ctx.reply(error)
        else:
            er_em = discord.Embed(title='An Error occurred!!', description='The error has been reported to the support server, write `a!support` to join the support server', colour=discord.Colour.red())
            er_em.add_field(name = 'Error', value=error, inline=False)
            c = self.client.get_channel(850643092231028736)
            invite = await ctx.channel.create_invite(max_uses = 5)
            #timestamp = datetime.datetime.now()
            await ctx.send(embed = er_em)
            #await c.send(embed = er)
            s_em = discord.Embed(title = f'An Error occurred in {ctx.guild} due to **{ctx.command}** command', description=f'{ctx.author} is the user.', colour = discord.Colour.red(), timestamp=datetime.utcnow())
            #s_em.add_field(name = 'TimeStamp', value=timestamp.strftime(r"%A %d %B %Y %I:%M %p"), inline=False)
            s_em.add_field(name = 'Invite of the server', value=invite, inline=False)
            s_em.add_field(name = 'User', value=f'{ctx.author}, {ctx.author.id}', inline=False)
            s_em.add_field(name = 'Server', value=f'{ctx.guild}, {ctx.guild.id}', inline=False)
            s_em.add_field(name = 'Command', value=f'{ctx.command}',inline=False)
            s_em.add_field(name = 'Error', value=error)
            await c.send(embed=s_em)

def setup(client):
    client.add_cog(Error_h(client))
