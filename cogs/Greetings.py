import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.WELCOMECHANNEL = 1176836289962725376

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I am your bot!")


    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send("Byeee")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.client.fetch_channel(self.WELCOMECHANNEL)
        if channel is not None:
            await channel.send(f"Hello, {member.mention}!")
        else:
            print("Couldn't welcome new member. Reason: Welcomechannel not set")

    @commands.Cog.listener()
    async def on_message(self, message):
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

async def setup(client):
    await client.add_cog(Greetings(client))