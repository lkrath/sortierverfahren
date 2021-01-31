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

    if message.content == '!join':
        channel = message.author.voice.channel
        await channel.connect()

#@bot.command(pass_context = True)
#async def join(ctx):
#    const connection = await message.member.voice.channel.join()
    #author = ctx.message.author
    #voice_channel 

@bot.command()
async def join(ctx):
    print('ok')
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(TOKEN)