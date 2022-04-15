### Imports ###
import asyncio, discord, json, requests, traceback, youtube_dl
from discord.ext import commands
import discord_token

### Initialize discord ###
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = "$", intents = intents)
server_id = 963468410707120228
general_channel_id = 963468410707120231
general_channel = None

### Initialize youtube_dl ###
youtube_dl.utils.bug_reports_message = lambda: ""
ytdl = youtube_dl.YoutubeDL({
    "format": "bestaudio/best",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0"
})

### Custom prints ###
def _print(txt = ""):
    print("\r" + str(txt))
    print("--- Press ^C to quit ---", end = "\r")

_print("Connecting to server " + str(server_id) + "...")

### Class to play audio with youtube_dl ###
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename

### Bot events ###
@client.event
async def on_ready():
    global general_channel
    _print("Logged in as {0.user}".format(client))
    general_channel = client.get_guild(server_id).get_channel(general_channel_id)

@client.event
async def on_command_error(ctx, err):
    await ctx.reply("Error: " + "".join(traceback.format_exception(type(err), err, err.__traceback__, chain=False)))

### Bot commands ###
@client.command(brief = "Marks you as available at becoming a mod", help = "Marks you as available at becoming a mod... but be careful about rickrolls!")
async def makememod(ctx):
    await ctx.reply("Type the following letters inverted to verify that you're a human:\nPUUOYEVIGANNOGREVEN")
    await asyncio.sleep(5)
    await ctx.reply(embed = discord.Embed(title = "And btw u have been rickrolled ;)").set_image(url = "https://c.tenor.com/x8v1oNUOmg4AAAAS/rickroll-roll.gif"))
    voice = ctx.author.voice
    if voice:
        await voice.channel.connect()
        filename = await YTDLSource.from_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ", loop = client.loop)
        ctx.message.guild.voice_client.play(discord.FFmpegPCMAudio(executable = "ffmpeg.exe", source = filename))

@client.command(brief = "Sends a meme", help = "Sends a meme in the current channel by requesting https://meme-api.herokuapp.com/gimme.")
async def meme(ctx):
    data = json.loads(requests.get("https://meme-api.herokuapp.com/gimme").text)
    await ctx.reply(embed = discord.Embed(title = f"{data['title']}").set_image(url = f"{data['url']}"))

@client.command(brief = "Rickrolls (quite obvious!)",help = "[Owner role required] Sends a trick to rickroll users in the <channel_name> channel.")
@commands.is_owner()
async def rickroll(ctx, channel_name):
    global general_channel
    channel = discord.utils.get(client.get_all_channels(), name = channel_name)
    await channel.send("Hello there!\nWe are searching for a new moderator.\nIf you're interested, type \"$makememod\" in my direct messaging chat.")

@rickroll.error
async def rickroll_error(ctx, err):
    if isinstance(err, commands.CommandInvokeError):
        await ctx.reply("Error: Cannot access the channel specified!")

### Start the bot ###
client.run(discord_token.token)
