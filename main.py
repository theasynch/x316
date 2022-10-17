
"""
X316 - Utilities and Fun!
~~~~~~~~~~~~~~~~~~~~~~~~~

Just a rather very fun and utile bot for your server!

Made with <3 by theasynch#4400

"""


import discord
from pypresence import Presence
import os
from discord.ext import tasks
from itertools import cycle

client = discord.Bot()
status = cycle(['the gears turn','the invite button', 'the kids play', 'Interstellar',
                 'Breaking Bad', 'KIC 9832227', 'the stars ✨', 'you watching this :P',])


@client.event
async def on_ready():

    print(client)
    print(f"{client.user} is ready and online!")
    change_status.start()

@tasks.loop(seconds=6)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))


@client.command(name='ping', description='📍 pong?')
async def ping(ctx):
    await ctx.respond('Pong! {0}'.format(round(client.latency, 1)))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('MTAyMjgyNjgyMjE3NTU2Nzk3Mg.G2njuS.QKydTT__RWaFOKEBqF6mM3OL1HXnXwe2c2yqeA')
