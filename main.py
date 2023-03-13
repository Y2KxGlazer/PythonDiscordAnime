import discord
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

with open("token.txt") as f:
    TOKEN = f.readline().strip()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    channel = client.get_channel(1055616703880503328) # This is the channel that the bot 'awakens' in
    await channel.send('Hello, world!')




@client.event
async def on_message(message):
    pathToFile = discord.File(r"C:\Users\bmini\Desktop\Pythonic Fluff\PythonDiscordAnime\Photos For Testing\animelovesauce_After_a_long_journey_my_feet_smells_a_lot__Huh__You_wanna_take_a_sniff__Really__Well,_if_you_like_stinky_feet_you_can,_but_do_it_well__(Elaina)_[Majo_no_Tabitabi]_koeio8.jpg", filename="image.jpg")


    print("Contents: {}, From:{}".format(message.content, message.author))
    if message.author.name == "George Orwell" and message.author.discriminator == "3046":
        msgChannel = message.channel
        await msgChannel.send("nice", file=pathToFile)

        #TODO: send image

        #TODO: embed image

        #TODO: Input MAL

        #TODO: Get anime pic from MAL







client.run(TOKEN)
