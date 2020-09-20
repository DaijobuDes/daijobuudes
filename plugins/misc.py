import discord
import psutil
import sys
import requests
import os

from discord.ext import commands
from datetime import datetime


def emb(ctx):
    global embed
    embed = discord.Embed(title="Misc Module", color=0xffe100)
    embed.set_footer(
        text=f"Requested by {ctx.author} on {ctx.message.created_at[:-7]}",
        icon_url=ctx.author.avatar_url
    )


# Code from https://www.scivision.dev/python-detect-wsl/
def in_wsl() -> bool:
    """
    WSL is thought to be the only common Linux kernel
    with Microsoft in the name.
    """

    return 'Microsoft' in os.uname().release


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        consoletime = datetime.now()
        lag = round(self.client.latency*1000)
        print(f'{consoletime} [NOTE/LOW] Latency: {lag} ms')
        message = await ctx.send('Pinging...')
        await message.edit(
            content=f'Pong... `{lag} ms`'
        )

    @commands.command()
    async def echo(self, ctx, *, args):
        await ctx.send(args)

    @commands.command()
    async def status(self, ctx):
        emb(ctx)

        # RAM Usage
        dict(psutil.virtual_memory()._asdict())
        usedmem = psutil.virtual_memory().used/1024/1024
        # activemem = psutil.virtual_memory().active
        tmem = psutil.virtual_memory().total/1024/1024
        pmem = round((usedmem/tmem)*100)

        # Swap Usage
        try:
            dict(psutil.swap_memory()._asdict())
            uswap = psutil.swap_memory().used/1024/1024
            tswap = psutil.swap_memory().total/1024/1024
            pswap = round((uswap/tswap)*100)
        except ZeroDivisionError:
            pass

        # Detect operating system
        if in_wsl():
            oper = 'WSL'
        else:
            if psutil.LINUX:
                oper = 'Linux'
            elif psutil.MACOS:
                oper = 'Mac OS'
            elif psutil.WINDOWS:
                oper = "Windows"
            else:
                oper = 'unknown'

        embed.add_field(
            name="CPU Usage",
            value=f'{psutil.cpu_percent()}%'
        )
        embed.add_field(
            name="CPU Cores",
            value=psutil.cpu_count()
        )
        embed.add_field(
            name="RAM Usage",
            value=f'{round(usedmem)}/{round(tmem)}MB ({round(pmem)}%)'
        )
        embed.add_field(
            name="Swap Usage",
            value=f'{round(uswap)}/{round(tswap)}MB ({round(pswap)}%)'
        )
        embed.add_field(
            name="OS",
            value=oper
        )

        await ctx.send(embed=embed)

    @commands.command(aliases=['about', 'ver'])
    async def version(self, ctx):
        version = 'v0.2-STABLE'
        dpy = discord.__version__
        pyver = sys.version_info
        pyver = list(pyver)

        # Detect operating system
        if in_wsl():
            oper = 'WSL'
        else:
            if psutil.LINUX:
                oper = 'Linux'
            elif psutil.MACOS:
                oper = 'Mac OS'
            elif psutil.WINDOWS:
                oper = "Windows"
            else:
                oper = 'unknown'

        embed = discord.Embed(
            title="Bot Version",
            color=0x4f1758,
            url="https://github.com/DaijobuDes/daijobuudes"
        )
        embed.add_field(
            name="Python",
            value=f'{pyver[0]}.{pyver[1]}.{pyver[2]}'
        )
        embed.add_field(
            name="Version",
            value=version
        )
        embed.add_field(
            name="Discord.py",
            value=dpy
        )
        embed.add_field(
            name="osu!api",
            value='1'
        )
        embed.add_field(
            name="OS",
            value=oper
        )
        embed.add_field(
            name="Web (Requests)",
            value=requests.__version__
        )
        embed.add_field(
            name="About DaijobuuDes",
            value="Created 14th July, 2020\n"
            "Primarily made for server moderation\n"
            "with audio support.\n"
            "Source: https://github.com/DaijobuDes/daijobuudes"
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Misc(client))
