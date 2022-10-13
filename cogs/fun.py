
"""
The Fun Cog!
"""

import discord 
from discord.ext import commands
import urllib
import json
from dadjokes import Dadjoke


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = 'reverse', description = '🔁 esrever')
    async def reverse(self, ctx, *, text):
        text = text[::-1]
        await ctx.respond(text)

    @discord.slash_command(name = 'meme', description = '💀 have a laugh.')
    async def meme(self, ctx):
        memeAPI = urllib.request.urlopen(
            "https://meme-api.herokuapp.com/gimme")
        memedata = json.load(memeAPI)
        memeurl = memedata['url']
        memename = memedata['title']
        memeposter = memedata['author']
        memesub = memedata['subreddit']
        memelink = memedata['postLink']

        embed = discord.Embed(title=memename, url=memelink)
        embed.set_image(url=memeurl)
        embed.set_footer(text=f"Meme by: {memeposter} | Subreddit: {memesub}")

        await ctx.respond(embed=embed)


    @discord.slash_command(name = 'dadjoke', description = '🥸 They never get old, do they?')
    async def dadjoke(self,ctx):
        dadjoke = Dadjoke()
        await ctx.respond(dadjoke.joke)


    @discord.slash_command(name='emojify',  description='⌨️ spam some emojis :P')
    async def emojify(self, ctx, *, text):
        emojis = []
        for s in text.lower():
            if s.isdecimal():
                num2emo = {'0': 'zero', '1': 'one', '2': 'two',
                           '3': 'three', '4': 'four', '5': 'five',
                           '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

                emojis.append(f' :{num2emo.get (s)}: ')
            elif s.isalpha():
                emojis.append(f' :regional_indicator_{s}: ')
            else:
                emojis.append(s)

        await ctx.respond(' '.join(emojis))
        
    @discord.slash_command(name='say',  description='great people say great things')
    async def say(self, ctx, *, quote):
        user = ctx.author.display_name
        await ctx.respond(f'**{quote}**\n\t -{user}')
    

def setup(bot):
    bot.add_cog(Fun(bot))
