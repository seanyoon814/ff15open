# bot.py
import os
import random

import discord
from RiotAPI import RiotAPI
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='stats', help='Displays summoner statistics') 
async def getStats(ctx, summonerName):
    api = RiotAPI('RGAPI-ac6cc217-9f3c-40be-a01b-a6594ace1fc2')
    name = api.getSummonerStats(summonerName, 'name')
    if(name == None):
        await ctx.send('The name does not exist. Summoner names must exist in NA servers.')
    else:
        level = api.getSummonerStats(summonerName, 'summonerLevel')
        await ctx.send('Summoner Name: ' + name + ' \nSummoner Level: ' + str(level))
    
bot.run(TOKEN)