import nextcord
from nextcord.ext import commands
from nextcord import Member
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord.utils import get

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.logchannel = client.get_channel(1175901104786133162)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    # Add Role Commands
    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def addRole(self, ctx, user : nextcord.Member, *, role : nextcord.role):

        if role in user.roles:
            await ctx.send("This user already has the role")
        else:
            await user.add_roles(role)
            await ctx.send(f"Added {role} to {user.mention}")

    @addRole.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command!")


    @commands.command(pass_context = True)
    @commands.has_permissions(manage_roles = True)
    async def removeRole(self, ctx, user : nextcord.Member, *, role : nextcord.role):

        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"Removed {role} from {user.mention}")
        else:
            
            await ctx.send(f"{user.mention} does not have the role {role}")

    @removeRole.error
    async def removeRole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to use this command!")



    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to do this!")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
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


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = nextcord.Embed(color=nextcord.Color.from_rgb(255, 0, 0))
        embed.set_author(name=message.author.name, icon_url=message.author.avatar)
        embed.add_field(name='', value=f'Message deleted in {message.channel.mention}\n', inline=False)
        embed.add_field(name='Content', value=message.content, inline=False)
        await self.logchannel.send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))