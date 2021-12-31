from nextcord import Embed, File
from nextcord.ext import commands
from commands.embed_template import theme_color
from commands._utils import generate_command_info_embed
import requests
from PIL import Image, ImageOps
from typing import NoReturn

help_embed = generate_command_info_embed("avatar [Member]", "Gets the avatar of a member.", [
    ("Member", "The target member", False)
])

class ImageModule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx) -> NoReturn:
        message = ctx.message
        member = message.author
        try:
            member = message.mentions[0]
        except IndexError:
            pass
        embed = Embed(color=theme_color)
        embed.set_image(url=str(member.avatar.url))
        embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}")
        await message.channel.send(embed=embed)
    
    @commands.command()
    async def invert(self, ctx) -> NoReturn:
        message = ctx.message
        member = message.mentions
        if not member:
            member = message.author
        else:
            member = member[0]
        msg = await message.channel.send("Processing...")
        req = requests.get(str(member.avatar.url))
        with open("imgs/invertcmd.png", "wb") as f:
            f.write(req.content)
        im = Image.open("imgs/invertcmd.png")
        ImageOps.invert(im.convert("RGB")).save("imgs/invertcmd.png")
        await message.channel.send(file=File("imgs/invertcmd.png"), content="Done!")
        await msg.delete()
    
    @commands.command()
    async def grayscale(self, ctx):
        message = ctx.message
        member = message.mentions
        if not member:
            member = message.author
        else:
            member = member[0]
        msg = await message.channel.send("Processing...")
        req = requests.get(str(member.avatar.url))
        with open("imgs/grayscale.png", "wb") as f:
            f.write(req.content)
        im = Image.open("imgs/grayscale.png")
        im.convert("L").save("imgs/grayscale.png")
        await message.channel.send(file=File("imgs/grayscale.png"), content="Done!")
        await msg.delete()

def setup(client):
    client.add_cog(ImageModule(client))
