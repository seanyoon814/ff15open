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
    api = RiotAPI('RGAPI-0772719d-e9eb-42c1-9f7e-6384bfcc282b')
    stats = api.getSummonerRank(summonerName)
    if(stats == None):
        await ctx.send('The name does not exist. Summoner names must exist in NA servers.')
    else:
        wins = stats['wins']
        losses = stats['losses']
        ratio = int(wins/(wins+losses)*100)
        top5 = api.getTopChamps(summonerName)
        
        #ranked players
        # await ctx.send('Summoner Name: ' + stats['summonerName']
        # +'\nRank: ' + stats['tier'].capitalize() + ' ' + stats['rank'] + ' ' + str(stats['leaguePoints']) + ' LP'
        # + '\n' + str(ratio) + '% WR' + ' (' + str(wins) + 'W ' + str(losses) + 'L)'
        # + top5[0] + "\n" + top5[1] + "\n" + top5[2] + "\n" + top5[3] + "\n" + top5[4] + "\n", 
        # file=discord.File(api.getRankImg(stats['tier'])))
        embed=discord.Embed(title="League of Legends Ranked (Solo/Duo) Statistics for " + stats['summonerName'], color=0x00ff9d)
        file = discord.File(str(api.getRankImg(stats['tier'])), filename="image.png")
        embed.set_thumbnail(url="attachment://image.png")
        embed.add_field(name="Rank", value=stats['tier'].capitalize() + ' ' + stats['rank'] + ' ' + str(stats['leaguePoints']) + ' LP', inline=True)
        embed.add_field(name="Statistics", value= str(wins) + 'W ' + str(losses) + 'L ' + '(' + str(ratio) + '% WR)', inline=True)
        # + str(api.getKDA(summonerName)/5.0)
        embed.add_field(name="Most Played Champions", value="" + api.formatChamps(top5), inline=False)
        await ctx.send(file = file, embed=embed)


@bot.command(name='live', help='Live game statistics') 
async def getLive(ctx, summonerName):
    api = RiotAPI('RGAPI-ac6cc217-9f3c-40be-a01b-a6594ace1fc2')


bot.run(TOKEN)