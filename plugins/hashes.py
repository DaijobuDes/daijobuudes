import hashlib
import zlib
import discord

from discord.ext import commands


class Hashes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def md5(self, ctx, *, args: str):
        embed = discord.Embed(title="Hashes Module")
        embed.set_footer(text=f"Requested by {ctx.author} on {ctx.message.created_at}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"MD5 of '{args}'",
                        value=hashlib.md5(args.encode('UTF-8')).hexdigest())
        await ctx.send(embed=embed)

    @commands.command()
    async def sha512(self, ctx, *, args: str):
        embed = discord.Embed(title="Hashes Module")
        embed.set_footer(text=f"Requested by {ctx.author} on {ctx.message.created_at}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"SHA512 of '{args}'",
                        value=hashlib.sha512(args.encode('UTF-8')).hexdigest())
        await ctx.send(embed=embed)

    @commands.command()
    async def sha384(self, ctx, *, args: str):
        embed = discord.Embed(title="Hashes Module")
        embed.set_footer(text=f"Requested by {ctx.author} on {ctx.message.created_at}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"SHA384 of '{args}'",
                        value=hashlib.sha384(args.encode('UTF-8')).hexdigest())
        await ctx.send(embed=embed)

    @commands.command()
    async def sha256(self, ctx, *, args: str):
        embed = discord.Embed(title="Hashes Module")
        embed.set_footer(text=f"Requested by {ctx.author} on {ctx.message.created_at}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"SHA256 of '{args}'",
                        value=hashlib.sha256(args.encode('UTF-8')).hexdigest())
        await ctx.send(embed=embed)

    @commands.command()
    async def sha224(self, ctx, *, args: str):
        embed = discord.Embed(title="Hashes Module")
        embed.set_footer(text=f"Requested by {ctx.author} on {ctx.message.created_at}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"SHA224 of '{args}'",
                        value=hashlib.sha224(args.encode('UTF-8')).hexdigest())
        await ctx.send(embed=embed)

    @commands.command()
    async def sha1(self, ctx, *, args: str):
        embed = discord.Embed(title="Hashes Module")
        embed.set_footer(text=f"Requested by {ctx.author} on {ctx.message.created_at}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"SHA1 of '{args}'",
                        value=hashlib.sha1(args.encode('UTF-8')).hexdigest())
        await ctx.send(embed=embed)

    @commands.command()
    async def crc32(self, ctx, *, args: str):
        temp = zlib.crc32(b'{args}')
        val = hex(temp)
        embed = discord.Embed(title="Hashes Module")
        embed.set_footer(text=f"Requested by {ctx.author} on {ctx.message.created_at}",
                         icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"CRC32 of '{args}'",
                        value=f'{val[2:]}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Hashes(client))
