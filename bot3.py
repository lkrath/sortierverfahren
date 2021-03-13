# noch ein versuch

import discord 
import os
from dotenv import load_dotenv
from discord.ext import commands
import youtube_dl
#from youtube_dl import YoutubeDL
from discord.utils import get
from discord import FFmpegPCMAudio

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

#@bot.command()
#async def join(ctx):
#    channel = ctx.author.voice.channel
#    await channel.connect()

@bot.command()
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@bot.command()
async def join(ctx):
    vc = discord.utils.get(ctx.guild.voice_channels, name='General')
    await vc.connect()

@bot.command()
async def yt(ctx, url:str):
    print("got song")
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Es spielt grade ein Lied.")
        return
        
    #vc = discord.utils.get(ctx.guild.voice_channels, name='General')
    #await vc.connect()
    voice = discord.utils.get(bot.voice_clients)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    voice.stop()

@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_playing():
        voice.pause()

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild = ctx.guild)
    if voice.is_paused():
        voice.resume()

@bot.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        if message.author == bot.user:
            return
        await message.channel.send('Happy Birthday 🎉')

    if 'xD' in message.content:
        if message.author == bot.user:
            return
        await message.channel.send(':D')

    if message.content == 'say hi to me':
        await message.author.create_dm()
        await message.author.dm_channel.send(f'Hi')

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)