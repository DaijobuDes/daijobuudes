import random

from discord.ext import commands
from math import ldexp, degrees, sqrt, sin, cos, tan, sinh, cosh, tanh


class Math(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx, base=100):
        if base < 0:
            base = -base
        await ctx.send(random.randint(0, base))

    @commands.command()
    async def dice(self, ctx, times=1, sides=6):
        if times == 0 and sides == 0:
            await ctx.send('You can\'t roll 0')
        elif times < 0 and sides < 0:
            times = -times
            sides = -sides
            await ctx.send()
        else:
            await ctx.send()

    @commands.command()
    async def pow(self, ctx, base: int, exponent: int):
        # Not using math.pow() since it is vulnerable to not
        # responding on calculating large values

        try:
            answer = ldexp(base, exponent)
        except OverflowError:
            await ctx.send('Nuh uh, nice try. Math range error')
        except ValueError:
            await ctx.send('Nice try placing invalid characters')
        finally:
            await ctx.send(answer)

    @commands.command()
    async def trig(self, ctx, choice: str, x: float):
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
        await ctx.send(f'''
        ```
D: {deg}
R: {answer}```''')

    @commands.command()
    async def sqrt(self, ctx, number):
        await ctx.send(sqrt(number))


def setup(client):
    client.add_cog(Math(client))
