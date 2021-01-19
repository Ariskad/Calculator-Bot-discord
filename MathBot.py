import discord
from discord.ext import commands
import random
import time
import math
from decimal import *
from discord.ext.commands import has_permissions, CheckFailure


client = commands.Bot(command_prefix=",")

getcontext().prec = 6
Decimal(1) / Decimal(7)

getcontext().prec = 28
Decimal(1) / Decimal(7)

limit = 0

ids = []

@client.event
async def on_ready():
    print("MathBot is running")await client.change_presence(activity=discord.Game(',help'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

    @client.command()
async def add(ctx,a:int, *,b:int): 
    """ Προσθέτει το πρώτο αριθμό με τον δεύτερο(a+b)(P.e.  2 2=4)"""
    await ctx.send(a+b)

    

@client.command() 
async def sub(ctx,a:int, *,b:int): 
    """Αφαιρεί το πρώτο αριθμό με τον δεύτερο(a-b)(P.e  2 2=4)"""
    await ctx.send(a-b)
    
    

@client.command() 
async def multiply(ctx,a:int, *,b:int): 
    """Πολλαπλασιάζει το πρώτο αριθμό με τον δεύτερο(a*b)(P.e  2 2=4)"""
    await ctx.send(a*b)
    

@client.command() 
async def divide(ctx,a:int, *,b:int): 
    """Διαιρεί το πρώτο αριθμό με τον δεύτερο(a/b)(P.e  2 2=1)"""
    if b == 0:
        await ctx.send("False")
    else:
        await ctx.send(a/b)
    

@client.command()
async def power(ctx,a:int, *,b:int):
    """Παίρνει τον πρώτο αριθμό και τον υψώνει στον αριθμό του δεύτερου(a^b)(P.e  2 2=4)"""
    await ctx.send(a**b)
    

client.run("TOKEN")
