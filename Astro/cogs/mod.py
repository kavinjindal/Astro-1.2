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


class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    #@client.command(aliases=['c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Purged {amount} messages on the request of {ctx.author}')
        #asyncio.sleep(2)
        await asyncio.sleep(5)
        await ctx.channel.purge(limit = 1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member,*,reason='No reason provided'):
        await member.kick(reason=reason)
        await ctx.send(member.name + 'Has been kicked')
        await member.send('You were kicked from there server...LOL' '\n' f'Reason : {reason}')  

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx,*, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if(user.name , user.discriminator)==(member_name, member_disc):
                await ctx.guild.unban(user)
                await member.send(f'You have been unbanned, congrats')
                await ctx.send(member_name + "Has been unbanned")
                return

        await ctx.send(member+"User not found")

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans a user"""
        if member.id == ctx.author.id:
            return await ctx.send("You can't do that to yourself!")
        if member.top_role >= ctx.me.top_role:
            return await ctx.send("That member's top role is higher or equal to mine!")

        guild = ctx.guild

        try:
            await member.send(f"You were banned from {guild.name} for {reason}")
        except:
            pass
        await guild.ban(member, reason=reason)
        await ctx.send(embed=discord.Embed(description=f"{member.name} was banned by {ctx.author.mention} for {reason}.", color=self.bot.color))

   
def setup(client):
    client.add_cog(Mod(client))
