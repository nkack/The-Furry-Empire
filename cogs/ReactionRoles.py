import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import os

os.load_dotenv('.env')
testServerId: int = os.getenv('TEST_SERVER')


class ReactionRoles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def new_rr(self, ctx, role = nextcord.Role):
        return
    

def setup(client):
    client.add_cog(ReactionRoles(client))
