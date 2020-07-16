import time

from discord.ext import commands
from ddate.base import DDate


class Time(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def time(self, ctx):
        localtime = time.asctime(time.localtime(time.time()))
        await ctx.send(f'Local bot time : `{localtime} GMT+8`')

    @commands.command()
    async def ddate(self, ctx):
        await ctx.send(DDate())

    @commands.command()
    async def at(self, ctx):
        await ctx.send(round(time.time()))


def setup(client):
    client.add_cog(Time(client))
