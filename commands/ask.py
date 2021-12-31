from nextcord import Embed
from nextcord.ext import commands
from .embed_template import theme_color
import random
from ._utils import generate_command_info_embed

help_embed = generate_command_info_embed(
    "ask {Question}", "Ask something and I will answer it!.",
    [
        ("Question", "The question you wanted to ask.", True)
    ]
)

possible_values = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",

    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

@commands.command(alias=["8ball"])
async def ask(message, args: list):
    response = Embed(title="Magic 8 ball", color=theme_color)
    response.add_field(name="Your question", value=" ".join(args), inline=False)
    response.add_field(name="Answer", value=random.choice(possible_values), inline=False)
    response.set_footer(
        text=f"Requested by {message.author.name}#{message.author.discriminator}",
        icon_url=str(message.author.avatar.url)
    )
    await message.channel.send(embed=response)
