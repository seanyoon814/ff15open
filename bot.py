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
    stats = api.getSummonerRank(summonerName)
    if(stats == None):
        await ctx.send('The name does not exist. Summoner names must exist in NA servers.')
    else:
        wins = stats['wins']
        losses = stats['losses']
        ratio = int(wins/(wins+losses)*100)
        await ctx.send('Summoner Name: ' + stats['summonerName']
        +'\nRank: ' + stats['tier'].capitalize() + ' ' + stats['rank'] + ' ' + str(stats['leaguePoints']) + ' LP'
        + '\n' + str(ratio) + '% WR' + ' (' + str(wins) + 'W ' + str(losses) + 'L)')

@bot.command(name='live', help='Live game statistics') 
async def getLive(ctx, summonerName):
    api = RiotAPI('RGAPI-ac6cc217-9f3c-40be-a01b-a6594ace1fc2')
    
bot.run(TOKEN)