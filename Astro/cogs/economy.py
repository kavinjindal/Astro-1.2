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
mainshop = [{"name":"watch","price":100,"description":"Time"},
                {"name":"laptop","price":1000,"description":"Work"},
                {"name":"PC","price":10000,"description":"Gaming"},
                {"name":"Fogg perfume","price":12000,"description":"Smell good and get urself a gf"}, 
                {"name":"Nitro","price":9900000,"description":"Nothing special, just a joke"},]
async def open_account(user):
        
        users = await get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]['Wallet'] = 100
            users[str(user.id)]['Bank'] = 0
        
        with open('mainbank.json','w') as f:
            json.dump(users,f)
        return True

async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

        return users

async def update_bank(user, change = 0, mode = "Wallet"):
        users = await get_bank_data()

        users[str(user.id)][mode] += change
        
        with open('mainbank.json','w') as f:
            json.dump(users,f)

        account = [users[str(user.id)]['Wallet'], users[str(user.id)]["Bank"]]
        return account

async def buy_this(user,item_name,amount):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                price = item["price"]
                break

        if name_ == None:
            return [False,1]

        cost = price*amount

        users = await get_bank_data()

        bal = await update_bank(user)

        if bal[0]<cost:
            return [False,2]


        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt + amount
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index+=1 
            if t == None:
                obj = {"item":item_name , "amount" : amount}
                users[str(user.id)]["bag"].append(obj)
        except:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"] = [obj]        

        with open("mainbank.json","w") as f:
            json.dump(users,f)

        await update_bank(user,cost*-1,"Wallet")

        return [True,"Worked"]

async def sell_this(user,item_name,amount,price = None):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                if price==None:
                    price = 0.9* item["price"]
                break

        if name_ == None:
            return [False,1]

        cost = price*amount

        users = await get_bank_data()

        bal = await update_bank(user)


        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt - amount
                    if new_amt < 0:
                        return [False,2]
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                    break
                index+=1 
            if t == None:
                return [False,3]
        except:
            return [False,3]    

        with open("mainbank.json","w") as f:
            json.dump(users,f)

        await update_bank(user,cost,"Wallet")

        return [True,"Worked"]
