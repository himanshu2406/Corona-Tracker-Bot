'''
This project was made by https://github.com/himanshu2406 , incase of cloning / modifying or release of any bot based on this source code,
You are obligated to give credits to the original author.

Original repo: https://github.com/himanshu2406/Corona-Tracker-Bot

Original Bot Support Server: https://discord.gg/kdj6DMr
'''

import uuid
import urllib.request
import asyncio
import textwrap
import re
import pickle
import json
from dotenv import load_dotenv
import discord
import cv2
import numpy as np
from discord.ext import commands
import time
import os
import random
import hashlib
from urllib3.exceptions import InsecureRequestWarning
import urllib3
import diseaseapi
from helper_functions import *
urllib3.disable_warnings(category=InsecureRequestWarning)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!cov ')
client.remove_command('help')

api_client = diseaseapi.Client().covid19

@client.command(help="Restarts the bot, requires admin permission")
@commands.has_role('admin')
async def restart(ctx):
    if ctx.message.author.id == 550965528936710154:
        await ctx.send('Restarting...')
        print('Restarting...')
        try:
            await client.logout()
        finally:
            os.system("py -3 bot.py")


@client.command(help="Shuts Down The bot, Requires admin permission")
@commands.has_role('admin')
async def shutdown(ctx):
    if ctx.message.author.id == 550965528936710154:
        await ctx.send('Bot is Shut Down')
        print('Shut Down Command Received')
        await client.logout()
        return


@client.command()
@commands.has_role('admin')
async def botservers(ctx):
    if ctx.message.author.id == 550965528936710154:
        list_guilds = []
        total_mem = 0
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" a !cov help in " + str(len(client.guilds)) + " server(s)"))
        await ctx.send("I'm in " + str(len(client.guilds)) + " servers")
        for guild in client.guilds:
            total_mem += len(guild.members)
            list_guilds.append(guild.name + ' : ' + str(guild.id))
        list_guilds.append('Total members: ' + str(total_mem))

        # await ctx.send(list_guilds)
        print(list_guilds)
        await ctx.send('Total members: ' + str(total_mem))
        return


@client.command()
@commands.has_role('admin')
async def leave(ctx, id):
    if ctx.message.author.id == 550965528936710154:
        to_leave = client.get_guild(int(id))
        await ctx.send('Leaving ' + str(to_leave))
        try:
            await to_leave.leave()
            await ctx.send('Left ' + str(to_leave))
        except:
            await ctx.send('Failed leaving ' + str(to_leave))
        return


@commands.group(name='graph', aliases=['g'])
async def graph(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.invoke(client.get_command('ghelp'))


@graph.command(name='top10')
async def graphtop10(ctx, arg2):
    if arg2 not in ['confirmed', 'active', 'deaths', 'recovered']:
        return

    newcountry = arg2.lower()
    urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/top_10_countries_' + \
        newcountry + '.png' + '?' + str(uuid.uuid4().hex[:15])
    embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                description="Graph for Top 10 " + newcountry + 'Cases', color=0x00ff00)
    embedVar.set_footer(
        text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    embedVar.set_image(url=urltobe)
    await ctx.send(embed=embedVar)


@graph.command(name='country')
async def graphcountry(ctx, arg2='all'):
        if arg2 == 'all':
            urltobe = 'https://github.com/resoucesforcorona/Resources/blob/master/All_countries.png?raw=true'
            embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                     description="Graph for all countries", color=0x00ff00)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/' + \
                newcountry + '.png' + '?' + str(uuid.uuid4().hex[:15])
            embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                     description="Graph for: " + newcountry, color=0x00ff00)
            
        embedVar.set_footer(
            text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)


@graph.command(name='continent')
async def graphcontinent(ctx, arg2='all'):
        if arg2 == 'all':
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/All_continents.png'
            embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                     description="Graph for all continents", color=0x00ff00)

        else:
            newcountry = (arg2.lower()).capitalize()
            urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/' + \
                newcountry + '.png' + '?' + str(uuid.uuid4().hex[:15])
            embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                     description="Graph for: " + newcountry, color=0x00ff00)

        embedVar.set_footer(
            text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)


