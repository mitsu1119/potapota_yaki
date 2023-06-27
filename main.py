import os
import discord

TOKEN = os.environ["DISCORD_BOT_TOKEN"]
GUILD_ID = int(os.environ["KAMAKIRI_GUILD_ID"])
# channel_testbot = os.environ['DISCORD_CHANNEL_TESTBOT']

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)

guild = ""
testbot_channel = ""

@client.event
async def on_ready():
    print('login')

@client.event
async def on_message(message):
    guild = client.get_guild(GUILD_ID)
    testbot_channel = discord.utils.get(guild.text_channels, name="testbot")
    if message.channel == testbot_channel and message.content == "hello":
        await testbot_channel.send('Hello!')

client.run(TOKEN)
print("logout")
