import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import os

client = Bot(description="", command_prefix="-", pm_help = True)


@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

@client.event
async def on_message(message):
    if message.content.startswith('-bild'):
        bild='lardpics/'
        randombild = random.choice(os.listdir(bild))
        bild += randombild
        await client.send_file(message.channel, bild)
		
	if message.content.startswith('-nsfw'):
        bild='lardpics-nsfw/'
        randombild = random.choice(os.listdir(bild))
        bild += randombild
        await client.send_file(message.channel, bild)

    if message.content.startswith('-zitat'):
        with open('lard.txt') as f:
            quotes = f.readlines()
            quotes = [x.strip() for x in quotes]
        await client.send_message(message.channel, random.choice(quotes))

client.run('Mzg3MTkyNzI5NzU2NzYyMTE2.DQgp6w.1rldO7G6GeYMqwtxRdlwIbrGj-s')
