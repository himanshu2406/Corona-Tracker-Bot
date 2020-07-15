'''
This project was made by https://github.com/himanshu2406 , incase of cloning / modifying or release of any bot based on this source code,
You are obligated to give credits to the original author.

Original repo: https://github.com/himanshu2406/Corona-Tracker-Bot

Original Bot Support Server: https://discord.gg/kdj6DMr
'''

import cv2
import numpy as np
from discord.ext import commands
import requests
import time
import os
import random
import hashlib
from urllib3.exceptions import InsecureRequestWarning
import urllib
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json
import pickle
import re
import textwrap
import asyncio
import uuid 
import imgkit
import urllib.request


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!cov ')
client.remove_command('help')


@client.command(pass_context=True)
async def graph(ctx, typeofgraph, arg2 = 'none'):
    if typeofgraph.lower() == 'top10' and arg2 != 'none':
        newcountry = arg2.lower() 
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/top_10_countries_' + newcountry + '.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for Top 10 " + newcountry + 'Cases', color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'country' and arg2 != 'none':
        if arg2 == 'all':
            urltobe = 'https://github.com/resoucesforcorona/Resources/blob/master/All_countries.png?raw=true'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for all countries", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/' + newcountry + '.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for :" + newcountry, color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'continent' and arg2 != 'none':
        if arg2 == 'all':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/All_continents.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for all continents", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/' + newcountry + '.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for :" + newcountry, color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'pie':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/all_countrywise_pie.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for Pie", color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'predict' and arg2 != 'none':
        newcountry = (arg2.lower())
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/world_prediction_curve_' + newcountry + '.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global prediction curve for " + newcountry, color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'global' and arg2 != 'none':
        if arg2 == 'daily_confirmed':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/daily_confirmed_cases_global.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global daily confirmed", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        elif arg2 == 'daily_deaths':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/daily_deaths_cases_global.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global daily deaths", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        elif arg2 == 'trend':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/world_trend_confirmed_cases.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global trend", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/worldwide_cases_deaths.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global total deaths", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'trend' and arg2 != 'none':
        if arg2 == 'confirmed':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/trend_comparison_continents_confirmed.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for trend comparison b/w continents [confirmed]", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/trend_comparison_countries_deaths.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for trend comparison b/w countries [deaths]" + newcountry, color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'spread':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/countries_vs_date_spread.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for number of countries infected vs date" , color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

@client.command(pass_context=True)
async def g(ctx, typeofgraph, arg2 = 'none'):
    if typeofgraph.lower() == 'top10' and arg2 != 'none':
        newcountry = arg2.lower() 
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/top_10_countries_' + newcountry + '.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for Top 10 " + newcountry + 'Cases', color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'country' and arg2 != 'none':
        if arg2 == 'all':
            urltobe = 'https://github.com/resoucesforcorona/Resources/blob/master/All_countries.png?raw=true'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for all countries", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/' + newcountry + '.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for :" + newcountry, color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'continent' and arg2 != 'none':
        if arg2 == 'all':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/All_continents.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for all continents", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/' + newcountry + '.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for :" + newcountry, color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'pie':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/all_countrywise_pie.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for Pie", color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'predict' and arg2 != 'none':
        newcountry = (arg2.lower())
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/world_prediction_curve_' + newcountry + '.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global prediction curve for " + newcountry, color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'global' and arg2 != 'none':
        if arg2 == 'daily_confirmed':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/daily_confirmed_cases_global.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global daily confirmed", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        elif arg2 == 'daily_deaths':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/daily_deaths_cases_global.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global daily deaths", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        elif arg2 == 'trend':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/world_trend_confirmed_cases.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global trend", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/worldwide_cases_deaths.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for global total deaths", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'trend' and arg2 != 'none':
        if arg2 == 'confirmed':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/trend_comparison_continents_confirmed.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for trend comparison b/w continents [confirmed]", color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/trend_comparison_countries_deaths.png'
            embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for trend comparison b/w countries [deaths]" + newcountry, color=0x00ff00)
            embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
            embedVar.set_image(url=urltobe)
            await ctx.send(embed=embedVar)

    if typeofgraph.lower() == 'spread':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/countries_vs_date_spread.png'
        embedVar = discord.Embed(title="Corona Tracker",url = 'https://anondoser.xyz', description="Graph for number of countries infected vs date" , color=0x00ff00)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4') 
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)

@client.command(pass_context=True)
async def help(ctx):
    embedVar = discord.Embed(title="Corona Tracker Help Panel", description="Here's some help for you :heart:", color=0x00ff00)
    embedVar.add_field(name="!cov graph [commands]", value="Consists of graphical predictions, analysis , statistics and more see below for command", inline=False)
    embedVar.add_field(name="!cov g [commands]", value="Same as above, use !cov ghelp for list of commands", inline=False)
    embedVar.add_field(name="!cov ghelp", value="Help and commands list for `!cov graph`", inline=False)
    embedVar.add_field(name="!cov all", value="Shows global Covid-19 statistics", inline=False)
    embedVar.add_field(name="!cov country {your country} {complete (optional)}", value="Shows you a particular country's stats (Optional- use complete for full report of the country)", inline=False)
    embedVar.add_field(name="!cov help", value="Shows you this message", inline=False)
    embedVar.add_field(name="!invite", value="Sends you the links to invite the bot to your own server & the official bot server", inline=False)
    embedVar.add_field(name="github", value="https://github.com/himanshu2406/Corona-Tracker", inline=False)
    embedVar.add_field(name="tip :heart: ", value="Buy me a Coffee [sends addresses for tipping]", inline=False)
    embedVar.add_field(name="Dev Contact", value="Firelogger#7717", inline=False)
    await ctx.send(embed=embedVar)


