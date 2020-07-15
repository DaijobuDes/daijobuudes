import discord
import random
from discord.ext import commands



class Games(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['8ball', 'eball'])
    async def eightball(self, ctx, *, question):
        responses = ['It is possible.',
                    'Yes!',
                    'Of course',
                    'Naturally',
                    'Obviously',
                    'It shall be',
                    'The outlook is good',
                    'It is so',
                    'One would be wise to think so',
                    'The answer is certainly yes.',
                    'Why would I deny?',
                    'Well, yes.',
                    'Yes, it is.',
                    'In your dreams',
                    'I doubt it very much.',
                    'No chance.',
                    'The outlook is poor.',
                    'Unlikely.',
                    'About as likely as pigs flying.',
                    'You\'re kidding, right?',
                    'NO!',
                    'NO.',
                    'No.',
                    'The answer is a resounding no.',
                    'No, it isn\'t.',
                    'Maybe...',
                    'No clue.',
                    'I don\'t know.',
                    'The outlook is hazy, please ask again later.',
                    'What are you asking me for?',
                    'Come again?',
                    'You know the answer better than I.',
                    'The answer is def-- oooh! Shiny thing!',
                    'Uhhhhhh....',
                    'I couldn\'t say yes or no.',
                    'Maybe it is.',
                    '50-50 chance',
                    'Maybe yes, maybe no.',
                    'Can\'t answer that question.',
                    'Just ask others.',
                    'Hmmmmmmmmm.....']
        await ctx.send(f'{random.choice(responses)}')
        print(f'Eightball triggered. Question: `{question}`')

def setup(client):
    client.add_cog(Games(client))