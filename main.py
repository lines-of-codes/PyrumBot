import nextcord.ext.commands
import os
from keep_alive import keep_alive


client = nextcord.ext.commands.Bot(status="Listening for -help...", command_prefix="-", case_insensitive=True, help_command=None)


@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
client.run(os.environ['TOK'])
