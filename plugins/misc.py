from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        print(f'Pinging at `{round(self.client.latency * 1000)} ms`')
        message = await ctx.send('Pinging...')
        await message.edit(content=f'Responded for `{round(self.client.latency*1000)} ms`')


def setup(client):
    client.add_cog(Misc(client))
