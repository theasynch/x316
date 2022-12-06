
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

    

    @discord.slash_command(name='about', description='💡 About the developer!')
    async def about(self, ctx):
        i = await self.bot.application_info()
        member = i.owner
        embed = discord.Embed(
            title='About the Developer...',
            url='https://discord.com/users/692295384868978710',
            description='> *To be, not to be* \n\n Just a fancy guy who likes minimalism and doing stuff.'
        )
        embed.add_field(
            name='__Social Handles__',
            value='`-`[Linktree](https://linktr.ee/the.asynchronus)\n`-`[GitHub](https://github.com/theasynchronus)\n`-`[Instagram](https://instagram.com/theasynch)\n`-`[Twitter](https://twitter.com/asynced1603)'
        )
        embed.add_field(
            name='__Servers__',
            value='`-`[The Dank Camp](https://discord.com/invite/6Eru3ebqah)\n`-`[8 - Bit Arcade](https://discord.gg/SrVTQsFaWX)'
        )
        embed.set_author(name = 'theasynch#4400')
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))