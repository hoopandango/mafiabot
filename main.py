import discord
from roleManagement import * 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&test'):
        await message.channel.send('Hail Homucifer!')

    elif message.content.startswith('&start'):
        await message.channel.send(playersStatus())
    
    elif message.content.startswith('&add'):
        await addPlayer(message.content[5:])
        
    elif message.content.startswith('&pcount'):
        setPlayercount(int(message.content[8:]))

    elif message.content.startswith('&default'):
        setDefaultPlayers()

    
client.run('<token goes here>')
