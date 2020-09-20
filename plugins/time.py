import time
import discord

from discord.ext import commands
from ddate.base import DDate


def emb(ctx):
    global embed
    embed = discord.Embed(title="Time Module", color=0x5eff00)
    embed.set_footer(
        text=f"Requested by {ctx.author} on {ctx.message.created_at[:-7]}",
        icon_url=ctx.author.avatar_url
    )


class Time(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def time(self, ctx):
        localtime = time.asctime(time.localtime(time.time()))
        emb(ctx)
        embed.add_field(
            name="Bot Local Time",
            value=f'Local time: `{localtime}` GMT+8'
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def ddate(self, ctx):
        emb(ctx)
        embed.add_field(name="DDate", value=DDate())
        await ctx.send(embed=embed)

    @commands.command()
    async def at(self, ctx):
        emb(ctx)
        embed.add_field(name="At", value=round(time.time()))
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Time(client))
