import discord
import logging
import time

from discord.ext import commands
from datetime import datetime

log = logging.getLogger('daijobuudes.events')
start_timestamp = time.time()
start_time = datetime.fromtimestamp(start_timestamp)
counter = 0
totalarg = 0
errarg = 0
totalcmd = 0


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        username = self.client.user.name
        discriminator = self.client.user.discriminator
        log.debug('Bot online')
        log.debug('---------------------------------------------')
        log.debug(f'Bot Name: {username}#{discriminator}')
        log.debug(f'Bot ID: {str(self.client.user.id)}')
        log.debug(f'Discord.py Version: {discord.__version__}')
        log.debug('---------------------------------------------')

    @commands.Cog.listener()
    async def on_disconnect(self):
        log.warning('Disconnected. Attempting to connect')

    @commands.Cog.listener()
    async def on_connect(self):
        log.info('Connected')

    @commands.Cog.listener()
    async def on_message(self, message):
        global counter, totalcmd, start_time
        counter += 1
        log.debug('Captured {} messages since {}'.format(counter, start_time.strftime("%b %d, %Y %H:%M:%S.%f")))
        if message.content.startswith('.'):
            totalcmd += 1
            log.info('Served {} commands since {}'.format(totalcmd, start_time))

    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     # Command handling
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         log.warning('Missing required arguments was supplied.')
    #         await ctx.send("Missing required arguments.")
    #     if isinstance(error, commands.BadArgument):
    #         log.warning('Bad arguments were inputted.')
    #         await ctx.send("Bad arguments")
    #     if isinstance(error, commands.CommandNotFound):
    #         log.warning('Command does not exist.')
    #     if isinstance(error, commands.TooManyArguments):
    #         log.warning('Too many arguments')
    #         await ctx.send("Too many arguments")

    #     # Extenstion handling
    #     if isinstance(error, commands.ExtensionError):
    #         log.error('Extension error')
    #     if isinstance(error, commands.ExtensionNotFound):
    #         log.warning('Extension not found')
    #     if isinstance(error, commands.ExtensionNotLoaded):
    #         log.debug('Extension not loaded')
    #     if isinstance(error, commands.ExtensionAlreadyLoaded):
    #         log.debug('Extension already loaded')


def setup(client):
    client.add_cog(Events(client))
