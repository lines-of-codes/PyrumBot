async def execute(message, args: list):
    try:
        args[0]
    except IndexError:
        await message.channel.send("You need to provide the emote name!")
    try:
        args[1]
    except IndexError:
        await message.channel.send("You need to provide the link to the image!")
    
    
