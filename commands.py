import time
import discord
from datetime import datetime
from discord.ext import commands
from lib.fetchimg import getRandImg
from lib.randhi import randHi

def sort_by_emoji_count(item):
    count = 0
    for reaction in item[0]:
        count += reaction.count
    return count

@commands.command(brief='Shows top reacted to messages from 1 to 14 days', require_var_positional=True)
async def reactions(ctx, how_long, *filter):
    user_list = []
    how_long = max(min(14, int(how_long)),1)
    td = datetime.fromtimestamp(time.time()-86400*how_long)

    async for message in ctx.history(after=td, limit=None):
        FLAG = False
        if len(message.reactions) == 0:
            continue

        if filter:
            for reaction in message.reactions:
                if str(reaction) in filter:
                    break
                else:
                    FLAG = True
        if FLAG:
            continue

        user_list.append((message.reactions, message.content, message.author, message.jump_url))

    user_list.sort(key=sort_by_emoji_count, reverse=True)

    embed = discord.Embed()

    embed.title = f'Top 10 reacted to messages form {how_long} days to now:'

    for index, item in enumerate(user_list[:10],start=1):
        reactions = ""
        count = 0
        for reaction in item[0]:
            count += reaction.count
            reactions += f" {reaction.emoji}: {reaction.count}"

        embed.add_field(
            name=f"{index}. {item[2]} | {item[3]}", 
            value=f"{reactions}",
            inline=False)
    await ctx.send(embed=embed)


@commands.command(brief="Przywitanie")
async def hi(ctx):
    await ctx.send(randHi("hi.txt", ";")+','+str(ctx.author.mention))

@commands.command(brief="Mój stosunek do bingus")
async def bingus(ctx):
    await ctx.send(randHi("bingus.txt", ", "))

@commands.command(brief="Najwyższa prawda")
async  def php(ctx):
    await  ctx.send("jebac php fest")

@commands.command(brief="Wspaniale fotografie")
async  def flop(ctx):
    await ctx.send(getRandImg())