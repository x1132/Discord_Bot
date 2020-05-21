import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

#開啟json文件
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    #隨機選取圖片(本機)
    @commands.command()
    async def 圖片(self,ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)
    
    #隨機選取圖片(web)
    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

def setup(bot):
    bot.add_cog(React(bot))

