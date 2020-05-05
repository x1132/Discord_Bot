import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')

#機器人上線事件
@bot.event
async def on_ready():
    print(">> Bot is online <<")

#成員加入and離開機器人傳送訊息
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(707116462057324566)
    await channel.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(707116543909298187)
    await channel.send(f"{member}leave!")

bot.run("NjY5ODQxNjYyNTM2NzEyMjIy.XqqYLQ.R3xYwu2FOc--QOsqD-aRa4Typ4c")
