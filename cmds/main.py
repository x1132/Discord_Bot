import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    
    #ctx = context(上下文)
    #round 表示四捨五入進位
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}毫秒")

    @commands.command()
    async def hi(self,ctx):
        await ctx.send("12345")

def setup(bot):
    bot.add_cog(Main(bot))

