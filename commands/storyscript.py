from nextcord.ext import commands
from StoryScript.storyscript.processor import reset_session, execute as execute_command
from threading import Thread
from traceback import print_exc
from ._utils import generate_command_info_embed
from StoryScript.storyscript.customprint import printing_list

help_embed = generate_command_info_embed(
    "eval {Expression}", "Evaluates a StoryScript expression. (StoryScript version: 0.0.2-preview)",
    [
        ("Expression", "The StoryScript expression you wanted to run.", True)
    ]
)

isFinished = False

def process(commands: list) -> list:
    global out
    global isFinished
    for command in commands:
        try:
            execute_command(command)
        except Exception as e:
            out = ["An error occurred while executing the following command: \n", command, f"Exception: {e}"]
            print_exc()
    isFinished = True

@commands.command(alias=["storyscript"])
async def eval(ctx):
    message = ctx.message
    commands = ((message.content)[6:]).split("\n")
    task = Thread(target=lambda: process(commands), daemon=True)
    task.start()
    out = printing_list
    if len(out) >= 100:
        out = out[0:100]
        out.append("[Reached max 100 lines]")
    out = "\n".join(out)
    if len(out) >= 1850:
        out = out[0:1850]
        out += "\n[Reached max 1850 characters]"
    await message.reply(f"Output: \n```\n{out}\n```")
    reset_session()
