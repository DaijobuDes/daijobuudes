import discord

from discord.ext import commands
from datetime import datetime


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        consoletime = datetime.now()
        username = self.client.user.name
        discriminator = self.client.user.discriminator
        print(
            f'{consoletime}'
            u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
            'Bot online.'
        )
        print(
            f'{consoletime}'
            u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
            '---------------------------------------------'
        )
        print(
            f'{consoletime}'
            u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
            "Bot Name: "+username+"#"+discriminator
        )
        print(
            f'{consoletime}'
            u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
            "Bot ID: " + str(self.client.user.id)
        )
        print(
            f'{consoletime}'
            u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
            "Discord.py Version: " + discord.__version__
        )
        print(
            f'{consoletime}'
            u'\u001b[36;1m [DEBUG/INFO] \u001b[0m'
            '---------------------------------------------'
        )

    @commands.Cog.listener()
    async def on_disconnect(self):
        consoletime = datetime.now()
        print(
            f'{consoletime}'
            u'\u001b[33;1m [WARN/HIGH] \u001b[0m'
            'Disconnected. Attempting to connect'
        )

    @commands.Cog.listener()
    async def on_connect(self):
        consoletime = datetime.now()
        print(
            f'{consoletime}'
            u'\u001b[37;1m [INFO/LOW] \u001b[0m'
            'Connected'
        )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        consoletime = datetime.now()
        # Command handling
        if isinstance(error, commands.MissingRequiredArgument):
            print(
                f'{consoletime}'
                u'\u001b[33;1m [WARN/LOW] \u001b[0m'
                f'Missing required arguments was supplied.'
            )
            await ctx.send("Missing required arguments.")
        if isinstance(error, commands.BadArgument):
            print(
                f'{consoletime}'
                u'\u001b[33;1m [WARN/LOW] \u001b[0m'
                f'Bad arguments were inputted.'
            )
            await ctx.send("Bad arguments")
        if isinstance(error, commands.CommandNotFound):
            print(
                f'{consoletime}'
                u'\u001b[37;1m [INFO/LOW] \u001b[0m'
                f'Command does not exist.'
            )
        if isinstance(error, commands.TooManyArguments):
            print(
                f'{consoletime}'
                u'\u001b[37;1m [INFO/LOW] \u001b[0m'
                f'Too many arguments'
            )
            await ctx.send("Too many arguments")

        # Extenstion handling
        if isinstance(error, commands.ExtensionError):
            print(
                f'{consoletime}'
                u'\u001b[31;1m [ERROR/SEVERE] \u001b[0m'
                f'Extension error'
            )
        if isinstance(error, commands.ExtensionNotFound):
            print(
                f'{consoletime}'
                u'\u001b[37;1m [INFO/LOW] \u001b[0m'
                f'Extension not found'
            )
        if isinstance(error, commands.ExtensionNotLoaded):
            print(
                f'{consoletime}'
                u'\u001b[37;1m [INFO/LOW] \u001b[0m'
                f'Extension not loaded'
            )
        if isinstance(error, commands.ExtensionAlreadyLoaded):
            print(
                f'{consoletime}'
                u'\u001b[37;1m [INFO/LOW] \u001b[0m'
                f'Extension already loaded'
            )


def setup(client):
    client.add_cog(Events(client))
