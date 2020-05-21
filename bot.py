import discord
from discord.ext import commands
import json
import random
import os

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
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done')
#在cmds資料夾底下匯入.py的檔案
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__=="__main__":
    pass

bot.run(jdata['TOKEN'])
