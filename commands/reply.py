from discord.ext import commands
from lib.fetchimg import getRandImg
@commands.command(brief="Przywitanie")
async def hi(ctx):
    await ctx.send('Siem')

@commands.command(brief="Mój stosunek do bingus")
async def bingus(ctx):
    await ctx.send('frajer')

@commands.command(brief="Najwyższa prawda")
async  def php(ctx):
    await  ctx.send("jebac php fest")

@commands.command(brief="Wspaniale fotografie")
async  def flop(ctx):
    await ctx.send(getRandImg())



