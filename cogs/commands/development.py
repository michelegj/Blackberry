import discord
from discord.ext import commands
from cogs.managers.helper import get_london_time


class DevelopmentCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command(
        name="shutdown",
        description="terminate robot activity",
        aliases=['stop'],
        hidden=True
    )
    async def _shutdown(self, ctx):
        """
        Terminate robot activity
        :param none:
        """
        await ctx.send(f"Raspberry shutdown at **{get_london_time()}**!")
        print(f"Raspberry shutdown at {get_london_time()}!")
        await ctx.message.delete()
        await self.bot.close()

    @commands.is_owner()
    @commands.command(
        name="say",
        description="repeats a message",
        hidden=True
    )
    async def _say(self, ctx, *, message: str):
        """
        Repeats a message
        :param message: the message to be repeated
        """
        message = message.replace("\\n", "\n")
        await ctx.message.delete()
        await ctx.send(message)

    @commands.is_owner()
    @commands.command(
        name="edit",
        description="Edit the bot message",
        hidden=True
    )
    async def _edit(self, ctx, message_id: int, *, new_message: str):
        """
        Edit the bot message
        :param message_id: ID of the message to edit
        :param new_message: the new content for the message
        """
        await ctx.message.delete()
        try:
            message_to_edit = await ctx.fetch_message(message_id)
        except discord.NotFound:
            await ctx.send(f"Message ({message_id}) not found!", delete_after=30)
            return
        await message_to_edit.edit(content=new_message)


async def setup(bot):
    await bot.add_cog(DevelopmentCog(bot))
