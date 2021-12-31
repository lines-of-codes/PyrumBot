from nextcord import Embed
from nextcord.ext import commands
from commands.embed_template import theme_color, permission_denied_color


class EmoteModule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def addemote(self, ctx, name, url):
        pass
    
    @commands.command()
    async def removeemote(self, ctx, name):
        pass


def setup(client):
    client.add_cog(EmoteModule(client))
