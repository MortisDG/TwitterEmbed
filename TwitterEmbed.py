# Fix twitter/x Embeds.
# By Mortis / Discord: @mortisdg
import discord
from discord.ext import commands
import re

token = 'your_bot_token'
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message contains a Twitter or x.com link
    twitter_match = re.search(r'https?://twitter\.com/(\S+)', message.content)
    x_match = re.search(r'https?://x\.com/(\S+)', message.content)

    if twitter_match:
        modified_link = f'https://vx{twitter_match.group(1)}'
        remaining_text = re.sub(r'https?://twitter\.com/\S+', '', message.content)
        await message.channel.send(f'{modified_link}\nSent by **{message.author.display_name}**\nMessage:{remaining_text}')
        await message.delete()

    elif x_match:
        modified_link = f'https://fixvx.com/{x_match.group(1)}'
        remaining_text = re.sub(r'https?://x\.com/\S+', '', message.content)
        await message.channel.send(f'{modified_link}\nSent by **{message.author.display_name}**\nMessage:{remaining_text}')
        await message.delete()

    await bot.process_commands(message)

bot.run(token)