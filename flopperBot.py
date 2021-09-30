from discord.ext import commands


class Bocisko(commands.Bot):
    async def on_ready(self):
        print(self)

