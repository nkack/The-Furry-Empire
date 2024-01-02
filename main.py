import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from dotenv import load_dotenv
import os

# Loading Channel Ids and Bot Token
load_dotenv('.env')
bot_token: str = os.getenv('BOT_TOKEN')
welcome_channel: int = os.getenv('WELCOME_CHANNEL')
log_channel: int = os.getenv('LOG_CHANNEL')


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



client.run(bot_token)