class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bal(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        await open_account(user)
        

        users = await get_bank_data()    
        
        wallet_amt = users[str(user.id)]['Wallet']
        bank_amt = users[str(user.id)]['Bank']

        bal = discord.Embed(
            title = f"{user}'s balance :moneybag: ",
            colour = discord.Colour.green()
        )
        bal.set_thumbnail(url='https://cdn.discordapp.com/attachments/739371149468762133/793754381455196190/money-banknotes-fan_102902-305.jpg')
        bal.add_field(name='Wallet :purse:', value=wallet_amt, inline=False)
        bal.add_field(name='Bank :bank:', value=bank_amt, inline=False)

        await ctx.send(embed = bal)
    @commands.command()
    async def bank(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        await open_account(user)

        users = await get_bank_data()

        bank_amt = users[str(user.id)]['Bank']
        bank = discord.Embed(title = f'Bank Balance of {user}', colour=discord.Colour.red())
        bank.add_field(name = 'Bank', value=bank_amt, inline=False)
        await ctx.send(embed = bank)

    @commands.command()
    async def wallet(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        await open_account(user)

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]['Wallet']
        bank = discord.Embed(title = f'Wallet of {user}', colour=discord.Colour.red())
        bank.add_field(name = 'Wallet', value=wallet_amt, inline=False)
        await ctx.send(embed = bank)
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def beg(self, ctx):
        user = ctx.author
        await open_account(user)

        users = await get_bank_data()  

        earnings = random.randrange(100)
        options = [f'Trump gave you {earnings} coins, lol ', f'You get nothing {ctx.message.author.name}, lmao', f'Lady Gaga donated {earnings} coins to you... :laughing:', 
        f'Your dad has given u {earnings} coins. Say tnx to him.', f'Captain America left {earnings} coins in your bag, you are great!', f'Bustin Jieber gave u {earnings} coins.', 
        'Selena Gomez says, you dont deserve a penny', f'JLo : Get outta here prick!']
        
        await ctx.send(F"{random.choice(options)}")
        


        users[str(user.id)]['Wallet'] += earnings

        with open('mainbank.json','w') as f:
            json.dump(users,f)
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        try:
            user = ctx.author
            await open_account(user)
            #earnings = random.randrange(1000)

            users = await get_bank_data()
            await ctx.send(f'1000 coins have been credited to your account')
            users[str(ctx.author.id)]['Wallet'] += 500
            
            with open('mainbank.json', 'w') as f:
                json.dump(users, f)
        except:
            await ctx.send('The command will be avaiable in 24 hours after executing the command')

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('The command will be available 24 hours after its use')

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)

    @commands.command()
    async def bag(self, ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []


        em = discord.Embed(title = "Bag")
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            em.add_field(name = name, value = amount)    

        await ctx.send(embed = em)    

    @commands.command()
    @commands.is_owner()
    @commands.cooldown(1, 2419200, commands.BucketType.user)
    async def monthly(self, ctx):
        try:

            user = ctx.author
            await open_account(user)
            #earnings = random.randrange(1000)

            users = await get_bank_data()
            await ctx.send(f'20000 coins have been credited to your account')
            users[str(ctx.author.id)]['Wallet'] += 20000
            
            with open('mainbank.json', 'w') as f:
                json.dump(users, f)
        except:
            await ctx.send("This command will be functional after a month. ")

    @monthly.error
    async def monthly_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('The command is on a cooldown of 1 month. ')
    @commands.command(aliases = ["lb"])
    async def leaderboard(self, ctx,x = 5):
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["Wallet"] + users[user]["Bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total,reverse=True)    

        em = discord.Embed(title = f"Top {x} Richest People" , description = "The total money in wallet and bank",color = discord.Color(0xfa43ee))
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            name = await self.client.fetch_user(id_)
            em.add_field(name = f":small_blue_diamond:  {name}" , value = f":coin: {amt}",  inline = False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed = em)
    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def work(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()  

        earnings = random.randrange(1100)
        options = [f'You worked as a sweeper and earned {earnings}', f'You worked as a Police Officer and earned {earnings}', f'You worked as a film director and earned {earnings}', 
        f'You are lazy and u get nothing', f'Go do some real work to earn', f'You worked as a robber and got {earnings}', f'You worked as a Python Programmer in a startup and earned {earnings}']
        
        await ctx.send(F"{random.choice(options)}")
        


        users[str(ctx.author.id)]['Wallet'] += earnings

        with open('mainbank.json','w') as f:
            json.dump(users,f)
    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
    @commands.command()
    async def withd(self, ctx, amount= None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send(f'Hey please enter the amount dude.')
            return

        account = await update_bank(ctx.author)
        amount = int(amount)
        if amount>account[1]:
            await ctx.send(f'You dont have that much of money {ctx.message.author.name}, better check your bank balance')
            return

        if amount<0:
            await ctx.send('Please enter a positive value you noob!')
            return

        await update_bank(ctx.author,amount)
        await update_bank(ctx.author,-1*amount,"Bank")


        await ctx.send(f'You withdrew {amount} coins')

    @commands.command()
    async def dep(self, ctx, amount= None):
        await open_account(ctx.author)
        if amount == None:
            await ctx.send(f'Hey please enter the amount dude.')
            return

        account = await update_bank(ctx.author)
        amount = int(amount)
        if amount>account[0]:
            await ctx.send('You dont have that much of money')
            return

        if amount<0:
            await ctx.send('Please enter a positive value')
            return

        await update_bank(ctx.author,-1*amount)
        await update_bank(ctx.author,amount,"Bank")

        
        await ctx.send(f'You deposited {amount} coins')

    @commands.command()
    async def give(self, ctx,member:discord.Member, amount= None):
        await open_account(ctx.author)
        await open_account(member)

        if amount == None:
            await ctx.send(f'Hey please enter the amount dude.')
            return

        account = await update_bank(ctx.author)
        amount = int(amount)
        if amount>account[1]:
            await ctx.send('You dont have that much of money')
            return

        if amount<0:
            await ctx.send('Please enter a positive value')
            return

        await update_bank(ctx.author,-1*amount, "Bank")
        await update_bank(member,amount,"Bank")

        
        await ctx.send(f'You gave {amount} coins to {member.mention}')

    

    

    @commands.command()
    async def shop(self, ctx):
        em = discord.Embed(title = "Shop")

        for item in mainshop:
            name = item["name"]
            price = item["price"]
            desc = item["description"]
            em.add_field(name = name, value = f"${price} | {desc}")

        await ctx.send(embed = em)

    @commands.command()
    async def buy(self, ctx,item,amount = 1):
        await open_account(ctx.author)

        res = await buy_this(ctx.author,item,amount)

        if not res[0]:
            if res[1]==1:
                await ctx.send("That Object isn't there!")
                return
            if res[1]==2:
                await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
                return


        await ctx.send(f"You just bought {amount} {item}")

    @commands.command()
    async def inv(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        
        await open_account(user)
        #user = ctx.author
        users = await get_bank_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []


        em = discord.Embed(title = f"Inventory of {user}")
        for item in bag:
            name = item["item"]
            amount = item["amount"]

            em.add_field(name = name, value = amount)    

        await ctx.send(embed = em)    

    

    @commands.command()
    async def sell(self, ctx,item,amount = 1):
        await open_account(ctx.author)

        res = await sell_this(ctx.author,item,amount)

        if not res[0]:
            if res[1]==1:
                await ctx.send("That Object isn't there!")
                return
            if res[1]==2:
                await ctx.send(f"You don't have {amount} {item} in your bag.")
                return
            if res[1]==3:
                await ctx.send(f"You don't have {item} in your bag.")
                return

        await ctx.send(f"You just sold {amount} {item}.")

    

def setup(client):
    client.add_cog(Start(client))
