import discord
import os
from keep_alive import keep_alive
import commands.userinfo

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    print(message)
    if not message.content.startswith("~") and not message.content.startswith(
            "~~"):
        return
    
    command = message.content.split()

    if command[0] == "~hello":
        await message.channel.send('Hello! I\'m AurumBot!')
    else:
        await message.channel.send(f"Invalid command! Command \"{command[0][1:]}\" does not exist!")

keep_alive()
client.run(os.environ['TOKEN'])
