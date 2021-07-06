import discord
import os
from keep_alive import keep_alive
import commands.userinfo
import commands.ban
import commands.kick
import commands.help

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.content.startswith("-"):
        return

    command = message.content.split()
    command[0] = command[0][1:]

    if command[0] == "hello":
        await message.channel.send(
            'Hello! I\'m PyrumBot! AurumBot But Python edition.')
    elif command[0] == "userinfo":
        await commands.userinfo.execute(message)
    elif command[0] == "warn":
        pass
    elif command[0] == "mute":
        pass
    elif command[0] == "kick":
        await commands.kick.execute(message, command[1:])
    elif command[0] == "ban":
        await commands.ban.execute(message)
    elif command[0] == "help":
        await command.help.execute(message)
    else:
        await message.channel.send(
            f"Invalid command! Command \"{command[0]}\" does not exist!")


keep_alive()
client.run(os.environ['TOK'])
