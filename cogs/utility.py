"""
Utility Cog
~~~~~~~~
Cog for the utility commands!
"""

import discord
from discord.ext import commands


class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='webss', description='Get the screenshot of the website, real time.')
    async def ss(self, ctx, link):
        embed = discord.Embed(title="Website Screenshot for: {}".format(link))
        embed.set_image(
            url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{link}")

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))
