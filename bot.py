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
    # Case where summoner DNE
    if(stats == None):
        await ctx.send('The name does not exist. Summoner names must exist in NA servers.')
    # Case where summoner is unranked
    elif stats == "Unranked":
        name = api.getSummonerByName(summonerName)
        top5 = api.getTopChamps(summonerName)
        embed=discord.Embed(title="League of Legends Ranked (Solo/Duo) Statistics for " + name['name'], color=0x00ff9d)
        file = discord.File("./Discord/Images/Emblem_Iron.png", filename="image.png")
        embed.set_thumbnail(url="attachment://image.png")
        embed.add_field(name="Rank", value='N/A', inline=True)
        embed.add_field(name="Statistics", value="0W 0L (0% WR)", inline=True)
        # + str(api.getKDA(summonerName)/5.0)
        embed.add_field(name="Most Played Champions", value="" + api.formatChamps(top5), inline=False)
        await ctx.send(file = file, embed=embed)
    else:
        wins = stats['wins']
        losses = stats['losses']
        ratio = int(wins/(wins+losses)*100)
        top5 = api.getTopChamps(summonerName)
        embed=discord.Embed(title="League of Legends Ranked (Solo/Duo) Statistics for " + stats['summonerName'], color=0x00ff9d)
        file = discord.File(str(api.getRankImg(stats['tier'])), filename="image.png")
        embed.set_thumbnail(url="attachment://image.png")
        embed.add_field(name="Rank", value=stats['tier'].capitalize() + ' ' + stats['rank'] + ' ' + str(stats['leaguePoints']) + ' LP', inline=True)
        embed.add_field(name="Statistics", value= str(wins) + 'W ' + str(losses) + 'L ' + '(' + str(ratio) + '% WR)', inline=True)
        # + str(api.getKDA(summonerName)/5.0)
        embed.add_field(name="Most Played Champions", value="" + api.formatChampsTop5(top5), inline=False)
        await ctx.send(file = file, embed=embed)

@bot.command(name='chest', help='Displays summoner statistics')
async def getChestChamps(ctx, summonerName):
    api = RiotAPI('RGAPI-0772719d-e9eb-42c1-9f7e-6384bfcc282b')
    # Case where summoner DNE
    try:
        name = api.getSummonerByName(summonerName)['name']
        allChamps = api.getAllChamps(summonerName)
        embed=discord.Embed(title="League of Legends Chest Statistics for " + name, color=0x00ff9d)
        file = discord.File("./Discord/Images/chest.png", filename="image.png")
        embed.set_thumbnail(url="attachment://image.png")
        format1 = api.formatChamps(allChamps, 0)
        format2 = api.formatChamps(allChamps, 1)
        embed.add_field(name="List of Champions", value=format1, inline=True)
        embed.add_field(name="‎", value=format2, inline=True)
        await ctx.send(file = file, embed=embed)
    except:
        await ctx.send('The name does not exist. Summoner names must exist in NA servers.')
    
@bot.command(name='live', help='Live game statistics') 
async def getLive(ctx, summonerName):
    api = RiotAPI('RGAPI-ac6cc217-9f3c-40be-a01b-a6594ace1fc2')


bot.run(TOKEN)