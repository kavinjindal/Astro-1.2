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
from discord.ext.commands import Bot
from multiprocessing.connection import Client
from discord.ext.commands.cooldowns import BucketType
import platform
import asyncio
from datetime import datetime


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
        invite = await ctx.channel.create_invite(max_uses = 100)
        await member.kick(reason=reason)
        await ctx.send(member.name + ' has been kicked')
          
        kicked = discord.Embed(
          title = f'User Kicked in {ctx.guild}', 
          colour = discord.Colour.red(), 
          timestamp=datetime.utcnow())
        kicked.add_field(name = 'Guild', value=f'Guild : {ctx.guild}''\n'f'Guild Id : {ctx.guild.id}''\n'f'{invite}', inline=False)
        kicked.add_field(name = 'User who kicked', value=f'User {ctx.message.author}''\n'f'User ID : {ctx.author.id}', inline=False)
        kicked.add_field(name = 'Kicked User', value=f'User : {member} \n Kicked User ID: {member.id}')
        kicked.add_field(name = 'Reason for Kicking', value=f'{reason}')
        kicked.set_footer(text = 'Astro Mod Log System - v2')
        channel = self.client.get_channel(848438121644294144)
        await channel.send(embed = kicked)

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
        invite = await ctx.channel.create_invite(max_uses = 100)
        kicked = discord.Embed(
          title = f'User Banned in {ctx.guild}', 
          colour = discord.Colour.red(), 
          timestamp=datetime.utcnow())
        kicked.add_field(name = 'Guild', value=f'Guild : {ctx.guild}''\n'f'Guild Id : {ctx.guild.id}''\n'f'{invite}', inline=False)
        kicked.add_field(name = 'User who banned', value=f'User {ctx.message.author}''\n'f'User ID : {ctx.author.id}', inline=False)
        kicked.add_field(name = 'Banned User', value=f'User : {member} \n Banned User ID: {member.id}')
        kicked.add_field(name = 'Reason for Ban', value=f'{reason}')
        kicked.set_footer(text = 'Astro Mod Log System - v2')
        channel = self.client.get_channel(848438418702860318)
        await channel.send(embed = kicked)

        guild = ctx.guild

        try:
            await member.send(f"You were banned from {guild.name} for {reason}")
        except:
            pass
        await guild.ban(member, reason=reason)
        await ctx.send(embed=discord.Embed(description=f"{member.name} was banned by {ctx.author.mention} for {reason}.", color=self.client.color))

    @commands.command()
    @commands.is_owner()
    async def mute(ctx, member: discord.Member=None):
      guild = ctx.guild
      if (not guild.has_role(name="Muted")):
          perms = discord.Permissions(send_messages=False, speak=False)
          
      role = discord.utils.get(ctx.guild.roles, name="Muted")
      await member.add_roles(role)      
      print("🔨 "+member+" was muted.")
      if (not member):
          await ctx.send("Please specify a member to mute")
          return
      

      



   
def setup(client):
    client.add_cog(Mod(client))
