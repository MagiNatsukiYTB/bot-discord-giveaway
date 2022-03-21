import discord
from discord import File
from discord.ext import commands
import random
import time
import os
import json
import asyncio
import datetime
from io import BytesIO
#######################
async def unmute(ctx, member: discord.Member):
    try:
        if member == None:
            await ctx.send("**Please tag the person you want to unmute**")
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        await member.send(f"You have been Unmute: - {ctx.guild.name}")
        embed = discord.Embed(title="Unmute", description=f" {member.mention} has been removed Muted ",colour=discord.Colour.red())
        await ctx.send(embed=embed)   
    except:
        await ctx.send("you need to grant bot permission")

###########################
async def mute(ctx, member: discord.Member, time=None,*, reason=None):
    try:
        time_convert = {"s": 1, "m": 60, "h":3600, "d": 86400}
        seconds = int(time[0]) * time_convert[time[-1]]
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        if member == None:
            await ctx.send("**Please tag the person you want to mute**")
        if time == None:
            await ctx.send("**You need to enter the time**")
        embed = discord.Embed(title="Mute", description=f"{member.mention} was mute by {ctx.author.mention}\nTimes: {time}", colour=discord.Colour.red())
        embed.add_field(name="Reasons:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f"You have been muted from the server {guild.name}\nReason: {reason}\nTimes: {time}")
        await asyncio.sleep(seconds)
        await unmute(ctx=ctx, member=member)
    except:
        await ctx.send("you need to grant bot permission")

######################
async def ban(ctx, member: discord.Member = None, *, reason=None):
    try:
        if member == None:
            await ctx.send("**Please tag the person you want to ban**")
        else:
            await ctx.send(f"{member} got banned for brawling")
            await member.ban(reason=reason)
    except:
        await ctx.send("you need to grant bot permission")