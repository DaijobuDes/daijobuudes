import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot online.")
        print("---------------------------------------------")
        print("Bot Name: "+self.client.user.name+"#"+self.client.user.discriminator)
        print("Bot ID: " + str(self.client.user.id))
        print("Discord.py Version: " + discord.__version__)
        print("---------------------------------------------")


def setup(client):
    client.add_cog(Events(client))
