from nextcord import Embed
from .embed_template import theme_color

def generate_command_info_embed(command_name: str, description: str, arguments: list) -> Embed:
    info_embed = Embed(title=command_name, description=description, color=theme_color)
    for v, desc, required in arguments:
        if required:
            info_embed.add_field(name=v, value=desc)
        else:
            info_embed.add_field(name=f"{v} (Optional)", value=desc)
    return info_embed