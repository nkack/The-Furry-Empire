import nextcord
from nextcord.ext import commands
import os

from apikeys import *
from Channels import *


intents = nextcord.Intents.all()
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
    activity = nextcord.Activity(type = nextcord.ActivityType.watching, name='Cute Furries on DC')
    await client.change_presence(status=nextcord.Status.online, activity=activity)
    await load_cogs()

    print("The bot is now ready for use!")
    print("------------------------------------")




client.run(BOTTOKEN)
