import discord
from discord.ext import commands, tasks
from jishaku.cog import Jishaku  # Import the Jishaku cog

# Create an instance of the bot
bot = commands.Bot(command_prefix='a!')
bot.owner_ids = [847770840266833961]

# Load the Jishaku extension
bot.load_extension('jishaku')

# Event to print a message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

# Simple command to respond with a greeting
@bot.command(name='hello', help='Responds with a greeting')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot with your token
bot.run('MTIwNDIzMzMwNjg5MjQwMjY5OA.G-a1N1.UmYKAo_6M2ldB0ZjC1mV_AdRFqSrAeTX4yyu4A')
