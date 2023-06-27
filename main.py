import os
import discord
from discord import app_commands

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
GUILD_ID = int(os.environ["KAMAKIRI_GUILD_ID"])

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message: discord.Message):
    guild = client.get_guild(GUILD_ID)
    testbot_channel = discord.utils.get(guild.text_channels, name="testbot")
    if message.channel == testbot_channel and message.content == "hello":
        await testbot_channel.send('Hello!')

@client.event
async def on_ready():
    print('login')
    await tree.sync()

@tree.command(name="cat", description="ﾈｺﾁｬﾝ")
async def cat_command(ctx: discord.Interaction):
    await ctx.response.send_message("ﾈｺﾁｬﾝ!", file=discord.File("neco.jpg"))

client.run(TOKEN)
print("logout")
