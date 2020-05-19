import discord
from discord.ext import commands
import json
import random
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

#隨機選取圖片(本機)
@bot.command()
async def 圖片(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)
#隨機選取圖片(web)
@bot.command()
async def web(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

bot.run(jdata['TOKEN'])
