import os
from dotenv import load_dotenv

import discord

from server import start_server, stop_server

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.content == '!start':
        # run server
        await message.channel.send('Starting server...')
        data = start_server()
        await message.channel.send(data["message"])
        await message.channel.send(f'{data["ip"]}:25565')
    
    elif message.content == '!stop':
        # stop server
        data = stop_server()
        await message.channel.send(data["message"])

client.run(DISCORD_TOKEN)