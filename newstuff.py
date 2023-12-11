import discord
from discord.ext import commands

class NewStuff(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def message(ctx, user:discord.Member, *, message=None):
        message = "Welcome to the server!"
        embed = discord.Embed(title=message)
        await user.send(embed=embed)
        await ctx.send("Message sent to user")

    @commands.command()
    async def embed(ctx):
        embed = discord.Embed(title="Dog", url="https://google.com", description="We love dogs!", color=0x4dff4d)
        embed.set_author(name=ctx.author.display_name, url="https://www.youtube.com/watch?v=UoROS78Vtr4&list=PL-7Dfw57ZZVRB4N7VWPjmT0Q-2FIMNBMP&index=9&ab_channel=JamesS", icon_url=ctx.author.avatar)
        embed.set_thumbnail(url="https://i.redd.it/zkskcm04rww61.jpg")
        embed.add_field(name="I like cats more", value="Cats are just cuter!", inline=False)
        embed.set_footer(text="Thank you for reading!")
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(NewStuff(client))