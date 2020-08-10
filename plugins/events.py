import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        username = self.client.user.name
        discriminator = self.client.user.discriminator
        print("Bot online.")
        print("---------------------------------------------")
        print("Bot Name: "+username+"#"+discriminator)
        print("Bot ID: " + str(self.client.user.id))
        print("Discord.py Version: " + discord.__version__)
        print("---------------------------------------------")


def setup(client):
    client.add_cog(Events(client))
