import asyncio, discord, json, requests
from discord.ext import commands

CLIENT = commands.Bot(command_prefix="!")
SERVER_ID = 963468410707120228
GENERAL_CHANNEL_ID = 963468410707120231

def _print(txt = ""):
    print("\r" + str(txt))
    print("--- Press ^C to quit ---", end = "\r")

_print()

@CLIENT.event
async def on_ready():
    _print("Logged in as {0.user}".format(CLIENT))

@CLIENT.command()
async def makememod(ctx):
    await ctx.reply("Type the following letters inverted to verify that you're a human:\nPUUOYEVIGANNOGREVEN")
    await asyncio.sleep(5)
    await ctx.reply(embed = discord.Embed(title = "And btw u have been rickrolled ;)").set_image(url = "https://c.tenor.com/x8v1oNUOmg4AAAAS/rickroll-roll.gif"))

@CLIENT.command()
async def meme(ctx):
    data = json.loads(requests.get("https://meme-api.herokuapp.com/gimme").text)
    await ctx.reply(embed = discord.Embed(title = f"{data['title']}").set_image(url = f"{data['url']}"))

@CLIENT.command()
async def rickroll(ctx):
    general_channel = CLIENT.get_guild(SERVER_ID).get_channel(GENERAL_CHANNEL_ID)
    await general_channel.send("Hello there!\nWe are searching for a new moderator.\nIf you're interested, use the command \"!makememod\" by direct messaging me.")

CLIENT.run("OTYzNDc3ODAxNzc0NzQzNjEy.YlWqoA.ywztuNgfKAGwrwJtUAjFRtGH0fY")
