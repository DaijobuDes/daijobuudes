import hashlib
import zlib
import discord

from discord.ext import commands


def emb(ctx):
    global embed
    embed = discord.Embed(title="Hashes Module", color=0x2463e0)
    embed.set_footer(
        text=f"Requested by {ctx.author} on {ctx.message.created_at[:-7]}",
        icon_url=ctx.author.avatar_url
    )


class Hashes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hash(self, ctx, method: str, *, args: str):
        method.lower()
        emb(ctx)
        if method == 'md5':
            embed.add_field(
                name=f"MD5 of '{args}'",
                value=hashlib.md5(args.encode('UTF-8')).hexdigest()
                )
        elif method == 'sha512':
            embed.add_field(
                name=f"SHA512 of '{args}'",
                value=hashlib.sha512(args.encode('UTF-8')).hexdigest()
                )
        elif method == 'sha384':
            embed.add_field(
                name=f"SHA384 of '{args}'",
                value=hashlib.sha384(args.encode('UTF-8')).hexdigest()
                )
        elif method == 'sha256':
            embed.add_field(
                name=f"SHA256 of '{args}'",
                value=hashlib.sha256(args.encode('UTF-8')).hexdigest()
                )
        elif method == 'sha224':
            embed.add_field(
                name=f"SHA224 of '{args}'",
                value=hashlib.sha224(args.encode('UTF-8')).hexdigest()
                )
        elif method == 'sha1':
            embed.add_field(
                name=f"SHA1 of '{args}'",
                value=hashlib.sha1(args.encode('UTF-8')).hexdigest()
                )
        elif method == 'crc32':
            temp = zlib.crc32(b'{args}')
            val = hex(temp)
            embed.add_field(
                name=f"CRC32 of '{args}'",
                value=f'{val[2:]}'
                )
        await ctx.send(embed=embed)

    @commands.command()
    async def algorithms(self, ctx):
        emb(ctx)
        embed.add_field(
            name="Available algorithms",
            value="MD5\nSHA512\nSHA384\nSHA256\nSHA224\nSHA1\nCRC32"
            )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Hashes(client))
