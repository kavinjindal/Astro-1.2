from typing import Optional
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
from discord import Embed
from discord.utils import get
from discord.ext.commands import Cog
from discord.ext.commands import command

cd = discord.Embed(
title = 'Commands for Astro', 
colour = discord.Colour.blue())
cd.add_field(name = 'Prefix', value='a!')

cd.set_footer(text = f'Write `a!help [command_name] to know more about the command`')
cd.add_field(name = 'Mod commands', value='`ban [@user] [reason], unban [@user], kick [@user] [reason], clear [amount] `', inline=False)
cd.add_field(name = 'Fun Commands', value='`kill [@user], slap [@user], roast [@user], pw, dice, toss, fsociety, bruh, hack, bitcoin, _8ball [your question]`', inline=False)
cd.add_field(name = 'Memer', value='`ph, meme, whm, dank, pewds, fb, animal`')
cd.add_field(name = 'Dev commands', value='`[Only available for owner] - send, rule, create, `', inline=False)
cd.add_field(name = 'Bot info', value='`stats, info, add, github, support, devop, credits, update, vote, calldevs [yourtext], website`', inline=False)
#cd.add_field(name = 'Dev info', value='`devop, credits`', inline=False)
cd.add_field(name = 'Meta Commands', value='`guild, av, ping`')
cd.add_field(name = 'Economy Commands', value='`bal, shop, bag, buy [item_name] [amount], give [@user] [amount from bank], withd [amount], dep [amount], sell [item_name] [amount], beg, work, daily, lb, bet [amount]`', inline=False)
cd.add_field(name = 'Calculations (New Feature)', value='`sqr [number], cube [number], addit [first digit] [second digit], subit [first digit] [second digit]`')
cd.add_field(name = 'Weather', value='`weather [valid city name]`')


def syntax(command):
	cmd_and_aliases = "|".join([str(command), *command.aliases])
	params = []

	for key, value in command.params.items():
		if key not in ("self", "ctx"):
			params.append(f"[{key}]" if "NoneType" in str(value) else f"<{key}>")

	params = " ".join(params)

	return f"`{cmd_and_aliases} {params}`"

'''
class HelpMenu(ListPageSource):
	def __init__(self, ctx, data):
		self.ctx = ctx
		'''
#		super().__init__(data, per_page=3)

#	async def write_page(self, menu, fields=[]):
		#offset = (menu.current_page*self.per_page) + 1
		#len_data = len(self.entries)
'''
		embed = Embed(title="Help",
					  description="Welcome to the Carberretta help dialog!",
					  colour=self.ctx.author.colour)
		embed.set_thumbnail(url=self.ctx.guild.me.avatar_url)
		embed.set_footer(text=f"{offset:,} - {min(len_data, offset+self.per_page-1):,} of {len_data:,} commands.")

		#for name, value in fields:
		#	embed.add_field(name=name, value=value, inline=False)

		#return embed

	#async def format_page(self, menu, entries):
	#	fields = []

	#	for entry in entries:
	#		fields.append((entry.brief or "No description", syntax(entry)))

	#	return await self.write_page(menu, fields)
'''
class Help(Cog):
	def __init__(self, bot):
		self.bot = bot
		self.bot.remove_command("help")

	async def cmd_help(self, ctx, command):
		embed = Embed(title=f"Help with `{command}`",
					  description=syntax(command),
					  colour=ctx.author.colour)
		embed.add_field(name="Command description", value=command.help)
		await ctx.send(embed=embed)

	@command(name="help")
	async def show_help(self, ctx, cmd: Optional[str]):
		"""Shows this message."""
		if cmd is None:
			await ctx.send(embed = cd)

		else:
			if (command := get(self.bot.commands, name=cmd)):
				await self.cmd_help(ctx, command)

			else:
				await ctx.send("That command does not exist.")
	
	


def setup(bot):
	bot.add_cog(Help(bot))