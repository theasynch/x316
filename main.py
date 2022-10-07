
"""
Kōyō - Utilities and Fun!
~~~~~~~~~~~~~~~~~~~~~~~~~

Just a rather very fun and utile bot for your server!

Made with <3 by theasynch#4400

"""


import discord
import os

client = discord.Bot()

@client.event
async def on_ready():
    print(f"{client.user} is ready and online!")

@client.command(name = 'ping', description = 'pong?')
async def ping(ctx):
    await ctx.respond('Pong! {0}'.format(round(client.latency, 1)))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('MTAyMjgyNjgyMjE3NTU2Nzk3Mg.GlkafH.b3C_N_1Uzg8EsZnK91YtqcBf2xWB_H9vqDvJc8')