@graph.command(name='pie')
async def graphpie(ctx):
    urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/all_countrywise_pie.png'
    embedVar = discord.Embed(
        title="Corona Tracker", url='https://anondoser.xyz', description="Graph for Pie", color=0x00ff00)
    embedVar.set_footer(
        text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    embedVar.set_image(url=urltobe)
    await ctx.send(embed=embedVar)


@graph.command(name='predict')
async def predict(ctx, arg2):
    newcountry = (arg2.lower())
    urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/world_prediction_curve_' + \
        newcountry + '.png' + '?' + str(uuid.uuid4().hex[:15])
    embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                description="Graph for global prediction curve for " + newcountry, color=0x00ff00)
    embedVar.set_footer(
        text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    embedVar.set_image(url=urltobe)
    await ctx.send(embed=embedVar)


@graph.command(name='global')
async def graphglobal(ctx, arg2):
    if arg2 not in ['daily_confirmed', 'daily_deaths', 'trend', 'deaths']:
        return

    if arg2 == 'daily_confirmed':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/daily_confirmed_cases_global.png'
        embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                    description="Graph for global daily confirmed", color=0x00ff00)

    elif arg2 == 'daily_deaths':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/daily_deaths_cases_global.png'
        embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                    description="Graph for global daily deaths", color=0x00ff00)

    elif arg2 == 'trend':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/world_trend_confirmed_cases.png'
        embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                    description="Graph for global trend", color=0x00ff00)

    else:
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/worldwide_cases_deaths.png'
        embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                    description="Graph for global total deaths", color=0x00ff00)
    
    embedVar.set_footer(
            text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    embedVar.set_image(url=urltobe)
    await ctx.send(embed=embedVar)


@graph.command(name='trend')
async def graphtrend(ctx, arg2):
    if arg2 not in ['confirmed', 'deaths']:
        return

    if arg2 == 'confirmed':
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/trend_comparison_continents_confirmed.png'
        embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                    description="Graph for trend comparison b/w continents [confirmed]", color=0x00ff00)

    else:
        newcountry = (arg2.lower()).capitalize()
        urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/trend_comparison_countries_deaths.png'
        embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                    description="Graph for trend comparison b/w countries [deaths]" + newcountry, color=0x00ff00)
    
        embedVar.set_footer(
            text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
        embedVar.set_image(url=urltobe)
        await ctx.send(embed=embedVar)


@graph.command(name='spread')
async def graphspread(ctx):
    urltobe = 'https://raw.githubusercontent.com/resoucesforcorona/Resources/master/countries_vs_date_spread.png'
    embedVar = discord.Embed(title="Corona Tracker", url='https://anondoser.xyz',
                                description="Graph for number of countries infected vs date", color=0x00ff00)
    embedVar.set_footer(
        text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    embedVar.set_image(url=urltobe)
    await ctx.send(embed=embedVar)


@client.command()
async def help(ctx):
    embedVar = discord.Embed(title="Corona Tracker Help Panel",
                             description="Here's some help for you :heart:", color=0x00ff00)
    embedVar.add_field(
        name="!cov graph [commands]", value="Consists of graphical predictions, analysis , statistics and more see below for command", inline=False)
    embedVar.add_field(
        name="!cov g [commands]", value="Same as above, use !cov ghelp for list of commands", inline=False)
    embedVar.add_field(
        name="!cov ghelp", value="Help and commands list for `!cov graph`", inline=False)
    embedVar.add_field(
        name="!cov all", value="Shows global Covid-19 statistics", inline=False)
    embedVar.add_field(name="!cov interactive", value="Sends the best live interactive maps \n See how the Covid spread on the world map from the very start \n See live status of Covid on the world map \n See Mortality Progression from the very beginning", inline=False)
    embedVar.add_field(name="!cov country {your country} {complete (optional)}",
                       value="Shows you a particular country's stats (Optional- use complete for full report of the country)", inline=False)
    embedVar.add_field(
        name="!cov help", value="Shows you this message", inline=False)
    embedVar.add_field(
        name="!cov invite", value="Sends you the links to invite the bot to your own server & the official bot server", inline=False)
    embedVar.add_field(
        name="github", value="https://github.com/himanshu2406/Corona-Tracker-Bot", inline=False)
    embedVar.add_field(
        name="tip :heart: ", value="Buy me a Coffee [sends addresses for tipping]", inline=False)
    embedVar.add_field(name="Dev Contact",
                       value="Firelogger#7717", inline=False)
    await ctx.send(embed=embedVar)


@client.command()
async def invite(ctx):
    embedVar = discord.Embed(title="Invite me", url='https://discord.com/api/oauth2/authorize?client_id=731855425145798668&permissions=121856&scope=bot',
                             description="Click the title to invite to your own server", color=0x00ff00)
    embedVar.set_footer(text="Firelogger#7717",
                        icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    await ctx.send(embed=embedVar)


@client.command()
async def tip(ctx):
    embedVar = discord.Embed(title="Tip :heart:", url='https://www.buymeacoffee.com/anondoser/shop',
                             description="Donate for improving the services and help running the bot", color=0x00ff00)
    embedVar.add_field(
        name="Btc address", value="```37btgSzgWdywmSPeBN5rUH8W5G9EYJoRoA```", inline=False)
    embedVar.add_field(
        name="Paypal", value="```https://www.paypal.me/firelogger```", inline=False)
    embedVar.add_field(
        name="For more", value="For more methods please dm me", inline=False)
    embedVar.set_footer(text="Firelogger#7717",
                        icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    await ctx.send(embed=embedVar)


@client.command()
async def interactive(ctx):
    embedVar = discord.Embed(title="Interactive and playable Maps and statistics",
                             description="Play with these live maps , statistics and visuals", color=0x00ff00)
    embedVar.add_field(name="World Map Live Progression",
                       value="See how COVID spread from the very beginning on the world map, seekable and playable", inline=False)
    embedVar.add_field(
        name="Link", value="https://corona.anondoser.xyz/worldmap_progression.html", inline=False)
    embedVar.add_field(name="World Map static interactive ",
                       value="see the current spread of Covid-19 on the world map", inline=False)
    embedVar.add_field(
        name="Link", value="https://corona.anondoser.xyz/worldmap_cases_interactive.html", inline=False)
    embedVar.add_field(name="Mortality rate Live progression",
                       value="A beautiful playable and seekable representation of the mortality rate progression from the beginning , see those balls bounce", inline=False)
    embedVar.add_field(
        name="Link", value="https://corona.anondoser.xyz/mortalityrate_progression.html", inline=False)
    embedVar.set_footer(text="Firelogger#7717",
                        icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    await ctx.send(embed=embedVar)


@client.command()
async def ghelp(ctx):
    embedVar = discord.Embed(title="Corona Tracker graph commands ",
                             description="Use - `!cov graph [command] [arguments]` you can use `!cov g` instead too", color=0x00ff00)
    embedVar.add_field(name="How to use - ",
                       value="```!cov graph [commands given below] [argument]``` arguments in round brackets - () mean type exact commands as given , \n Square brackets -[] mean a variable like your country name", inline=False)
    embedVar.add_field(
        name="spread", value="No arguments ; shows the spread among countries vs date", inline=False)
    embedVar.add_field(
        name="pie", value="No arguments ; shows a list of pie charts for cases among countries", inline=False)
    embedVar.add_field(name="top10 (confirmed/active/deaths/recovered)",
                       value="Shows top 10 countries based on the argument given", inline=False)
    embedVar.add_field(name="global (daily_confirmed/daily_deaths/trend/deaths)",
                       value="Shows graphs for global arguments", inline=False)
    embedVar.add_field(
        name="country [country name]", value="Graph for the country given", inline=False)
    embedVar.add_field(name="continent [continent name]",
                       value="Graph for the continent given", inline=False)
    embedVar.add_field(name="predict (confirmed/deaths)",
                       value="Shows graphical projections for the future along with next 10 day predicted figures for the argument", inline=False)
    embedVar.add_field(name="trend (confirmed/deaths)",
                       value="Shows trend between different countries / continents based on the argument", inline=False)
    #embedVar.add_field(name="github", value="https://github.com/himanshu2406/Corona-Tracker", inline=False)
    #embedVar.add_field(name="tip :heart: ", value="Buy me a Coffee [sends addresses for tipping]", inline=False)
    embedVar.add_field(
        name="Example", value="```!cov graph top10 confirmed```", inline=False)
    embedVar.set_footer(text="Firelogger#7717",
                        icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    await ctx.send(embed=embedVar)


@client.command(aliases=['c'])
async def country(ctx, args, complete='full'):
    if complete not in ['full', 'micro']:
        return 

    try:
        i = await api_client.country(args)
        yday_c = await api_client.country(i.name, yesterday=True)
    except diseaseapi.NotFound:
        embedVar = discord.Embed(title="Invalid Country: " + args.capitalize(), description="Error, the country doesn't exist in the database", color=0xe33b3b, url='https://anondoser.xyz')
        await ctx.send(embed=embedVar)

    embedVar = discord.Embed(description="Statistics from disease.py",
                                color=0xe33b3b, url='https://anondoser.xyz')

    yday_c = await api_client.country(i.name, yesterday=True)
        
    cases_diff = cleaned_diff(i.cases, yday_c.cases)
    death_diff = cleaned_diff(i.deaths, yday_c.deaths)
    re_diff = cleaned_diff(i.recoveries, yday_c.recoveries)
    active_diff = cleaned_diff(i.active, yday_c.active)
    crit_diff = cleaned_diff(i.critical, yday_c.critical)
    test_diff = cleaned_diff(i.tests, yday_c.tests)

    embedVar.add_field(name='Cases:', value=check_na(i.cases)+cases_diff, inline=True)
    embedVar.add_field(name='Cases Today:', value=check_na(i.today.cases), inline=True)
    embedVar.add_field(name='Deaths:', value=check_na(i.deaths)+death_diff, inline=True)
    embedVar.add_field(name='Deaths Today:', value=check_na(i.today.deaths), inline=True)
    embedVar.add_field(name='Recovered:', value=check_na(i.recoveries)+re_diff, inline=True)
    embedVar.add_field(name='Recovered Today:', value=check_na(i.today.recoveries), inline=True)
    embedVar.add_field(name='Active:', value=check_na(i.active)+active_diff, inline=True)
    embedVar.add_field(name='Critical:', value=check_na(i.critical)+crit_diff, inline=True)
    embedVar.add_field(name='Tests:', value=check_na(i.tests)+test_diff, inline=True)
    urltobe = str(i.info.flag)

    if complete == 'complete':
        embedVar.add_field(name ='Cases per Million', value= i.per_million.cases, inline=True)
        embedVar.add_field(name ='Active per Million', value= i.per_million.active, inline=True)
        embedVar.add_field(name ='Recoveries per Million', value= i.per_million.recoveries, inline=True)
        embedVar.add_field(name ='Tests per Million', value= i.per_million.tests, inline=True)
        embedVar.add_field(name ='Deaths per Million', value= i.per_million.deaths, inline=True)
        embedVar.add_field(name ='Critical per Million', value= i.per_million.critical, inline=True)
        embedVar.add_field(name ='One Case per Person', value= i.per_people.case, inline=True)
        embedVar.add_field(name ='One Death per Person', value= i.per_people.death, inline=True)
        embedVar.add_field(name ='One Test per Person', value= i.per_people.test, inline=True)
        embedVar.add_field(name ='Updated', value= i.updated, inline=True)

    embedVar.title = "Covid Stats for: " + i.name
    embedVar.set_thumbnail(url=urltobe)
    embedVar.set_footer(
        text="Firelogger#7717", icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    await ctx.send(embed=embedVar)


@client.command()
async def all(ctx):
    response = await api_client.all()
    embedVar = discord.Embed(title="Covid Worldwide Stats",
                                 description="Statistics from disease.py", color=0xe33b3b, url='https://anondoser.xyz')
    

    yday_c = await api_client.all(yesterday=True)
    cases_diff = cleaned_diff(response.cases, yday_c.cases)
    death_diff = cleaned_diff(response.deaths, yday_c.deaths)
    re_diff = cleaned_diff(response.recoveries, yday_c.recoveries)
    active_diff = cleaned_diff(response.active, yday_c.active)
    crit_diff = cleaned_diff(response.critical, yday_c.critical)
    test_diff = cleaned_diff(response.tests, yday_c.tests)
    embedVar.add_field(name='Cases:', value=check_na(response.cases)+cases_diff, inline=True)
    embedVar.add_field(name='Cases Today:', value=check_na(response.today.cases), inline=True)
    embedVar.add_field(name='Deaths:', value=check_na(response.deaths)+death_diff, inline=True)
    embedVar.add_field(name='Deaths Today:', value=check_na(response.today.deaths), inline=True)
    embedVar.add_field(name='Recovered:', value=check_na(response.recoveries)+re_diff, inline=True)
    embedVar.add_field(name='Recovered Today:', value=check_na(response.today.recoveries), inline=True)
    embedVar.add_field(name='Active:', value=check_na(response.active)+active_diff, inline=True)
    embedVar.add_field(name='Critical:', value=check_na(response.critical)+crit_diff, inline=True)
    embedVar.add_field(name='Tests:', value=check_na(response.tests)+test_diff, inline=True)
    embedVar.add_field(name ='Cases per Million', value= response.per_million.cases, inline=True)
    embedVar.add_field(name ='Active per Million', value= response.per_million.active, inline=True)
    embedVar.add_field(name ='Recoveries per Million', value= response.per_million.recoveries, inline=True)
    embedVar.add_field(name ='Tests per Million', value= response.per_million.tests, inline=True)
    embedVar.add_field(name ='Deaths per Million', value= response.per_million.deaths, inline=True)
    embedVar.add_field(name ='Critical per Million', value= response.per_million.critical, inline=True)
    embedVar.add_field(name ='One Case per Person', value= response.per_people.case, inline=True)
    embedVar.add_field(name ='One Death per Person', value= response.per_people.death, inline=True)
    embedVar.add_field(name ='One Test per Person', value= response.per_people.test, inline=True)
    embedVar.add_field(name ='Updated', value= response.updated, inline=True)

    embedVar.set_footer(text="Firelogger#7717",icon_url='https://avatars2.githubusercontent.com/u/37951606?s=460&u=f45b1c7a7f0eddbe0036a7cf79b47d7dfa889321&v=4')
    await ctx.send(embed=embedVar)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" a !cov help in " + str(len(client.guilds)) + " server(s)"))


@client.event
async def on_guild_join(guild):
    for i in guild.text_channels:
        general = i
        if general.permissions_for(guild.me).send_messages:
            embedVar = discord.Embed(title="Corona Tracker Help Panel",
                                     description="Here's some help for you :heart:", color=0x00ff00)
            embedVar.add_field(name="!cov graph [commands]", value="Consists of graphical predictions, analysis , statistics and more see below for command", inline=False)
            embedVar.add_field(name="!cov g [commands]", value="Same as above, use !cov ghelp for list of commands", inline=False)
            embedVar.add_field(name="!cov ghelp", value="Help and commands list for `!cov graph`", inline=False)
            embedVar.add_field(name="!cov all", value="Shows global Covid-19 statistics", inline=False)
            embedVar.add_field(name="!cov interactive", value="Sends the best live interactive maps \n See how the Covid spread on the world map from the very start \n See live status of Covid on the world map \n See Mortality Progression from the very beginning", inline=False)
            embedVar.add_field(name="!cov country {your country} {complete (optional)}",
                               value="Shows you a particular country's stats (Optional- use complete for full report of the country)", inline=False)
            embedVar.add_field(name="!cov help", value="Shows you this message", inline=False)
            embedVar.add_field(name="!cov invite", value="Sends you the links to invite the bot to your own server & the official bot server", inline=False)
            embedVar.add_field(name="github", value="https://github.com/himanshu2406/Corona-Tracker-Bot", inline=False)
            embedVar.add_field(name="tip :heart: ", value="Buy me a Coffee [sends addresses for tipping]", inline=False)
            embedVar.add_field(name="Dev Contact",
                               value="Firelogger#7717", inline=False)
            await general.send(embed=embedVar)
            break
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=" a !cov help in " + str(len(client.guilds)) + " server(s)"))


@client.event
async def on_message(message):
    # do previous on_message stuff here
    if message.guild is None and not message.author.bot:
        dmchannel = client.get_channel(731531934517297266)
        await dmchannel.send(message.author)
        await dmchannel.send(message.content)
    # add at bottom to allow commands to work
    await client.process_commands(message)

client.run(TOKEN)
