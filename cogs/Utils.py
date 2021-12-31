from nextcord.ext import commands
from typing import NoReturn

class UtilsModule(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(alias=["tobin"])
    async def binary(self, ctx, number: int) -> NoReturn:
        message = ctx.message
        try:
            out = str(bin(int(number)))
            await message.reply(f"Result: {out}")
        except ValueError as e:
            await message.reply(f"An exception occurred: {e}\n__**What does this exception mean**__\nThis mean you've input the wrong type of the data to convert.")
    
    @commands.command()
    async def round(self, ctx, number: float) -> NoReturn:
        await ctx.message.reply(f"Result: {round(float(number))}")

def setup(client):
    client.add_cog(UtilsModule(client))
