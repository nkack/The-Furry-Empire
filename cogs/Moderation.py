import nextcord, os
from nextcord.ext import commands, application_checks
from nextcord import Member, Interaction
from nextcord.ext.commands import has_permissions, MissingPermissions
from nextcord.utils import get
from dotenv import load_dotenv

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channels = {
                "log_channel": 1175901104786133162,
            }
        
    testServerId = 1079386114328105011

    @nextcord.slash_command(name="purge", description="Purge an amount of messages", guild_ids=[testServerId])
    async def purge(self, interaction: Interaction, amount: int, specific_user: nextcord.Member = None):
        messages = await interaction.channel.history(limit=amount).flatten()
        await interaction.response.send_message("Purging messages...")
        for message in messages:
            if message.author == specific_user or specific_user == None:
                await message.delete()
        await interaction.edit_original_message(content="Successfully purged messages!")
        print(f"Purged {amount} messages from {interaction.channel.name}")

        embed = nextcord.Embed(color=nextcord.Color.from_rgb(0, 0, 255))
        embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
        embed.add_field(name='', value=f'Message purge in {interaction.channel.name}', inline=False)
        embed.add_field(name='', value=f'{interaction.user.display_name} purged {amount} messages from {interaction.channel.mention}', inline=False)

        await self.client.get_channel(self.channels["log_channel"]).send(embed=embed)


    @nextcord.slash_command(name="kick", description="Kick someone from the server!", guild_ids=[testServerId])
    @application_checks.has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction, member: nextcord.Member, reason: str):
        await interaction.response.send_message(f"User {member} has been kicked!")


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
        if isinstance(error, MissingPermissions):
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
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have permission to use this command!")



    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have the permissions to do this!")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You don't have the permissions to do this!")



    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        if isinstance(error, MissingPermissions):
            ctx.send("You don't have permission to run this command")


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = nextcord.Embed(color=nextcord.Color.from_rgb(255, 0, 0))
        embed.set_author(name=message.author.name, icon_url=message.author.avatar)
        embed.add_field(name='', value=f'Message deleted in {message.channel.mention}\n', inline=False)
        embed.add_field(name='Content', value=message.content, inline=False)
        await self.client.get_channel(self.channels["log_channel"]).send(embed=embed)


def setup(client):
    client.add_cog(Moderation(client))