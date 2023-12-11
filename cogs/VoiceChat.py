import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

class VoiceChat(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.queues = {}


    def check_queue(self, ctx, id):
        if self.queues[id] != []:
            voice = ctx.guild.voice_client
            source = self.queues[id].pop(0)
            player = voice.play(source)

        # VC Join Command
    @commands.command(pass_context = True)
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            intro_song = './music/JoinSound.mp3'
            source = FFmpegPCMAudio(intro_song)
            player = voice.play(source)
            await ctx.send("I joined your VC!")
        else:
            await ctx.send("For me to join you need to be in a voice channel!")



    # VC Leave Command
    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I am not in a voice channel")



    # VC Pause Audio Command
    @commands.command(pass_context = True)
    async def pause(self, ctx):
        voice = discord.utils.get(self.client.voice_clients,guild = ctx.guild)
        if voice.is_playing():
            voice.pause()
        else: 
            await ctx.send("No audio is playing right now")


    # VC Resume Audio Command
    @commands.command(pass_context = True)
    async def resume(self, ctx):
        voice = discord.utils.get(self.client.voice_clients,guild = ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("There's currently no paused audio")


    # VC Stop Audio Command
    @commands.command(pass_context = True)
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients,guild = ctx.guild)
        voice.stop()


    # VC Play Audio Command
    @commands.command(pass_context = True)
    async def play(self, ctx, arg):
        voice = ctx.guild.voice_client
        song = './music/' + arg + '.mp3'
        source = FFmpegPCMAudio(song)
        player = voice.play(source, after=lambda x=None: self.check_queue(ctx, ctx.message.guild.id))


    # VC Queue Audio Command
    @commands.command(pass_context = True)
    async def queue(self, ctx, arg):
        voice = ctx.guild.voice_client
        song = './music/' + arg + '.mp3'
        source = FFmpegPCMAudio(song)

        guild_id = ctx.message.guild.id

        if guild_id in self.queues:
            self.queues[guild_id].append(source)
        else:
            self.queues[guild_id] = [source]

        await ctx.send("Added to queue!")


async def setup(client):
    await client.add_cog(VoiceChat(client))