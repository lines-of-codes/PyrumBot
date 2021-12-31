from nextcord import Embed, Colour

permission_denied_color: Colour = Colour.from_rgb(64, 256, 64)
permission_denied: Embed = Embed(
	title="Permission denied",
    color=permission_denied_color
)

theme_color: Colour = Colour.from_rgb(0, 255, 128)
