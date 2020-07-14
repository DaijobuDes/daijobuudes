import discord
import os

from discord.ext import commands, tasks
from itertools import cycle

# Open token file
with open("token.txt", "r") as file:
    token = file.read()    

client = commands.Bot(command_prefix = ".")
# status = cycle(['', '', '', ''])

async def is_owner(ctx):
    return ctx.author.id == 451974524053749780 # DaijobuDes#0870

@client.command()
@commands.check(is_owner)
async def load(ctx, extension):
    client.load_extension(f'plugins.{extension}')
    print(f'{extension} loaded')

@client.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    client.unload_extension(f'plugins.{extension}')
    print(f'{extension} unloaded')

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

##### Error handling 
# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Missing required argument.')
#         print("Command missing argument")
#     elif isinstance(error, commands.CommandNotFound):
#         print("No command exists")

client.run(token)
