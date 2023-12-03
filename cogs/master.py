import discord
from discord.ext import commands
from cogs.managers.helper import get_london_time


class MasterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Signed as {self.bot.user} with {len(self.bot.guilds)} guilds at {get_london_time()}")

        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="messages"
            )
        )

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"Joined new guild {guild.name} ({guild.id}) at {get_london_time()}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"Left guild {guild.name} ({guild.id}) at {get_london_time()}")


async def setup(bot):
    await bot.add_cog(MasterCog(bot))
