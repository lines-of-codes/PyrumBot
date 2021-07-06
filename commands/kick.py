from commands.embed_template import permission_denied
from discord import Forbidden, HTTPException


async def execute(message, args):
    if not message.author.guild_permissions.kick_members:
        await message.channel.send(embed=permission_denied)
        return
    target = message.mentions
    if not target:
        await message.channel.send("Hey!, You need to mention the Target user you wanted to kick.")
        return
    target = target[0]
    try:
        reason = " ".join(args[1:])
        if not reason:
            reason = "No reason specified."
        dm = await target.create_dm()
        await dm.send(f"Hi!, You may or may not have been kicked from {message.guild.name}. Note that, If you have the Role higher than the bot, You may haven't been kicked yet.")
        await dm.send(f"Reason: {reason}")
        await target.kick(reason=reason)
    except Forbidden:
        await message.channel.send("The bot does not have a Proper permission to kick the target member!")
    except HTTPException:
        await message.channel.send("The bot failed to kick the Target member!")
