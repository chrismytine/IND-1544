token = 'MTIuuuuuuuuuuuzNjU3OTM4OuiukhkkhTYzMDU3ODY4OA.GbTXPM.HAecOeBW2mw1jB4DfRKdk7XuixiWkVOehcHuj8'

import discord
from discord.ext import commands
import time
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def greeting(ctx):
    await ctx.send(f"In a cafe full of aroma, i arrive as the diploma. Yahoo, the name's Sneoma!")

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def end(ctx):
    await ctx.send(f"I'm {bot.user}, ending our session. \n boop...boop...")

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
        
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


bot.run(token)
