import discord
from discord.ext import commands
import random
import asyncio
import os
import json


##########################################
os.chdir("E:\\lt\\bot")
prefixes = "g"
client = commands.Bot(command_prefix = prefixes)
client.remove_command("help")
TOKEN = "Tự thêm"


###########################################
@client.event
async def on_ready():
    print(f'Bot {client.user.name} đã hoạt động')
    await client.wait_until_ready()
    sta = ['Magi Natsuki', '-help[-h]',f'Với {len(client.guilds)} máy chủ']
    while not client.is_closed():
        a = random.choice(sta)
        await client.change_presence(activity=discord.Streaming(name=a, url='https://www.twitch.tv/your_channel_here'))
        await asyncio.sleep(5)


#########################################
@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def giveaway(ctx, time:int, loại_time=None, *,prize:str):
    try:
        if loại_time == None:
            await ctx.send("You need to enter time type and have time types: **s, m, h, d**")

        if prize == None:
            await ctx.send("You need to enter the prize")

        embed = discord.Embed(title=":gift:Giveaway!",colour=discord.Colour.red())
        embed.add_field(name=f"**{prize}**!!", value=f"React:gift:to join\nTime left: {time}{loại_time}\nHosted by: {ctx.author.mention}")

        if loại_time == "s":
            gawtime = time * 1

        if loại_time == "m":
            gawtime = time * 60

        if loại_time == "h":
            gawtime = time * 3600

        if loại_time == "d":
            gawtime = time * 86400

        embed.set_footer(text=f"Giveaway ends in {time}{loại_time}")

        with open('channel.json', 'r') as f:
            channels = json.load(f)

        gaw_msg = await client.get_channel(channels[str(ctx.guild.id)]).send(embed=embed)
        await gaw_msg.add_reaction("🎉")
        await ctx.message.delete()
        await asyncio.sleep(gawtime)
        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)
        users = await new_gaw_msg.reactions[0].users().flatten()
        users.pop(users.index(client.user))
        winner = random.choice(users)
        embed.clear_fields()
        embed.add_field(name="Winner!!", value=f"{winner.mention}\nHosted by: {ctx.author.mention}")
        await gaw_msg.edit(embed=embed)
        await ctx.send(f"Winner!! {winner.mention} won {prize}!")
    except:
        await ctx.send("pjoingiveaway to connect giveaway with channel to create giveaway")

@client.command()
async def joingiveaway(ctx):
    with open('channel.json', 'r') as f:
        channels = json.load(f)
    
    idchannel = ctx.channel.id

    channels[str(ctx.guild.id)] = idchannel
    with open('channel.json', 'w') as f:
        json.dump(channels, f, indent=4)
    await ctx.send("Connected to the channel")

@client.command()
async def help_giveaway(ctx):
    embed = discord.Embed(title="Help Giveaway",colour=discord.Colour.red())
    embed.add_field(name=f"Create and start new giveaway. For requirements, you need to create task first!",
    value=f"**There are time types:**\n`s, m, h, d`\n\n**Structure command and For Example:**\n```CSS\npgiveaway [time] [kind of time] [prize]\npgiveaway 1 s 100owo\npgiveaway 12 m 300coin```")
    await ctx.send(embed=embed)


##########################
client.run(TOKEN)