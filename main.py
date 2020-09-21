# MIT License
#
# Copyright (c) 2020 Kate Aubrey Cellan (Maine Ichinose)
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
import logging
import discord
import psutil

from discord.ext import commands
from plugins.color import *


if psutil.WINDOWS:
    os.system('cls')
elif psutil.LINUX:
    os.system('clear')
else:
    pass


# LOG START
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w'
)
handler.setFormatter(
    logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
    )
)
logger.addHandler(handler)
# LOG END

start_time = time.time()

# Open token file
with open("token.txt", "r") as file:
    token = file.read()

# Change owner_id to your own discord ID if you plan to self host
client = commands.Bot(command_prefix=">>", owner_id=451974524053749780)
# DaijobuDes#0870


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f'plugins.{extension}')
        print(f'{debuginfo}{extension} loaded')
    except ModuleNotFoundError:
        await ctx.send(f'No module named {extension}')
    except ImportError:
        await ctx.send(f' {extension}')
        print(f'{errorsevere}There was an error loading this {extension}'
        )


# Unload plugins
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f'plugins.{extension}')
        print(f'{debuginfo}{extension} unloaded'
        )
    except Exception:
        await ctx.send(f'Module not loaded {extension}')
        print(f'{warnlow}{extension} not loaded')


# Reload plugins
# Useful for realtime plugin testing
@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'plugins.{extension}')
    client.load_extension(f'plugins.{extension}')
    print(f'{debuginfo}{extension} reloaded')


@client.command(aliases=['al', 'dr'])
@commands.is_owner()
async def dirload(ctx, extension):
    client.load_extension(f'{extension}')
    print(f'{debuginfo}{extension} loaded')


@client.command(aliases=['au', 'dru'])
@commands.is_owner()
async def dirunload(ctx, extension):
    client.unload_extension(f'{extension}')
    print(
        f'{datetime.datetime.now()}'
        u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
        f'{extension} unloaded'
    )


@client.command(aliases=['drr', 'drel'])
@commands.is_owner()
async def dirreload(ctx, extension):
    client.unload_extension(f'{extension}')
    client.load_extension(f'{extension}')
    print(
        f'{datetime.datetime.now()}'
        u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
        f'{filename[:-3]} loaded'
    )


@client.command(aliases=['rall'])
@commands.is_owner()
async def reloadall(ctx):
    for filename in os.listdir('./plugins'):
        if filename.endswith('.py'):
            if filename[:-3] == 'color':
                pass
            else:
                client.unload_extension(f'plugins.{filename[:-3]}')
                print(f'{debuginfo}Unloaded {filename[:-3]}')
                client.load_extension(f'plugins.{filename[:-3]}')
                print(f'{debuginfo}Loaded {filename[:-3]}')
    print(f'{debuginfo}All plugins reloaded.')
    await ctx.send('All plugins reloaded.')


for filename in os.listdir('./plugins'):
    if filename.endswith('.py'):
        if filename[:-3] == 'color':
            pass
        else:
            client.load_extension(f'plugins.{filename[:-3]}')
            print(f'{debuginfo}{filename[:-3]} loaded')


@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time-start_time))
    text_time = str(datetime.timedelta(seconds=difference))
    print(f'{infolow}Uptime: {text_time}')
    embed = discord.Embed(title=None, color=0x519ba4)
    embed.add_field(name="Uptime", value=text_time)
    await ctx.send(embed=embed)

client.run(token)
