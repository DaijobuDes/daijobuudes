# MIT License
#
# Copyright (c) 2020 Kate Aubrey Cellan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import time
import datetime
import discord
import youtube_dl
import shutil
import logging

from discord.ext import commands
from discord.utils import get

queues = {}

# LOG START
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# LOG END

start_time = time.time()

# Open token file
with open("token.txt", "r") as file:
    token = file.read()

client = commands.Bot(command_prefix=">>")


# Change ctx.author.id to your own discord ID if you plan to self host
async def is_owner(ctx):
    return ctx.author.id == 451974524053749780  # DaijobuDes#0870


@client.command()
@commands.check(is_owner)
async def load(ctx, extension):
    client.load_extension(f'plugins.{extension}')
    print(f'{extension} loaded')


# Unload plugins
@client.command()
@commands.check(is_owner)
async def unload(ctx, extension):
    client.unload_extension(f'plugins.{extension}')
    print(f'{extension} unloaded')


# Reload plugins
# Useful for realtime plugin testing
@client.command()
@commands.check(is_owner)
async def reload(ctx, extension):
    client.unload_extension(f'plugins.{extension}')
    client.load_extension(f'plugins.{extension}')
    print(f'{extension} reloaded')


for filename in os.listdir('./plugins'):
    if filename.endswith('.py'):
        client.load_extension(f'plugins.{filename[:-3]}')
        print(f'{filename} loaded')


@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time-start_time))
    text_time = str(datetime.timedelta(seconds=difference))
    await ctx.send(f'`Uptime: {text_time}`')


@client.command(pass_context=True, aliases=['j'])
async def join(ctx):
    global voice
    global channel
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send(f'Moved to {channel}.')
        print(f'Moved to {channel}.')
    else:
        voice = await channel.connect()
        await ctx.send(f'Joined {channel}.')
        print(f'Joined {channel}.')


@client.command(pass_context=True, aliases=['l'])
async def leave(ctx):
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send('Left voice channel.')
        print('Left voice channel.')
    else:
        await ctx.send('I\'m not on a voice channel.')
        print('Attempted to leave not on a voice channel.')


@client.command(pass_context=True, aliases=['p'])
async def play(ctx, url: str):

    def check_queue():
        Queue_infile = os.path.isdir("./queue")

        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1

            try:
                first_file = os.listdir(DIR)[0]
            except:
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
    except:
        print('No old Queue folder')

    voice = get(client.voice_clients, guild=ctx.guild)
    # channel = ctx.message.author.voice.channel

    ydl_opts = {
        'format': 'bestaudio/best',
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


@client.command(pass_context=True, aliases=['pa'])
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.pause()
        print('Audio paused.')
        await ctx.send('Audio paused.')
    else:
        print('Music currently not playing')
        await ctx.send('Music currently not playing')


@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

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


@client.command(pass_context=True, aliases=['st'])
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

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


@client.command(pass_context=True, aliases=['s', 'sk', 'next', 'n'])
async def skip(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        voice.stop()
        print('Stopping audio.')
        message = await ctx.send('Skipping track.')
        await message.edit(content='Skipped :thumbsup:')
    else:
        print('Music currently not playing.')
        await ctx.send('Music currently not playing.')



@client.command(pass_context=True, aliases=['q'])
async def queue(ctx, url: str):
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
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus',
            # 'prefferedquality': '192'
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio...\n')
        ydl.download([url])

    await ctx.send('Adding song ' + str(q_num) + ' to queue.')
    print('Adding song ' + str(q_num) + ' to queue.')


client.run(token)
