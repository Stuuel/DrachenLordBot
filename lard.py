import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import os
from random import randint

client = Bot(description="", command_prefix="-", pm_help = True)


@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

better_random = random.SystemRandom()

@client.event
async def on_message(message):
    if message.content.startswith('-bild'):
        bild = 'lardpics/'
        randombild = better_random.choice(os.listdir(bild))
        bild += randombild
        await client.send_file(message.channel, bild)

    if message.content.startswith('-nsfw'):
        nsfw = 'lardpics-nsfw/'
        randomnsfw = better_random.choice(os.listdir(nsfw))
        nsfw += randomnsfw
        await client.send_file(message.channel, nsfw)

    if message.content.startswith('-zitat'):
        with open('lard.txt') as f:
            quotes = f.readlines()
            quotes = [x.strip() for x in quotes]
        await client.send_message(message.channel, better_random.choice(quotes))
        
    if message.content.startswith('-frage'):
        with open('frage.txt') as f:
            quotes = f.readlines()
            quotes = [x.strip() for x in quotes]
        await client.send_message(message.channel, better_random.choice(quotes))

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='387184662906404864')
    while not client.is_closed:
        bildquote = randint(0,40)
        if bildquote > 10:
            with open('lard.txt') as f:
                quotes = f.readlines()
                quotes = [x.strip() for x in quotes]
                await client.send_message(channel, better_random.choice(quotes))
        #else:
        #    bild = 'lardpics/'
        #    randombild = better_random.choice(os.listdir(bild))
        #    bild += randombild
        #    await client.send_file(channel, bild)

        await asyncio.sleep(randint(0,10)) 

client.loop.create_task(my_background_task())

client.run('Mzg3MjI4MDA5Nzc5ODIyNTky.DQbxmg.I3fSZb6GhxpLU85SxHhShd-ihwg')
