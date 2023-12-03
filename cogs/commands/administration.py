import discord
from discord.ext import commands


class AdministrationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="kick",
        description="Kick a user from the server",
        aliases=['k']
    )
    @commands.has_permissions(kick_members=True)
    async def _kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """
        Kick a user from the server
        :param member: The user to be kicked
        :param reason: Reason for the kick (optional)
        """
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked. Reason: {reason}")

    @commands.command(
        name="ban",
        description="Ban a user from the server",
        aliases=['b']
    )
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """
        Ban a user from the server
        :param member: The user to be banned
        :param reason: Reason for the ban (optional)
        """
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned. Reason: {reason}")

    @commands.command(
        name="clear",
        description="Clear a specified number of messages in the channel",
        aliases=['c']
    )
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount: int):
        """
        Clear a specified number of messages in the channel
        :param amount: The number of messages to clear
        """
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Cleared {amount} messages.")

    @commands.command(
        name="mute",
        description="Mute a user in the server",
        aliases=['m']
    )
    @commands.has_permissions(manage_roles=True)
    async def _mute(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """
        Mute a user in the server
        :param member: The user to be muted
        :param reason: Reason for the mute (optional)
        """
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(muted_role, send_messages=False)

        await member.add_roles(muted_role, reason=reason)
        await ctx.send(f"{member.mention} has been muted. Reason: {reason}")

    @commands.command(
        name="unmute",
        description="Unmute a user in the server",
        aliases=['um']
    )
    @commands.has_permissions(manage_roles=True)
    async def _unmute(self, ctx, member: discord.Member):
        """
        Unmute a user in the server
        :param member: The user to be unmuted
        """
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")

        if muted_role and muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(f"{member.mention} has been unmuted.")
        else:
            await ctx.send(f"{member.mention} is not muted.")


async def setup(bot):
    await bot.add_cog(AdministrationCog(bot))
