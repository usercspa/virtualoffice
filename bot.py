# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    random_message = [
        'I\'m the human form of the 💯 ^100 emoji.',
        'Meowpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'undoubtedly awesomenes.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(random_message)
        await message.channel.send(response)
        
client = CustomClient()

client.run(TOKEN)