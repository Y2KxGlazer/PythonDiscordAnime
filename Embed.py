import io
import os, random as rand
import discord
from colorthief import ColorThief
from PIL import Image

# Embed builder module


def embed_builder():
    pass


def send_embed_message():
    pass


def send_rand_local_message():
    folder_path = r"C:\Users\bmini\Desktop\Pythonic Fluff\PythonDiscordAnime\Photos For Testing"
    file_name = rand.choice(os.listdir(folder_path))
    random_image_path = folder_path + r"\{}".format(file_name)

    with Image.open(random_image_path) as rand_image:
        resized_random_image = rand_image.resize((256, 256))
        arr = io.BytesIO()
        resized_random_image.save(arr)
        arr.seek(0)

    pic = discord.File(arr, filename="image.jpg")


    image_color = color_thief_image.get_color(quality=1)
    color_from_image = discord.Color.from_rgb(image_color[0], image_color[1], image_color[2])

    user_embed = discord.Embed(color=color_from_image, title="test",
                               type='rich')
    user_embed.set_image(url=f"attachment://image.jpg")
    await msg_channel.send(embed=user_embed, file=pic)

#Todo get the most dominate color for the color in

# If you move this to the main.py it'll send a embed