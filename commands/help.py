from commands.embed_template import theme_color
from nextcord import Embed
from typing import NoReturn
from . import serverinfo, storyscript, userinfo, ask
from ._utils import generate_command_info_embed

INFO_EMBEDS = {
    "userinfo": userinfo.help_embed,
    "help": generate_command_info_embed(
        "help [command]", "Find an Information about commands.",
        [
            ("command", "The command you wanted to get the Description.", False)
        ]
    ),
    "kick": generate_command_info_embed(
        "kick {Member} [Reason]", "Kick a Member.",
        [
            ("Member", "The target member", True),
            ("Reason", "The reason of the kick.", False)
        ]
    ),
    "ban": generate_command_info_embed(
        "ban {Member} [Reason kek]", "Ban a Member.",
        [
            ("Member", "The target member", True),
            ("Reason", "The reason of the ban.", False)
        ]
    ),
    "serverinfo": serverinfo.help_embed,
    "eval": storyscript.help_embed,
    "invite": generate_command_info_embed(
        "invite", "Get the bot invite",
        []
    ),
    "utility": generate_command_info_embed(
        "Utility", "Utility commands",
        [
            ("tobin {number}", "Converts an Integer (Whole number) into Binary.", True),
            ("round {number}", "Round a Number.", True)
        ]
    ),
    "github": generate_command_info_embed(
        "GitHub commands", "GitHub related commands",
        [
            ("getrepo {repository}", "Get an information about a GitHub repository", True),
            ("listorgrepo {organization}", "List an organization repositories", True),
            ("listrepo {user}", "List a user repositories", True)
        ]
    ),
    "getrepo": generate_command_info_embed(
        "getrepo {repository}", "Get an Information about a GitHub repository",
        [
            ("repository", "The target repository", True)
        ]
    ),
    "listorgrepo": generate_command_info_embed(
        "listorgrepo {organization}", "List an organization repositories",
        [
            ("organization", "The target organization", True)
        ]
    ),
    "listrepo": generate_command_info_embed(
        "listrepo {user}", "List a user repositories",
        [
            ("user", "The target user", True)
        ]
    ),
    "moderation": generate_command_info_embed(
        "Moderation", "Moderation commands",
        [
            ("kick {user} [reason]", "Kick a user.", True),
            ("ban {user} [reason]", "Ban a user.", True),
            ("cooldown {seconds}", "Set the channel cooldown on the current channel.", True)
        ]
    ),
    "cooldown": generate_command_info_embed(
        "cooldown {seconds}", "Set the current channel cooldown.",
        [
            ("seconds", "Number of seconds you wanted to set the cooldown to.", True)
        ]
    ),
    "ask": ask.help_embed,
    "image": generate_command_info_embed(
        "Image", "The image module.",
        [
            ("avatar", "Gets the avatar of a member.", True)
        ]
    )
}

async def execute(message, args: list) -> NoReturn:
    if not args:
        help_embed = Embed(title="Help", description=" Information about commands.", color=theme_color)
        help_embed.add_field(name="-help [Command]", value="a Help command.")
        help_embed.add_field(name="-userinfo [Member]", value="View an Information about a User.")
        help_embed.add_field(name="-serverinfo", value="View an Information about this server.")
        help_embed.add_field(name="-eval {Expression}", value="Evaluates a StoryScript expression.")
        help_embed.add_field(name="-invite", value="Get the bot invite!")
        help_embed.add_field(name="-ask {Question}", value="Ask something and I will answer it!")
        help_embed.add_field(name="Moderation", value="Moderation commands. Type `-help moderation` for more info.")
        help_embed.add_field(name="Utility", value="Type `-help utility` for more info.")
        help_embed.add_field(name="GitHub", value="Geethoob related commands. Type `-help github` for more info.")
        help_embed.add_field(name="Image", value="A module about images. Type `-help image` for more info.")
        await message.reply(embed=help_embed)
    else:
        embed = INFO_EMBEDS.get(args[0].lower())
        if embed is None:
            await message.channel.send("Unknown command! Did you misspelled something?")
            return
        await message.reply(embed=embed)
