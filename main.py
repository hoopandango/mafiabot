import discord
from roleManagement import * 

client = discord.Client()
JAILOR_CHAT = 796787913471295548
JAILED_CHAT = 796787933587439656
BOOKMARKS = 796787874451685407


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: # Doesn't respond to self
        return

    if message.content.startswith('-cleanjail') and message.author.name == "Pandango":
        if message.channel == client.get_channel(JAILOR_CHAT):
            msgs = []
            async for msg in client.get_channel(JAILED_CHAT).history(limit=100):
                msgs.append(msg)
            await client.get_channel(JAILED_CHAT).delete_messages(msgs)
            await client.get_channel(JAILOR_CHAT).send("All messages in jailed chat cleaned.")
            
    elif message.channel == client.get_channel(JAILOR_CHAT):
        await client.get_channel(JAILED_CHAT).send("Jailor: "+message.content)

    elif message.channel == client.get_channel(JAILED_CHAT):
        await client.get_channel(JAILOR_CHAT).send(message.author.name+": "+message.content)

    if message.content.startswith('-cleanbm') and message.author.name == "Pandango":
        msgs = []
        async for msg in client.get_channel(BOOKMARKS).history(limit=100):
            msgs.append(msg)
        await client.get_channel(BOOKMARKS).delete_messages(msgs)
        await message.channel.send("All bookmarks cleaned.")

    elif message.content.startswith('-test'):
        await message.channel.send('Hail Homucifer!')

    elif message.content.startswith('-start'):
        await message.channel.send(playersStatus())

    elif message.content.startswith('-roles'):
        await message.channel.send(printRolelist())
    
    elif message.content.startswith('-add'):
        await message.channel.send(addPlayer(message.content[5:])+" Players added")
        
    elif message.content.startswith('-pcount'):
        n = int(message.content[8:])
        setPlayercount(n)
        await message.channel.send("Player count is now "+str(n))

    elif message.content.startswith('-print'):
        await message.channel.send(printRolelist())

    elif message.content.startswith('-rolelist'):
        await message.channel.send(getRolelist())

    elif message.content.startswith('-default'):
        setDefaultPlayers()
        await message.channel.send("Default players added")

    elif message.content.startswith('-bm'):
        async for msg in message.channel.history(limit=5):
            if msg.author == client.user:
                await client.get_channel(BOOKMARKS).send(msg.content)
                return 

    elif message.content.startswith('-plist'):
        await message.channel.send(getPlayers())

    elif message.content.startswith('-rig'):
        msg = message.content[5:].split(',')
        await message.channel.send(rig(int(msg[0]),msg[1]))

    elif message.content.startswith('-swap'):
        msg = message.content[6:].split(',')
        await message.channel.send(swap(int(msg[0]),int(msg[1])))

    elif message.content.startswith('-sort'):
        await message.channel.send(sort())

    
client.run('<token goes here>')