@client.command(pass_context=True)
async def ghelp(ctx):
    embedVar = discord.Embed(title="Corona Tracker graph commands ", description="Use - `!cov graph [command] [arguments]` you can use `!cov g` instead too", color=0x00ff00)
    embedVar.add_field(name="How to use - ", value="```!cov graph [commands given below] [argument]``` arguments in round brackets - () mean type exact commands as given , \n Square brackets -[] mean a variable like your country name", inline=False)
    embedVar.add_field(name="spread", value="No arguments ; shows the spread among countries vs date", inline=False)
    embedVar.add_field(name="pie", value="No arguments ; shows a list of pie charts for cases among countries", inline=False)
    embedVar.add_field(name="top10 (confirmed/active/deaths/recovered)", value="Shows top 10 countries based on the argument given", inline=False)
    embedVar.add_field(name="global (daily_confirmed/daily_deaths/trend/deaths)", value="Shows graphs for global arguments", inline=False)
    embedVar.add_field(name="country [country name]", value="Graph for the country given", inline=False)
    embedVar.add_field(name="continent [continent name]", value="Graph for the continent given", inline=False)
    embedVar.add_field(name="predict (confirmed/deaths)", value="Shows graphical projections for the future along with next 10 day predicted figures for the argument", inline=False)
    embedVar.add_field(name="trend (confirmed/deaths)", value="Shows trend between different countries / continents based on the argument", inline=False)
    #embedVar.add_field(name="github", value="https://github.com/himanshu2406/Corona-Tracker", inline=False)
    #embedVar.add_field(name="tip :heart: ", value="Buy me a Coffee [sends addresses for tipping]", inline=False)
    embedVar.add_field(name="Example", value="```!cov graph top10 confirmed```", inline=False)
    embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    await ctx.send(embed=embedVar)

@client.command(pass_context=True)
async def country(ctx,args, complete = 'false'):
    found = False
    response = requests.get('https://disease.sh/v3/covid-19/countries?yesterday=false&sort=cases&allowNull=true')
    x = response.text
    y = json.loads(x)
    embedVar = discord.Embed(title="Covid Stats for: " + args.capitalize(), description="Statistics from disease.sh", color=0xe33b3b, url = 'https://anondoser.xyz')

    for i in y:
        if i['country'].lower() == args.lower():
            if complete == 'complete':
                for y in i:
                    if y == 'countryInfo':
                        continue
                    embedVar.add_field(name=y, value=str(i[y]), inline=True)
            else:
                embedVar.add_field(name='Cases:', value=str(i['cases']), inline=True)
                embedVar.add_field(name='Cases Today:', value=str(i['todayCases']), inline=True)
                embedVar.add_field(name='Deaths:', value=str(i['deaths']), inline=True)
                embedVar.add_field(name='Deaths Today:', value=str(i['todayDeaths']), inline=True)
                embedVar.add_field(name='Recovered:', value=str(i['recovered']), inline=True)
                embedVar.add_field(name='Recovered Today:', value=str(i['todayRecovered']), inline=True)
                embedVar.add_field(name='Active:', value=str(i['active']), inline=True)
                embedVar.add_field(name='Critical:', value=str(i['critical']), inline=True)
                embedVar.add_field(name='Tests:', value=str(i['tests']), inline=True)
            urltobe = str(i['countryInfo']['flag'])
            found = True
    if found == False:
        embedVar = discord.Embed(title="Invalid Country: " + args.capitalize(), description="Error , the country doesn't exist in the database", color=0xe33b3b, url = 'https://anondoser.xyz')
        await ctx.send(embed=embedVar)
    else:
        embedVar.set_thumbnail(url=urltobe)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
        await ctx.send(embed=embedVar)
        return

@client.command(pass_context=True)
async def all(ctx):
        response = requests.get('https://disease.sh/v3/covid-19/all')
        x = response.text
        y = json.loads(x)
        embedVar = discord.Embed(title="Covid Worldwide Stats", description="Statistics from disease.sh", color=0xe33b3b, url = 'https://anondoser.xyz')
        embedVar.set_thumbnail(url='https://i0.wp.com/www.inventiva.co.in/wp-content/uploads/2020/03/corona-virus-negative.png')
        for i in y:
            embedVar.add_field(name=i, value=str(y[i]), inline=True)
        embedVar.set_footer(text ="Firelogger#7717", icon_url = 'https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
        await ctx.send(embed=embedVar)
        return   


@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" a !help in " + str(len(client.guilds)) + " server(s)"))



@client.event
async def on_message(message):
	# do previous on_message stuff here
	await client.process_commands(message) # add at bottom to allow commands to work

client.run(TOKEN)
