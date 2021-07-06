from discord import Embed, Colour


def datetodatestring(indate):
    return f"{indate.day}/{indate.month}/{indate.year}"


async def execute(message):
    member = message.mentions
    if not member:
        member = message.author
    else:
        member = member[0]
    info_embed = Embed(title=f"an Info about {member}:",
                       color=Colour.from_rgb(0, 255, 180))
    info_embed.set_thumbnail(url=str(member.avatar_url))
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
