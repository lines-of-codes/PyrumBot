from nextcord import Embed
from nextcord.ext import commands
from commands.embed_template import theme_color
from ._utils import generate_command_info_embed

help_embed = generate_command_info_embed(
    "serverinfo", "Find an Information about the Server.", []
)

@commands.command()
async def serverinfo(message):
    guild = message.guild
    if not guild:
        await message.channel.send("Looks like the message you sent is not in a Discord Server (Guilds)!")
        return
    info_embed = Embed(title="Server info", description="Information about the current server (guild).", color=theme_color)
    info_embed.add_field(name="Guild name", value=guild.name)
    info_embed.add_field(name="Channel count", value=str(len(guild.channels)))
    info_embed.add_field(name="Voice channels", value=str(len(guild.voice_channels)))
    if len(guild.stage_channels) != 0:
        info_embed.add_field(name="Stage channels", value=str(len(guild.stage_channels)))
    info_embed.add_field(name="Text channels", value=str(len(guild.text_channels)))
    info_embed.add_field(name="Is server large (>50 members)", value=str(guild.large))
    info_embed.add_field(name="Emoji count", value=str(len(guild.emojis)))
    info_embed.add_field(name="Server region", value=str(guild.region))
    info_embed.add_field(name="Roles count", value=str(len(guild.roles)))
    info_embed.add_field(name="Filesize limit", value=f"{guild.filesize_limit / 1e+6}mb")
    info_embed.add_field(name="Verification level", value=str(guild.verification_level))
    info_embed.add_field(name="Boosts count", value=str(guild.premium_subscription_count))
    info_embed.add_field(name="Nitro tier", value=str(guild.premium_tier))
    info_embed.set_thumbnail(url=str(guild.icon_url))

    await message.channel.send(embed=info_embed)