import discord
from discord.ext import commands


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Purge messages
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def purge(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        print(f'Purged {amount} messages')

    # Kick a member
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Sucessfully kicked `{member}` for `{reason}`')
        print(f'Kicked member `{member}` for `{reason}`.')

    # Ban a member
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'Sucessfully banned `{member}` for `{reason}`')
        print(f'Banned member `{member}` for `{reason}`.')

    # Unban a member
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unban(self, ctx, *, member):
        self.banned_users = await ctx.guild.bans()
        self.member_name, self.member_discriminator = member.split('#')

        for ban_entry in self.banned_users:
            user = ban_entry.user

        membername = self.member_name
        memberdisc = self.member_discriminator
        if (user.name, user.discriminator) == (membername, memberdisc):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned user {user.name}#{user.discriminator}')
            print(f'Unbanned user {user.name}#{user.discriminator}')
            return
        else:
            await ctx.send('User not found.')
            print('User not found.')
            return


def setup(client):
    client.add_cog(Moderation(client))
