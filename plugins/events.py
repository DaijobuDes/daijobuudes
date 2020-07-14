import discord
from discord.ext import commands

class Events(commands.Cog):
    
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot online.")

    
def setup(client):
    client.add_cog(Events(client))