import discord
import os, random as rand
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
@client.event
async def on_message(message):

    print("Contents: {}, From:{}".format(message.content, message.author))
    if message.author.name == "George Orwell" and message.author.discriminator == "3046":
        msgChannel = message.channel
        print(msgChannel)
        if msgChannel.id != 1055616703880503328:
            await msgChannel.send("Nope")
        else:
            folder_path = r"C:\Users\bmini\Desktop\Pythonic Fluff\PythonDiscordAnime\Photos For Testing"
            file_name = rand.choice(os.listdir(folder_path))
            random_image_path = folder_path + r"\{}".format(file_name)
            pic = discord.File(random_image_path)
            await msgChannel.send("nice", file=pic)

        #TODO: send image

        #TODO: embed image

        #TODO: Input MAL

        #TODO: Get anime pic from MAL







client.run(TOKEN)
