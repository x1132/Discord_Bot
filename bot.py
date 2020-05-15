import discord
from discord.ext import commands
import json
#開啟json文件
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='~')

#機器人上線事件
@bot.event
async def on_ready():
    print(">> Bot is online <<")

#成員加入and離開機器人傳送訊息
#await Bot回復
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f"{member}join!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f"{member}leave!")

#ctx = context(上下文)
#round 表示四捨五入進位
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}毫秒")

bot.run(jdata['TOKEN'])
