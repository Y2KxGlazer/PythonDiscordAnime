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


async def send_rand_local_message(channel):
    """This function gets the channel name and sends a random picture
    from the folder to a discord channel. It also sets the color of the embed
    to the dominant color of the color from the image.

    DOES NOT WORK FOR NON IMAGE TYPE FILES.
     """
    folder_path = r"C:\Users\bmini\Desktop\Pythonic Fluff\PythonDiscordAnime\Photos For Testing"
    file_name = rand.choice(os.listdir(folder_path))
    random_image_path = folder_path + r"\{}".format(file_name)
    with Image.open(random_image_path) as rand_image:
        resized_random_image = rand_image.resize((128, 128))
        arr = io.BytesIO()
        resized_random_image.save(arr, "png")
        arr.seek(0)
    pic_resized_for_embed_color = arr
    pic = discord.File(random_image_path, filename="image.jpg")
    image_color = ColorThief(pic_resized_for_embed_color).get_color(quality=1)
    color_from_image = discord.Color.from_rgb(image_color[0],
                                              image_color[1], image_color[2])
    user_embed = discord.Embed(color=color_from_image, title="test",
                                type='rich')
    user_embed.set_image(url=f"attachment://image.jpg")
    await channel.send(embed=user_embed, file=pic)



