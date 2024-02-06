import discord
from discord.ext import commands
from jishaku.cog import Jishaku
import tracemalloc  

tracemalloc.start()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')
    await bot.change_presence(activity=discord.Game(name="awarebot.pro/invite"))
    await bot.wait_until_ready() 
    await bot.load_extension('jishaku') 
bot.owner_ids = {847770840266833961} 

@bot.command(name='web', help='Responds with a greeting')
async def hello(ctx):
    await ctx.send(f'https://awarebot.pro/invite')

bot.run('MTIwNDIzMzMwNjg5MjQwMjY5OA.G3XaQp.9JccFarIEzWBcdC0ol0eNxC2fwSwZ7JUNfXRx0')
