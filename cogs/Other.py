from nextcord.ext import commands as ncommands
import commands.help


class OtherModule(ncommands.Cog):
    def __init__(self, client):
        self.client = client
    
    @ncommands.command()
    async def hello(self, ctx):
        await ctx.message.reply('Hello! I\'m PyrumBot! A general moderation utility bot!')
    
    @ncommands.command()
    async def invite(self, ctx):
        await ctx.reply("Use this link!: https://discord.com/oauth2/authorize?client_id=867322458305855519&scope=bot+applications.commands&permissions=8589934591")
    
    @ncommands.command()
    async def help(self, ctx):
        message = ctx.message
        command = message.content.split()
        command[0] = command[0][1:]
        await commands.help.execute(message, command[1:])

def setup(client):
    client.add_cog(OtherModule(client))
