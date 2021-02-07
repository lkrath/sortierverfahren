#neu weil anderes zu unordentlich

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event 
async def on_ready():
    print(f'{bot.user.name} has connected to Discord')
    channel = bot.get_channel(799670616381849643)
    await channel.send('HI')

@bot.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        if message.author == bot.user:
            return
        await message.channel.send('Happy Birthday 🎉')

    if message.content == 'say hi to me':
        await message.author.create_dm()
        await message.author.dm_channel.send(f'Hi')

@bot.command(pass_context = True)
async def yt(ctx, url):
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await bot.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()


bot.run(TOKEN)