import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.WELCOMECHANNEL = 1176836289962725376

    testServerId = 1079386114328105011

    @nextcord.slash_command(name="greeting", description="A greeting from the bot", guild_ids=[testServerId])
    async def greet(self, interaction: Interaction):
        await interaction.response.send_message("Hello! Your interaction worked!")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.client.fetch_channel(self.WELCOMECHANNEL)
        if channel is not None:
            await channel.send(f"Welcome to The Furry Empire, {member.mention}! We are happy to see you, and hope that you'll enjoy your stay. 🩷 \n \n Before you talk, please check out the <#1175352660141019177> to make sure you follow our set rules for keeping an open and friendly environment.")
        else:
            print("Couldn't welcome new member. Reason: Welcomechannel not set")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        if ("happy") in message.content:
            emoji = '😁'
            await message.add_reaction(emoji)
        content = message.content.lower()
        greetings = {"hello": "Hewwo cutie!",
                    "hi": "Hiiii cutie",
                    "good morning": "Morning cutie, how was your sleep?",
                    "good evening": "Evening cutie, wyd rn?",
                    "good night": "Good Night cutie, sleep tight and don't let the bedbugs bite <3"}
        for greeting in greetings.keys():
            if content == greeting:
                await message.reply(greetings[greeting])
                print(f"Answered on hi to {message.author.display_name}")
            else:
                pass
        await self.client.process_commands(message)

    
        


    

def setup(client):
    client.add_cog(Greetings(client))
