from nextcord import Embed, Colour
from nextcord.ext import commands
from ._utils import generate_command_info_embed

help_embed = generate_command_info_embed(
    "userinfo [Member]", "Find an Information about the Member.",
    [
        ("Member", "The target member.", False)
    ]
)

def datetodatestring(indate):
    return f"{indate.day}/{indate.month}/{indate.year}"


@commands.command()
async def userinfo(message):
    member = message.mentions
    if not member:
        member = message.author
    else:
        member = member[0]
    info_embed = Embed(title=f"Some Info about {member}:",
                       color=Colour.from_rgb(0, 255, 180))
    info_embed.set_thumbnail(url=str(member.avatar.url))
    info_embed.add_field(name="Username", value=str(member), inline=True)
    info_embed.add_field(name="User ID", value=str(member.id))
    if message.author.nick != None:
        info_embed.add_field(name="Nickname", value=member.nick)
    if message.author.joined_at != None:
        info_embed.add_field(name="Joined at",
                             value=datetodatestring(member.joined_at))
    if message.author.created_at != None:
        info_embed.add_field(name="Created at",
                             value=datetodatestring(member.created_at))
    info_embed.set_footer(text="Note: All dates are formatted in dd/mm/yyyy.")

    await message.channel.send(embed=info_embed)
