import discord
from discord.ext import commands

class DcId(commands.Cog):

    def __init__(self, client):
        self.client = client
        
        self.WELCOMECHANNEL = 1176836289962725376
        self.GENERALVC = 1174975790136430616
        self.TESTVC = 1079386115523489885


async def setup(client):
    await client.add_cog(DcId(client))