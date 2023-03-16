import discord


# The strip on the embed
user_embed = discord.Embed(color=discord.Color.dark_red(), title="test", type='rich')
await channel.send(embed=user_embed, file)