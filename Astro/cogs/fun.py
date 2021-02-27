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
bru_lib = ['https://cdn.discordapp.com/attachments/800269388372508692/802405673761636383/really-bruh-picture-2.jpg', 
'https://cdn.discordapp.com/attachments/800269388372508692/802405633789919272/artworks-000533739219-8qcl2j-t500x500.jpg', 
'https://cdn.discordapp.com/attachments/800269388372508692/802405627770961940/bruh_4x.png', 
'https://cdn.discordapp.com/attachments/800269388372508692/802405585043456050/11d913c39a0aff5067d7ce5b28144eb2.jpg', 
'https://cdn.discordapp.com/attachments/800269388372508692/802405582895316992/9DzrfV60_400x400.jpg',
'https://cdn.discordapp.com/attachments/800269388372508692/802405582102462484/5dd60cfe2a9f024f6595cb91d8a33e77.jpg',
'https://cdn.discordapp.com/attachments/800269388372508692/802405655646306344/i_luff_u.jpg']
class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

   

    @commands.command()
    async def slap(self, ctx,*,name):
        await ctx.send(f'{ctx.author.mention} just slapped :wave: {name}, lol :laughing:')

    @commands.command()
    async def kill(self, ctx, *, name):
        responses1 = [f'{ctx.author.mention} killed {name} with a sniper',
                    f'{ctx.author.mention} shot {name} on the head',
                    f'{name} was stabbed by {ctx.author.mention}',
                    f"{name} drank tea made up of an elephant's sh*t and died",
                    f"{ctx.author.mention} slit {name}'s head using Thor's Stormbreaker.",
                    f"{ctx.author.mention} stole Captain's shield and smacked it on {name}'s jaw.",
                    '\n'f'Unfortunately {name} died :sad:',
                    f'{ctx.author.mention} killed {name} with a hulk smash.',
                    f'An african elephant just sat on {name}.',
                    f"{name}'s teacher caught him cheating in his exams and killed him with a metal scale.",]
        await ctx.send(random.choice(responses1))

    @commands.command()
    async def roast(self, ctx, *, name):
        responses = [
                    
                    f'I would slap you {name}, but that would be animal abuse :laughing:',
                    f'You are the reason that god created middle finger ',
                    f'Is your ass jealous of the amount of shit that comes out of your mouth? :poop:',
                    f"I don't want to waste time roasting asses like you",
                    f"You're so ugly, when you were born, your Mom said 'What a treasure', but your dad said let's throw it away in the bin :laughing:",
                    f"You must have been born on a highway, because thats where most accidents happen",
                    f"How this animal is able to use discord???",
                    f"You are the God's only mistake.",
                    f"You are the God's biggest mistake",
                    f"I would refer to die rather than seeing your face.",
                    f"Hey {ctx.author.mention} you better see yourself before roasting others :laughing:",
                    ]
        await ctx.send(f'Roasting {name} "\n" {random.choice(responses)}')

    @commands.command()
    async def pw(self, ctx):
        s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&"
        passlen = 8
        p =  "".join(random.sample(s,passlen ))
        msg = p.format(ctx)

        await ctx.send(f'Hey {ctx.author.mention}, your password has been sent in the dms to you.')
        await ctx.author.send(f'Here is your generated 8 digit password|| {msg} ||')

    @commands.command()
    async def dice(self, ctx):
        die = ['1', '2', '3', '4', '5', '6']
        dice = discord.Embed(title=f':game_die: Dice Game',
        colour = discord.Colour.blue())
        dice.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        dice.set_thumbnail(url='https://cdn.discordapp.com/attachments/782647287494082611/792315877994266654/tenor.gif')
        dice.add_field(name=f'Dice game', value=f'You got **{random.choice(die)}** on your dice')
        dice.set_footer(text='Astro 999 v1.2.0', icon_url='https://cdn.discordapp.com/attachments/800269388372508692/802434552063590420/Slide1.jpg')
        await ctx.send(embed = dice)

    @commands.command()
    async def toss(self, ctx):
        op = ['Heads', 'Tails']
        toss = discord.Embed(
            title = f"{ctx.author}'s toss game :coin:",
            description = f'{ctx.author} flipped the coin!!'
        )
        toss.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        toss.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/800269388372508692/800357830355714088/tenor.gif')
        toss.add_field(name = f'--------', value=f'You got **{random.choice(op)}** on your coin.')
        toss.set_footer(text='Astro 999 v1.2.0', icon_url='https://cdn.discordapp.com/attachments/800269388372508692/802434552063590420/Slide1.jpg')
        await ctx.send(embed = toss)


    @commands.command()
    async def fsociety(self, ctx):
        fs = discord.Embed(
            title = 'F*** SOCIETY!!!!!!!', 
            colour = discord.Colour.red()
        )
        fs.set_image(url = 'https://media.discordapp.net/attachments/762886017253638164/794601784383504394/tenor.gif')
        await ctx.send(embed = fs)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bruh(self, ctx):
        bruh = discord.Embed(title = 'BRUHHHHH!!!!!!!', colour=discord.Color.teal())
        bruh.set_image(url = random.choice(bru_lib))
        await ctx.send(embed = bruh)

    



def setup(client):
    client.add_cog(fun(client))
