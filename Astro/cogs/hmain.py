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
    async def cmd(self, ctx):
        cd = discord.Embed(
        title = 'Commands for Astro 1.2', 
        colour = discord.Colour.blue())
        cd.add_field(name = 'Prefix', value='a!')
        cd.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/800269388372508692/802434552063590420/Slide1.jpg')
        cd.set_footer(text = f'Write `a!help [command_name] to know more about the command`')
        cd.add_field(name = 'Mod commands', value='`ban [@user] [reason], unban [@user], kick [@user] [reason], clear [amount] `', inline=False)
        cd.add_field(name = 'Fun Commands', value='`kill [@user], slap [@user], roast [@user], pw, dice, toss, fsociety, bruh`', inline=False)
        cd.add_field(name = 'Memer', value='`ph, meme, whm, dank, pewds, fb, animal`')
        cd.add_field(name = 'Dev commands', value='`[Only available for owner] - send, rule, create, `', inline=False)
        cd.add_field(name = 'Bot info', value='`stats, info, add, github, support, devop, credits, update, vote, calldevs [yourtext]`', inline=False)
        #cd.add_field(name = 'Dev info', value='`devop, credits`', inline=False)
        cd.add_field(name = 'Meta Commands', value='`guild, av, ping`')
        cd.add_field(name = 'Economy Commands', value='`bal, shop, bag, buy [item_name] [amount], give [@user] [amount from bank], withd [amount], dep [amount], sell [item_name] [amount], beg, work, daily, lb, bank, wallet`', inline=False)
        cd.add_field(name = 'Coder Commands', value='`coder, py, bpy`', inline=False)
        await ctx.send(embed = cd)

    @commands.command()
    async def about(self, ctx):
    

        about = discord.Embed(
            title = 'Astro 999 v1.1', 
            colour = discord.Colour.green()
        )
        about.set_author(name = f'{ctx.author}', icon_url=ctx.author.avatar_url)
        about.add_field(name = 'About', value='I am Astro 999 a bot made by <@!452737276812984330>, I have moderation commands, fun game commands, utility commands and also economy commands.', inline=False)
        #help.add_field(name = 'Commands', value='`a!cd for commands`', inline=False)
        about.add_field(name = 'Bot Prefix', value=f'a!', inline=False)
        about.add_field(name = 'Bot Version', value=f'v1.2', inline=False)
        about.add_field(name = 'Note', value=f'Make sure to give the bot admin permissions or else some of its features wont work', inline=False)

        about.set_footer(text = f'Astro v1.2', icon_url=self.client.user.avatar_url)
        
        about.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/800269388372508692/802434552063590420/Slide1.jpg')
        await ctx.message.add_reaction('✔️')
        await ctx.send(embed = about)

    
    
   

def setup(client):
    client.add_cog(h(client))
