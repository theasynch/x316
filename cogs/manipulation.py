import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random
import os

# Extenstion COG for image-manipulation commands.


class Manipulation(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @discord.slash_command(name='acheive', description = '⛏️ Some minecraft aesthetics.')
    async def achievement(self, ctx, *, achievement:discord.Option(str)):
        image = random.choice(range(40))
        achievement = achievement.replace(' ', "+")
        link = f"https://minecraftskinstealer.com/achievement/{image}/Achievement+Get%21/{achievement}"

        embed = discord.Embed(
        )
        embed.set_image(url=link)
        await ctx.respond(embed=embed)

    


def setup(client):
    client.add_cog(Manipulation(client))
