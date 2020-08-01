import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!cov ')
client.remove_command('help')

client.load_extension('bot')

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