import discord
from discord.ext import commands
import os, random as rand
from colorthief import ColorThief
import asyncio


intents=discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

with open("token.txt") as f:
    TOKEN = f.readline().strip()

folder_path = ""
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
            pic = discord.File(random_image_path, filename="image.jpg")

            color_thief_image = ColorThief(random_image_path)
            image_color = color_thief_image.get_color(quality=1)
            color_from_image = discord.Color.from_rgb(image_color[0], image_color[1], image_color[2])

            user_embed = discord.Embed(color=color_from_image, title="test",
                                       type='rich')
            user_embed.set_image(url=f"attachment://image.jpg")
            await msg_channel.send(embed=user_embed, file=pic)


        #TODO: set up bot prefix..... skipping


        #TODO: Input MAL

        #TODO: Get anime pic from MAL



bot.run(TOKEN)
