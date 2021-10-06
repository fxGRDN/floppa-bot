from discord.ext import commands
from lib.fetchimg import getRandImg
from lib.randhi import randHi, randBingus

@commands.command(brief="Przywitanie")
async def hi(ctx):
    await ctx.send(randHi("hi.txt")+','+str(ctx.author.mention))

@commands.command(brief="Mój stosunek do bingus")
async def bingus(ctx):
    await ctx.send(randBingus("bingus.txt"))

@commands.command(brief="Najwyższa prawda")
async  def php(ctx):
    await  ctx.send("jebac php fest")

@commands.command(brief="Wspaniale fotografie")
async  def flop(ctx):
    await ctx.send(getRandImg())



