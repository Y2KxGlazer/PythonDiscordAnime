import discord
from discord.ext import commands


import asyncio

import Embed

intents=discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

with open("token.txt") as f:
    TOKEN = f.readline().strip()

folder_path = ""
@bot.event
async def on_ready():
    awaken_channel =   # This is the channel that the bot 'awakens' in ( Right-Click Channel -> Copy Channel ID)
    print('Logged in as {0.user}'.format(bot))
    channel = bot.get_channel(awaken_channel)
    await channel.send(f'Hello, world!')



@bot.event
async def on_message(message):
    msg_channel = message.channel
    if message.author.name == "Test" and message.author.discriminator == "1234":

        if msg_channel.id != : # Enter Valid channels
            await msg_channel.send("Nope")

        else:
            await Embed.send_rand_local_message(msg_channel)
            # Lower the resolution of image so color theif can work faster




        #TODO: set up bot prefix..... skipping


        #TODO: Input MAL

        #TODO: Get anime pic from MAL



bot.run(TOKEN)
