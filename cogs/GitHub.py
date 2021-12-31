from nextcord import Embed
from nextcord.ext import commands
from commands.embed_template import theme_color, permission_denied_color
import requests
from typing import NoReturn
import json

class GitHubModule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def getrepo(self, ctx, repo):
        message = ctx.message
        response = json.loads(requests.get(f"https://api.github.com/repos/{repo}").content)
        if response.get("message") == "Not Found":
            await message.reply(embed=Embed(title=f"Repository {repo} not found ;-;", color=permission_denied_color))
            return
        response_embed = Embed(title=repo, color=theme_color, url=f"https://github.com/{repo}")
        response_embed.add_field(name="Stargazers", value=response["stargazers_count"])
        response_embed.add_field(name="Language", value=response["language"])
        response_embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}")
        await message.reply(embed=response_embed)
    
    @commands.command()
    async def listorgrepo(self, ctx, org) -> NoReturn:
        message = ctx.message
        response = json.loads(requests.get(f"https://api.github.com/orgs/{org}/repos").content)
        if isinstance(response, dict) and response.get("message") == "Not Found":
            await message.reply(embed=Embed(title=f"Organization {org} not found ;-;", color=permission_denied_color))
            return
        response_embed = Embed(title=f"{org} repositories", color=theme_color, url=f"https://github.com/{org}")
        for i in response:
            response_embed.add_field(name=i["name"], value=i["description"])
        await message.reply(embed=response_embed)
    
    @commands.command()
    async def listrepo(self, ctx, user):
        message = ctx.message
        response = json.loads(requests.get(f"https://api.github.com/users/{user}/repos").content)
        if isinstance(response, dict) and response.get("message") == "Not Found":
            await message.reply(embed=Embed(title=f"Organization {user} not found ;-;", color=permission_denied_color))
            return
        response_embed = Embed(title=f"{user} repositories", color=theme_color, url=f"https://github.com/{user}")
        for i in response:
            response_embed.add_field(name=i["name"], value=i["description"])
        await message.reply(embed=response_embed)

def setup(client):
    client.add_cog(GitHubModule(client))
