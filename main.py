import discord
from discord.ext import commands
import os

from apikeys import *
from dcids import *


intents = discord.Intents.default()
intents.all()
intents.reactions = True
intents.members = True
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix = '!', intents=intents)


async def load_cogs():
    for extension in os.listdir('./cogs'):
        if extension.endswith('.py') and extension != '__init__.py':
            try:
                await client.load_extension('cogs.' + extension[:-3])
                print(f"Cog: {extension} loaded successfully!")
            except Exception as e:
                print(f"Error loading cog: {type(e).__name__} - {e}")



@client.event
async def on_ready():
    activity = discord.Activity(type = discord.ActivityType.watching, name='Cute Furries on DC')
    await client.change_presence(status=discord.Status.online, activity=activity)
    await load_cogs()

    print("The bot is now ready for use!")
    print("------------------------------------")




client.run(BOTTOKEN)
