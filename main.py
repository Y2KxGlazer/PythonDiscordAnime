import discord
from discord.ext import commands
import os, random as rand
import asyncio


intents=discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

with open("token.txt") as f:
    TOKEN = f.readline().strip()


@bot.event
async def on_ready():
    awaken_channel = 1055616703880503328  # This is the channel that the bot 'awakens' in
    print('Logged in as {0.user}'.format(bot))
    channel = bot.get_channel(awaken_channel)
    await channel.send(f'Hello, world!')



@bot.event
async def on_message(message):
    if message.author.name == "George Orwell" and message.author.discriminator == "3046":
        msg_channel = message.channel
        if msg_channel.id != 1055616703880503328:
            await msg_channel.send("Nope")

        else:
            folder_path = r"C:\Users\bmini\Desktop\Pythonic Fluff\PythonDiscordAnime\Photos For Testing"
            file_name = rand.choice(os.listdir(folder_path))
            random_image_path = folder_path + r"\{}".format(file_name)
            pic = discord.File(random_image_path)

            await msg_channel.send("nice", file=pic)

        #TODO: set up bot prefix..... skipping

        #TODO: embed image

        #TODO: Input MAL

        #TODO: Get anime pic from MAL



bot.run(TOKEN)
