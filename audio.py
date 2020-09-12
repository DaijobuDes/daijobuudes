import discord
import youtube_dl
import shutil
import os

from discord.ext import commands
from discord.utils import get

queues = {}


class Audio(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['j'])
    async def join(self, ctx):
        global voice
        global channel
        channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
            await ctx.send(f'Moved to {channel}.')
            print(f'Moved to {channel}.')
        else:
            voice = await channel.connect()
            await ctx.send(f'Joined {channel}.')
            print(f'Joined {channel}.')

    @commands.command(pass_context=True, aliases=['l'])
    async def leave(self, ctx):
        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send('Left voice channel.')
            print('Left voice channel.')
        else:
            await ctx.send('I\'m not on a voice channel.')
            print('Attempted to leave not on a voice channel.')

    @commands.command(pass_context=True, aliases=['p'])
    async def play(self, ctx, url: str):

        def check_queue():
            Queue_infile = os.path.isdir("./queue")

            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("queue"))
                length = len(os.listdir(DIR))
                still_q = length - 1

                try:
                    first_file = os.listdir(DIR)[0]
                except FileNotFoundError:
                    print('No more songs in queue.')
                    queues.clear()
                    return

                main_location = os.path.dirname(os.path.realpath(__file__))
                # Change / to \\ if you are on windows. / was supposed to be on unix systems
                song_path = os.path.abspath(os.path.realpath("queue") + "/" + first_file)

                if length != 0:
                    print('Song done, playing next song.')
                    print(f'Songs in queue {still_q}')
                    song_there = os.path.isfile("song.opus")

                    if song_there:
                        os.remove("song.opus")
                        print('Removed song.')

                    shutil.move(song_path, main_location)

                    for file in os.listdir("./"):
                        if file.endswith(".opus"):
                            os.rename(file, 'song.opus')

                    voice.play(discord.FFmpegPCMAudio("song.opus"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 1.00

                else:
                    queues.clear()
                    return

            else:
                queues.clear()
                print('No songs were queued.')

        song_there = os.path.isfile("song.opus")
        try:
            if song_there:
                os.remove("song.opus")
                queues.clear()
                print('Removed song.opus on directory.')
        except PermissionError:
            print('Operation not permitted or file is in use.')
            return

        Queue_infile = os.path.isdir("./queue")

        try:
            Queue_folder = "./queue"
            if Queue_infile is True:
                print('Removed old folder.')
                shutil.rmtree(Queue_folder)
        except FileNotFoundError:
            print('No old Queue folder')

        voice = get(self.client.voice_clients, guild=ctx.guild)
        # channel = ctx.message.author.voice.channel

        ydl_opts = {
            'format': 'bestaudio/best',
            # 'quiet': True,
            'noplaylist': True,
            'maxfilesize': '50M',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'opus',
                # 'prefferedquality': '192'
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading audio...\n')
            ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith(".opus"):
                name = file
                print(f'Renamed File: {file}')
                os.rename(file, "song.opus")

        # if voice and voice.is_connected():
        #     await voice.disconnect()
        #     voice = await channel.connect()

        voice.play(discord.FFmpegPCMAudio("song.opus"), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1.00

        nname = name.rsplit("-", 2)
        # await ctx.send(f'Playing: {nname}')
        print(f'Playing audio {nname}')

    @commands.command(pass_context=True, aliases=['pa'])
    async def pause(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.pause()
            print('Audio paused.')
            await ctx.send('Audio paused.')
        else:
            print('Music currently not playing')
            await ctx.send('Music currently not playing')

    @commands.command(pass_context=True, aliases=['r', 'res'])
    async def resume(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        if voice and voice.is_paused():
            voice.resume()
            print('Audio resuming')
            await ctx.send('Audio resuming')
        elif voice and voice.is_playing():
            print('Music already playing.')
            await ctx.send('Music already playing.')
        else:
            print('Music currently not playing')
            await ctx.send('Music currently not playing.')

    @commands.command(pass_context=True, aliases=['st'])
    async def stop(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        queues.clear()

        Queue_infile = os.path.isdir("./queue")

        if Queue_infile is True:
            shutil.rmtree("./queue")

        if voice and voice.is_playing():
            voice.stop()
            print('Stopping audio.')
            message = await ctx.send('Stopping audio.')
            await message.edit(content='Stopped :thumbsup:')
        else:
            print('Music currently not playing')
            await ctx.send('Music currently not playing.')

    @commands.command(pass_context=True, aliases=['s', 'sk', 'next', 'n'])
    async def skip(self, ctx):
        voice = get(self.client.voice_clients, guild=ctx.guild)

        queues.clear()

        if voice and voice.is_playing():
            voice.stop()
            print('Stopping audio.')
            message = await ctx.send('Skipping track.')
            await message.edit(content='Skipped :thumbsup:')
        else:
            print('Music currently not playing.')
            await ctx.send('Music currently not playing.')

    @commands.command(pass_context=True, aliases=['q'])
    async def queue(self, ctx, url: str):
        Queue_infile = os.path.isdir("./queue")

        if Queue_infile is False:
            os.mkdir("queue")
        DIR = os.path.abspath(os.path.realpath("queue"))

        q_num = len(os.listdir(DIR))
        q_num += 1
        add_queue = True

        while add_queue:
            if q_num in queues:
                q_num += 1
            else:
                add_queue = False
                queues[q_num] = q_num

        queue_path = os.path.abspath(os.path.realpath("queue") + f'/song{q_num}.%(ext)s')

        ydl_opts = {
            'format': 'bestaudio/best',
            # 'quiet': True,
            'noplaylist': True,
            'outtmpl': queue_path,
            'maxfilesize': '50M',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'opus',  # mp3
                # 'prefferedquality': '192'
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print('Downloading audio...\n')
            ydl.download([url])

        await ctx.send('Adding song ' + str(q_num) + ' to queue.')
        print('Adding song ' + str(q_num) + ' to queue.')


def setup(client):
    client.add_cog(Audio(client))
