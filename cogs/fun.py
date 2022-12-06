
"""
The Fun Cog!
"""

import discord 
from discord.ext import commands
from discord import Option
import urllib
import json
from dadjokes import Dadjoke
import random
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name = 'reverse', description = '🔁 esrever')
    async def reverse(self, ctx, text:discord.Option(str)):
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
        
    @discord.slash_command(name='say',  description='📜 great people say great things')
    async def say(self, ctx, *, quote):
        user = ctx.author.display_name
        await ctx.respond(f'**{quote}**\n\t -{user}')

    @discord.slash_command(name = 'leetify', description = "|337 c0d3?")
    async def leetify(self, ctx, *, text):
        text = text.lower()
        text = text.replace('a', "4")
        text = text.replace('b', "6")
        text = text.replace('e', "3")
        text = text.replace('g', "9")
        text = text.replace('i', "1")
        text = text.replace('l', "|")
        text = text.replace('o', "0")
        text = text.replace('s', "5")
        text = text.replace('t', "7")
        text = text.replace('z', "2")
        await ctx.respond(text)

    @discord.slash_command(mame = 'greentext', description = '🟢 go green')
    async def greentext(self, ctx, *, text):
        text = f'```json\n"{text}"\n```'
        await ctx.respond(text)
    
    @discord.slash_command(name = 'kill', description = '🔪 more like e-kill.')
    async def kill(self, ctx, member: Option(discord.Member)):
        user = ctx.author
        n = member.display_name
        kill = [f"{n} went on a ride with a lead balloon and eventually fell in the valley.",
                f"{n} ate an apple but it turned out to be made of wax. Someone died of food poisoning later that day.",
                f"{n} was squashed by a storm of cooked chicken.",
                f"{user.display_name} threw a beam of frozen turkey at {n} killing them instantly.",
                f"{user.display_name} tickled {n} to death :skull:",
                f"{n} has a stroke after a sad miserable existence. They are then devoured by their ample cats.",
                f"{user.display_name} cleaves the head of {n} with their keyboard.",
                f"{n} died from doing the icebucket challenge.",
                f"{n} filled up their humidifier with vodka and died of alcohol poisoning",
                f"{user.display_name} turns on Goosebumps [2015] on the T.V, {n} being a scardy cat dies of an heart attack.",
                f"{n} tried to get famous on YouTube by live-streaming something dumb. Skydiving while chained to a fridge.",
                f"{user.display_name} murders {n} with `minecraft.stick` .",
                f"{n} gets trampled under the feet of a baby elephant.",
                f"{user.display_name} bamboozled {n} by killing them with a sharp card."
                f"{user.display_name} made their dog chase behind {n}. {n} died of running for too long. SAD!",
                f"{n} were trying to solve a rubik cube, but their fingers got chiseled... They died of shock.",
                f"{n} were vaporised by an alien that came out from no-where.",
                f"{n} stubbed thier pinky toe finger.",
                f"{n} choked themselves with water. WHAT A SHAME!",
                f"{n}'s brain was hacked by Neuralink.",
                f"{n} listened to thier own recorded voice.",
                f"{n} ate a lego by mistake.",
                f"{n} picked up a grenade, thinking that it was a rotten apple.",
                f"{n} tried to kick a dog, but fell down due to slippery ice, they died instantly. KARMA! Bitch",
                f"{n} were slapped bruttally until they were roasted to death."]


        await ctx.respond(random.choice(kill))

    @discord.slash_command(name = 'mock', description = '🐒 DoNt mOcK mE!')
    async def mock(self, ctx, *, text):
        test_str = text
        res = ""
        for idx in range(len(test_str)):
            if not idx % 2 :
                res = res + test_str[idx].upper()
            else:
                res = res + test_str[idx].lower()
        await ctx.respond(res)

    @discord.slash_command(name = 'hack', description = '💽 your info is now mine :)')
    async def hack(self, ctx, member: Option(discord.Member, description = 'Choose someone to heck.')):

        user = ctx.author.display_name
        user = user.replace(" ",'_')
        email = ["Covid69420@brazzers.com",f"{user}-wissenf*ckedme@beggers.com", "wissenhasabigone@prolongers.com", "iamgae6969@nobanana.com", "nobanana@tiktok.com"]
        passo = ["mineissmall123", "she_says_its_small", "trustno1", "i_love_my_mommy", "i_miss_banana", "phallic_is_too_large", "nope.", "1234567890", "i_cant_speak_english"]
        rand = random.choice(email)
        ips = ["179.156.92.62", "222.28.40.75","179.178.3.75","43.211.138.85","143.194.250.58","85.218.229.27","186.156.166.202","38.154.43.115","35.255.211.6","93.207.1.121","172.211.91.242","6.234.184.21","180.58.149.178","136.37.111.144","16.223.41.163","158.9.12.216","223.42.58.12","230.99.0.222","198.3.172.240"]

        await ctx.respond('<x316.cmd. exe object at 0x000001B24CD93FD0>')
        message = await ctx.send("Okay, setting up variable `IP Adress`")
        await asyncio.sleep(2)
        await message.edit(content="[▘]Okay, setting up variable `IP Adress`")
        await asyncio.sleep(2)
        await message.edit(content="[▝]Okay, setting up variable `IP Adress`")
        await asyncio.sleep(2)
        await message.edit(content="√ IP is now variable.")
        await asyncio.sleep(2)
        await message.edit(content=f"IP adress found: `{random.choice(ips)}`")
        await asyncio.sleep(2)
        await message.edit(content="[▘]Now, hacking users email.")
        await asyncio.sleep(2)
        await message.edit(content=f"Email: {rand}")
        await asyncio.sleep(3)
        await message.edit(content=f"Password: {random.choice(passo)}")
        await asyncio.sleep(3)
        await message.edit(content=f"[▝]Hacking discord")
        await asyncio.sleep(2)
        await message.edit(content="[▖]Hacking discord. **2FA bypassed**")
        await asyncio.sleep(2)
        await message.edit(content="√ Discord account hacked!")
        await asyncio.sleep(2)
        await message.edit(content="[▘]Fetching friend list (if there are any)")
        await asyncio.sleep(2)
        await message.edit(content=f"Affirmative. No friends for discriminator `#{member.discriminator}`.")
        await asyncio.sleep(3)
        await message.edit(content=f"Now finding the most common word used in the **server that {member} should not be in**")
        await asyncio.sleep(5)
        await message.edit(content=f"Most common word: `small`")
        await asyncio.sleep(2)
        await message.edit(content=f"Latest DM: `I think it is smaller than most.`")
        await asyncio.sleep(2)
        await message.edit(content=f"[▖]Hacking onlyfans account.")
        await asyncio.sleep(2)
        await message.edit(content=f"[▘]Hacking onlyfans account.")
        await asyncio.sleep(2)
        await message.edit(content=f"√onlyfans account hacked.")
        await asyncio.sleep(2)
        await message.edit(content=f"Selling this data to the government.")
        await asyncio.sleep(2)
        await message.edit(content=f"Finished hacking {member}")

        await ctx.respond("Completely different from Dank Memer and dangerous hack was complete!")



def setup(bot):
    bot.add_cog(Fun(bot))
