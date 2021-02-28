#neu weil anderes zu unordentlich

import os
import discord
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

bot.run(TOKEN)

@bot.event 
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')
    channel = bot.get_channel(799670616381849643)
    await channel.send('Hi')

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
    #if message.content == '!leave':
    #    channel = message.author.voice.channel
        #if voice.is_connected():
    #    await channel.disconnect()

#    if message.content == 

@bot.command()
#@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.author.voice.channel
    #if not voice.is_connected():
    await channel.connect()

#@bot.command(pass_context = True)
#async def leave(ctx):
#    channel = ctx.author.voice.channel
    #if voice.is_connected():
#    await channel.disconnect()

#@bot.command(pass_context = True)
#async def yt(ctx, url):
#    guild = ctx.message.guild

#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        file = ydl.extract_info(url, download=True)
#        path = str(file['title']) + "-" + str(file['id'] + ".mp3")

#    voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
#    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

#    await ctx.send(f'**Music: **{url}')

#@bot.command(pass_context = True)
#async def yt(ctx, url:str):
#    vc = discord.utils.get(ctx.guild.voice_channels, name = 'General')
#    voice = discord.utils.get(client.voice_client, guild = guild.ctx)
#    await vc.connect()

bot.run(TOKEN)