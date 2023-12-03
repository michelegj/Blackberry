import discord
import os
import platform
import json
import glob
import asyncio
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.all()
)

bot.remove_command('help')

with open('resources/token.json', 'r') as f:
    settings = json.loads(f.read())
    TOKEN = settings['blacktoken']

print(f"Blackberry Development Robot Running")
print(f"Running at Python {platform.python_version()}v, Discord.py {discord.__version__}v - "
      f"{platform.system()} {platform.release()} ({os.name})\n")


async def load():
    file_paths = [
        os.path.relpath(file_path, start=os.path.dirname(os.path.abspath(__file__)))
        for file_path in glob.glob('./cogs/**/*.py', recursive=True)
    ]

    for file_path in file_paths:
        cog_name = file_path.replace(os.sep, '.')[:-3]
        try:
            await bot.load_extension(cog_name)
        except commands.NoEntryPointError:
            print(f"Skipped loading extension '{cog_name}' as it does not have a 'setup' function")


async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
# -*- coding: utf-8 -*-
