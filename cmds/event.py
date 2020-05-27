import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
#開啟json文件
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    #成員加入and離開機器人傳送訊息
    #await Bot回復
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f"{member}join!")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f"{member}leave!")

    #觸發事件
    @commands.Cog.listener()
    async def on_message(self,msg):
        #當使用者輸入keyword中的文字，且不是bot發送的  在所在平頻道回復
        # == 代表完全等於
        keyword = ['apple', 'pen', 'pie', 'abc']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('hi')

def setup(bot):
    bot.add_cog(Event(bot))

