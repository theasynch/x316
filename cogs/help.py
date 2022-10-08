
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @discord.slash_command(name='about', description='About the developer!')
    async def about(self, ctx):
        embed = discord.Embed(
            title='theasynch#4400',
            url='https://discord.com/users/692295384868978710',
            description='Hey there! Greetings! I am theasynch. You can call me `asy`, nonetheless.\n I really like to socialize and learn new skills! \n You can reach out to me via the below links'
        )
        embed.add_field(
            name='Socials',
            value='[`Linktree`](https://link.tree.com)\n[`Instagram`](https://instagram.com/theasynch)\n[`Twitter`](https://twitter.com/)'
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/692295384868978710/4f3725e0d53a5ced8f153ce38aa50ca6.webp')
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))