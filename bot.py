# -*- coding: utf-8 -*-

import discord
import os
from PDBot import PDBot
from dotenv import load_dotenv

# Get discord token from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Creating discord client
client = discord.Client()

# Command list
commands = ['ping',
            'protimg']

# Function to get command parameters
def format_command(message):
    message = message.split(' ')
    command = message[0].replace('!','')
    
    if len(message) > 1:
        parameters = message[1:]
    else:
        parameters = False

    return command, parameters

@client.event
async def on_ready():
    print('PDBot has connected to Discord!')

@client.event
async def on_message(message):
    # Only respond to message that starts with "!"
    if message.content.startswith('!'):
        command, parameters = format_command(message.content)
        if command in commands:
            if command == 'ping':
                await message.channel.send('pong!')
            if command == 'protimg':
                if parameters:
                    pdbot = PDBot()
                    try:
                        mymsg = await message.channel.send('Pesquisando imagem da proteína {} no PDB...'.format(parameters[0].upper()))
                        img_url = pdbot.get_protein_img(parameters[0])
                    except:
                        print('An error occour during get image process.')
                    await mymsg.delete()
                    await message.channel.send(img_url)
                else:
                    print('Error: One parameter required got none.')
        else:
            print('Command not found.')

client.run(TOKEN)