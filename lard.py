import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import os
from random import randint

client = Bot(description="", command_prefix="-", pm_help = True)
counter = 0
random_text = 0

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))

better_random = random.SystemRandom()


class Reply:
    def __init__(self, message):
        global client
        self.message = message

    def text(self, message, textfile):
        with open(textfile + '.txt') as f:
            quotes = f.readlines()
            quotes = [x.strip() for x in quotes]
        return better_random.choice(quotes)

    def filetype(self, message, path):
        filetype = path + '/'
        random = better_random.choice(os.listdir(filetype))
        filetype += random
        return filetype




@client.event
async def on_message(message):
    global random_text
    global counter
    reply = Reply(message)

    if  message.author == client.user:
        return
    counter += 1

    if random_text == 0:
        random_text = randint(15, 150)

    if counter >= random_text:
        if counter%2 == 0:
            await client.send_message(message.channel, reply.text(message, 'quotes'))
        else:
            await client.send_file(message.channel, reply.filetype(message, 'pics'))
        counter = 0
        random_text = 0

    if message.content.startswith('-gif'):
        await client.send_file(message.channel, reply.filetype(message, 'gifs'))

    if message.content.startswith('-bild'):
        await client.send_file(message.channel, reply.filetype(message, 'pics' ))

    if message.content.startswith('-nsfw'):
        await client.send_file(message.channel, reply.filetype(message, 'nsfw'))

    if message.content.startswith('-zitat'):
        await client.send_message(message.channel, reply.text(message, 'quotes'))

    if message.content.startswith('-frage'):
        await client.send_message(message.channel, reply.text(message, 'questions'))
	
	if message.content.startswith('-stream'):
		await client.send_message(message.channel, reply.text(message, 'stream'))




client.run('Mzg3MTkyNzI5NzU2NzYyMTE2.DQgp6w.1rldO7G6GeYMqwtxRdlwIbrGj-s')
