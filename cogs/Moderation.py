from nextcord import Embed, Forbidden, HTTPException
from nextcord.ext import commands
from commands.embed_template import theme_color, permission_denied
from typing import NoReturn

class ModerationModule(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def kick(self, ctx, reason: str) -> NoReturn:
        message = ctx.message
        if not message.author.guild_permissions.kick_members:
            await message.channel.send(embed=permission_denied)
            return
        target = message.mentions
        if not target:
            await message.reply("Hey!, You need to mention the Target user you wanted to kick.")
            return
        target = target[0]
        if target.id == message.author.id:
            await message.reply("Hey!, You can't kick yourself!")
            return
        try:
            if not reason:
                reason = "No reason specified."
            dm = await target.create_dm()
            await dm.send(f"Hi!, You may or may not have been kicked from {message.guild.name}. Note that, If you have the Role higher than the bot, You may haven't been kicked yet.")
            await dm.send(f"Reason: {reason}")
            await target.kick(reason=reason)
            info_embed = Embed(title="Member kicked.", color=theme_color)
            info_embed.add_field(name="Reason", value=reason)
            message.reply(embed=info_embed)
        except Forbidden:
            await message.reply("The bot does not have a Proper permission to kick the target member!")
        except HTTPException:
            await message.reply("The bot failed to kick the Target member!")
    
    @commands.command(alias=["slowmode"])
    async def cooldown(self, ctx, seconds: int):
        message = ctx.message
        if not message.author.guild_permissions.manage_messages:
            await message.channel.send(embed=permission_denied)
            return
        await message.channel.edit(slowmode_delay=int(seconds))
        if seconds == "0":
            await message.channel.send("Successfully disabled channel slowmode!")
            return
        await message.channel.send(f"Slowmode successfully changed to {seconds} seconds!")

def setup(client):
    client.add_cog(ModerationModule(client))
