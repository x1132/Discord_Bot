import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')

#機器人上線事件
@bot.event
async def on_ready():
    print(">> Bot is online <<")

#成員加入and離開機器人傳送訊息
#await Bot回復
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(707116462057324566)
    await channel.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(707116543909298187)
    await channel.send(f"{member}leave!")

#ctx = context(上下文)
#round 表示四捨五入進位
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}毫秒")

bot.run("Your discord bot token")
