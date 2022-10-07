
"""
Help Cog
~~~~~~~~
Cog for all the help and manuals needed for the bot
"""

import discord
from discord.ext import commands
import random

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = 'help', description = "Stop it, get some help:')")
    async def help(self, ctx):
        user = ctx.author
        embed = discord.Embed(
            description = "[`Invite Me!`](https://your0bot-link-here) | [`Support Server`](https://support-server-link)",
            colour = discord.Color.random()
        )
        await ctx.respond(embed = embed)

def setup(bot):
    bot.add_cog(Help(bot))