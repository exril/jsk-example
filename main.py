import discord
from discord.ext import commands
from jishaku.cog import Jishaku

# Create an instance of the bot
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event to print a message when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    await bot.wait_until_ready()  # Wait until the bot is fully ready before loading extensions
    bot.load_extension('jishaku')  # Load the Jishaku extension

# Set the bot owner(s) ID(s)
bot.owner_ids = {847770840266833961}  # Replace with your owner ID(s)

# Simple command to respond with a greeting
@bot.command(name='hello', help='Responds with a greeting')
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot with your token
bot.run('MTIwNDIzMzMwNjg5MjQwMjY5OA.G3XaQp.9JccFarIEzWBcdC0ol0eNxC2fwSwZ7JUNfXRx0')
