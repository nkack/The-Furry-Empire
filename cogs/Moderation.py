import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def addRole(self, ctx, user : discord.Member, *, role : discord.role):

        if role in user.roles:
            await ctx.send("This user already has the role")


    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to do this!")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to do this!")



    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            ctx.send("You don't have permission to run this command")


async def setup(client):
    await client.add_cog(Moderation(client))