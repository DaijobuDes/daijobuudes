import random
import discord
import d20

from discord.ext import commands
from math import degrees, sqrt, sin, cos, tan, sinh, cosh, tanh
from math import pow as exp


def emb(ctx):
    global embed
    embed = discord.Embed(title="Math Module", color=0xe700ff)
    embed.set_footer(
        text=f"Requested by {ctx.author} on {ctx.message.created_at[:-7]}",
        icon_url=ctx.author.avatar_url
    )


class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx, base=100):
        if base < 0:
            base = -base
        await ctx.send(random.randint(0, base))

    @commands.command()
    async def dice(self, ctx, times=6, sides=6):
        """Rolls 6 times and 6 sides by default."""

        emb(ctx)
        if times == 0 and sides == 0:
            embed.add_field(name="Error",
                            value="You can't roll 0.")
        elif times < 0 and sides < 0:
            embed.add_field(name="Error",
                            value="You can't roll negative values.")
        elif sides > 1000:
            embed.add_field(name="Error",
                            value="Dice can't have more than 1000 sides.")
        elif times > 100:
            embed.add_field(name="Error",
                            value="Dice can't roll more than 100 sides.")
        else:
            results = d20.roll(f"{times}d{sides}")
            embed.add_field(name="Results",
                            value=results
                            )
        await ctx.send(embed=embed)

    @commands.command()
    async def pow(self, ctx, base: int, exponent: int):

        emb(ctx)
        try:
            answer = exp(base, exponent)
        except OverflowError:
            embed.add_field(name="Error",
                            value="Nuh uh, nice try. Math range error")
            await ctx.send(embed=embed)
        except ValueError:
            embed.add_field(name="Error",
                            value="Nice try placing invalid characters")
            await ctx.send(embed=embed)
        finally:
            embed.add_field(name=f"Answer to {base}^{exponent}", value=answer)
            await ctx.send(embed=embed)

    @commands.command()
    async def trig(self, ctx, choice: str, x: float):

        emb(ctx)
        if choice == 'sin':
            answer = (sin(x))
        elif choice == 'cos':
            answer = (cos(x))
        elif choice == 'tan':
            answer = (tan(x))
        elif choice == 'sinh':
            answer = (sinh(x))
        elif choice == 'cosh':
            answer = (cosh(x))
        elif choice == 'tanh':
            answer = (tanh(x))
        else:
            answer = 0
        deg = degrees(answer)
        embed.add_field(name="Answer",
                        value=f"Degrees: {deg}\nRadians: {answer}"
                        )
        await ctx.send(embed=embed)

    @commands.command()
    async def sqrt(self, ctx, number: float):

        emb(ctx)
        embed.add_field(name="Answer",
                        value=sqrt(number)
                        )
        await ctx.send(embed=embed)

    @commands.command()
    async def itersqrt(self, ctx, number: float):

        emb(ctx)
        for i in range(1, 11):
            embed.add_field(name=f'Iteration {i}', value=sqrt(number))
            number = sqrt(number)
        await ctx.send(embed=embed)

    @commands.command()
    async def iterpow(self, ctx, base: int):

        emb(ctx)
        for i in range(1, 11):
            try:
                embed.add_field(name=f'Iteration {i}', value=exp(base, i))
            except OverflowError:
                embed.add_field(
                    name=f'Iteration {i}',
                    value="Nuh uh, nice try. Math range error"
                )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Math(client))
