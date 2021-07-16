import discord
from discord.ext import commands
from discord import DMChannel
from discord import Intents
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



 # https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID

class Chatbot(commands.Cog):
    def __init__(self, client):
        self.client = client
        
              
        
        


          
    
    

    
      

    

def setup(client):
    client.add_cog(Chatbot(client))
