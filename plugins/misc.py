import discord
import psutil

from discord.ext import commands


def emb(ctx):
    global embed
    embed = discord.Embed(title="Misc Module", color=0xffe100)
    embed.set_footer(
        text=f"Requested by {ctx.author} on {ctx.message.created_at}",
        icon_url=ctx.author.avatar_url
    )


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        print(f'Pinging at `{round(self.client.latency * 1000)} ms`')
        message = await ctx.send('Pinging...')
        await message.edit(
            content=f'Pong... `{round(self.client.latency*1000)}` ms'
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
        dict(psutil.swap_memory()._asdict())
        uswap = psutil.swap_memory().used/1024/1024
        tswap = psutil.swap_memory().total/1024/1024
        pswap = round((uswap/tswap)*100)

        # Detect operating system
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


def setup(client):
    client.add_cog(Misc(client))
