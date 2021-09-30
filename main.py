import discord
from dotenv import load_dotenv
from os import environ
from flopperBot import Bocisko
from commands.reply import hi, bingus, php
from httpserver import run

load_dotenv()
DISCORD_TOKEN = environ.get('DISCORD_TOKEN')

act = discord.Game(name='The Tiananmen Square Massacre 2')

bot = Bocisko(command_prefix='^^', activity=act)
bot.add_command(hi)
bot.add_command(bingus)
bot.add_command(php)
bot.run(DISCORD_TOKEN)
run()

