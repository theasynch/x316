
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
        embed = discord.Embed(
            title='About the Developer...',
            description='Hey there! I am [theasynch](https://discord.com/users/692295384868978710). I really like to socialize and learn new skills! \nYou can reach out to me via the below links'
        )
        embed.add_field(
            name='🔗__Social Handles__',
            value='[`Linktree`](https://linktr.ee/the.asynchronus)\n[`GitHub`](https://github.com/theasynchronus)\n[`Instagram`](https://instagram.com/theasynch)\n[`Twitter`](https://twitter.com/)'
        )
        embed.add_field(
            name='__Servers__',
            value='[`The Dank Camp`](https://discord.com/invite/6Eru3ebqah)\n[`8 - Bit Arcade`](https://discord.gg/SrVTQsFaWX)'
        )
        embed.set_author(name = 'theasynch#4400',icon_url='https://cdn.discordapp.com/avatars/692295384868978710/4f3725e0d53a5ced8f153ce38aa50ca6.webp')
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))