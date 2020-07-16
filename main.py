# MIT License
#
# Copyright (c) 2020 Kate Aubrey Cellan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import time
import datetime

from discord.ext import commands

# LOG START
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# LOG END

start_time = time.time()

# Open token file
with open("token.txt", "r") as file:
    token = file.read()

client = commands.Bot(command_prefix=".")


# Change ctx.author.id to your own discord ID if you plan to self host
async def is_owner(ctx):
    return ctx.author.id == 451974524053749780  # DaijobuDes#0870


@client.command()
@commands.check(is_owner)
async def load(ctx, extension):
    client.load_extension(f'plugins.{extension}')
    print(f'{extension} loaded')


# Unload plugins
@client.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    client.unload_extension(f'plugins.{extension}')
    print(f'{extension} unloaded')


# Reload plugins
# Useful for realtime plugin testing
@client.command()
@commands.check(is_owner)
async def reload(ctx, extension):
    client.unload_extension(f'plugins.{extension}')
    client.load_extension(f'plugins.{extension}')
    print(f'{extension} reloaded')


for filename in os.listdir('./plugins'):
    if filename.endswith('.py'):
        client.load_extension(f'plugins.{filename[:-3]}')
        print(f'{filename} loaded')


@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time-start_time))
    text_time = str(datetime.timedelta(seconds=difference))
    await ctx.send(f'`Uptime: {text_time}`')


client.run(token)
