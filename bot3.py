# noch ein versuch

import discord 
import os
from dotenv import load_dotenv
from discord.ext import commands
from youtube_dl import YoutubeDL
from discord.utils import get
from discord import FFmpegPCMAudio

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    #if not voice.is_connected():
    await channel.connect()

@bot.command()
async def leave(ctx):
    #channel = ctx.author.voice.channel
    #if voice.is_connected():
    #await channel.disconnect()
    server = ctx.message.guild.voice_client
    await server.disconnect()
    
@bot.command()
async def yt(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
    else:
        await ctx.send("Already playing song")
        return

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

    if message.content == 'bonk':
        await message.channel.send('horny jail')   

    if message.content == 'say hi to me':
        await message.author.create_dm()
        await message.author.dm_channel.send(f'Hi')

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)