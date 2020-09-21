import discord
from .color import *

from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        username = self.client.user.name
        discriminator = self.client.user.discriminator
        print(f'{debuginfo}Bot online')
        print(f'{debuginfo}---------------------------------------------')
        print(f"{debuginfo}Bot Name: "+username+"#"+discriminator)
        print(f"{debuginfo}Bot ID: " + str(self.client.user.id))
        print(f"{debuginfo}Discord.py Version: " + discord.__version__)
        print(f'{debuginfo}---------------------------------------------')

    @commands.Cog.listener()
    async def on_disconnect(self):
        print(f'{warnhigh}Disconnected. Attempting to connect')

    @commands.Cog.listener()
    async def on_connect(self):
        print(f'{infolow}Connected')

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     # Command handling
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         print(f'{warnlow}Missing required arguments was supplied.')
    #         await ctx.send("Missing required arguments.")
    #     if isinstance(error, commands.BadArgument):
    #         print(f'{warnlow}Bad arguments were inputted.')
    #         await ctx.send("Bad arguments")
    #     if isinstance(error, commands.CommandNotFound):
    #         print(f'{warnlow}Command does not exist.')
    #     if isinstance(error, commands.TooManyArguments):
    #         print(f'{infolow}Too many arguments')
    #         await ctx.send("Too many arguments")

    #     # Extenstion handling
    #     if isinstance(error, commands.ExtensionError):
    #         print(f'{Color.errorsevere(self)}Extension error')
    #     if isinstance(error, commands.ExtensionNotFound):
    #         print(f'{infolow}Extension not found')
    #     if isinstance(error, commands.ExtensionNotLoaded):
    #         print(f'{infolow}Extension not loaded')
    #     if isinstance(error, commands.ExtensionAlreadyLoaded):
    #         print(f'{infolow}Extension already loaded')


def setup(client):
    client.add_cog(Events(client))
