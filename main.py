import nextcord
from nextcord.ext import commands
import os

from apikeys import *
from Channels import *


intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)

async def load_cogs(client):
    cogs = ['Greetings', 'Moderation', 'ReactionRoles', 'VoiceChat']
    for cog in cogs:
        try:
            client.load_extension('cogs.' + cog)
            print(f'The "{cog}" cog has been loaded!')
        except Exception as e:
            print(f'Error loading cog "{cog}": {type(e).__name__} - {e}')


@client.event
async def on_ready():
    activity = nextcord.Activity(type = nextcord.ActivityType.watching, name='Cute Furries on DC')
    await client.change_presence(status=nextcord.Status.online, activity=activity)
    await load_cogs(client)

    print("The bot is now ready for use!")
    print("------------------------------------")




client.run(BOTTOKEN)
