# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()
#guild = discord.utils.get(client.guilds, name=SERVER)

#@client.event
#async def on_ready():
#    guild = discord.utils.get(client.guilds, name=SERVER)
#    print(
#        f'{client.user} is connected to the following server:\n'
#        f'{guild.name} (id: {guild.id})'
#    )

# Zeigt nur den bot namen an

#
#    members = '\n - '.join([member.name for member in guild.members])
#    print(f'Server Members:\n - {members}')


@client.event 
async def on_ready():
    print(f'{client.user.name} has connected to Discord')
    #channel = discord.utils.get(guild.text_channels, name="general")
    #await channel.send('HI')
    channel = client.get_channel(799670616381849643)
    await channel.send('HI')

# funktioniert nicht
@client.event
async def on_member_join(member):    
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if 'happy birthday' in message.content.lower():
        if message.author == client.user:
            return
        await message.channel.send('Happy Birthday 🎉')

    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

        
client.run(TOKEN)
