# egg code
import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix='!', intents=disnake.Intents.all())

@bot.event

async def on_message(message):

    if "egg" or "egG" or "eGG" or "EgG" or "EGG" or "eGg" or "EGg" or "Egg" in message.content:

        await message.add_reaction('🥚')

    await bot.process_commands(message)

@bot.event

async def on_ready():

    await bot.change_presence(activity=disnake.Activity(name='🥚', type=disnake.ActivityType.playing))

    print('Bot is ready')

bot.run('token')
