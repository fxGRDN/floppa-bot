import discord
from discord.ext import commands
from os import environ
from dotenv import load_dotenv
from simple_commands import hi, php, bingus, flop
from commands.reactions import reactions

load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Game(name='^^ | It\'s Flopp\'in Time')

bot = commands.Bot(command_prefix='^^', activity=activity, intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Misslick or there is no such command")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Wrong argument")

bot.add_command(hi)
bot.add_command(reactions)
bot.add_command(php)
bot.add_command(bingus)
bot.add_command(flop)
bot.run(DISCORD_TOKEN)