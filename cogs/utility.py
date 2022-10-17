"""
Utility Cog
~~~~~~~~~~~~
Cog for the utility commands!
"""

import discord
from discord.ext import commands
import random
import time
import datetime


class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name='webss', description='📸 Get the screenshot of the website, real time.')
    async def ss(self, ctx, link):
        embed = discord.Embed(title="Website Screenshot for: {}".format(link))
        embed.set_image(
            url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{link}")

        await ctx.respond(embed=embed)

    @discord.slash_command(name = 'toss', description = '🪙 Quickly toss a coin, no cheating')
    async def toss(self, ctx):
        sides = ["+heads", "-tails"]
        side = random.choice(sides)
        await ctx.respond(f"```diff\n{side}\n```")

    @discord.slash_command(name = 'timer', description = '⏱️ tick tick tick....')
    async def timer(self, ctx, hour:int, min:int, sec:int, note = None):
        if note is None:
            note = 'beep boop beep, the timer has ended!'
        hour = hour*3600
        min = min*60
        total_seconds = hour+min+sec
        await ctx.respond('*clock turns on*')
        display = await ctx.send(f'Timer started for {hour}:{min}:{sec}')
        while total_seconds > 0:
            timer = datetime.timedelta(seconds=total_seconds)
            print(timer, end="\r")
            await display.edit(content = timer)
            time.sleep(0.7)
            total_seconds -= 1
        await ctx.send(note)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @discord.slash_command(name='simple_interest', description='🧮 Calculate the Simple Interest for an amount and a tenure')
    async def simple_interest(self, ctx, amt: int, time: int, rate: int):
        si = (amt*time*rate)/100
        total = si + amt
        embed = discord.Embed(
            title="Simple Interest Calculator",
            description=f"```yaml\n Principle Amount : {amt}\n Rate of Interest : {rate}\n Tenure : {time} years\n Simple Interest : {si}\n Total Amount : {total}\n```",
        )
        await ctx.respond(embed=embed)
    
    @discord.slash_command(name='compound_interest', description='🧮 Calculate the compound interest!')
    async def ci(self, ctx, amt: int, time: int, rate: int):
        Amount = amt * (pow((1 + rate / 100), time))
        CI = Amount - amt
        CI = round(CI, 3)
        Amount = round(Amount, 3)

        embed = discord.Embed(
            title="Compound Interest Calculator",
            description=f"```yaml\n Principle Amount : {amt}\n Rate of Interest : {rate}\n Tenure : {time} years\n Compound Interest : {CI}\n Total Amount : {Amount}\n```",
        
        )
        await ctx.respond(embed=embed)

    @discord.slash_command(name='roll', description = '🎲 Roll a dice with unlimited faces. 6 if None')
    async def roll(self, ctx, num: int = None):
        try:
            if num == None:
                roll = random.randrange(1, 6)
                await ctx.respond(f"X316 rolls a die, and it lands a **{roll}**")
            else:
                roll = random.randrange(1, num)
                await ctx.respond(f"X316 rolls **{roll}**!")

        except:
            await ctx.respond("Error, check if the number is an integer or not!")

    
    @discord.slash_command(name = 'wordcount', description = '🔠 count the number of words in an input.')
    async def wordcount(self, ctx, input: discord.Option(str, description = 'Text to be counted')):
        input_words = len(input.split())
        embed = discord.Embed(title = 'WordCounter.exe',description = f'```yaml\nWord Count : {input_words}\n```')
        embed.set_footer(text = '💡 Click on your command to see the input')

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
