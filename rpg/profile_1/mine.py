# from nis import cat
import re
import discord
from discord.ext import commands
import random
import time
import os
import json
import asyncio
from discord.utils import get
import DiscordUtils


######################
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

#cúp
pickaxe1 = "<:pickaxe1:945939722268721152>"
pickaxe2 = "<:pickaxe2:945939722293882940>"
pickaxe3 = "<:pickaxe3:945939761502244914>"
pickaxe4 = "<:pickaxe4:945939774160642080>"
pickaxe5 = "<:pickaxe5:946338341077528586>"
pickaxe6 = "<:pickaxe6:946338366847320116>"

#tiền
coin="<:coinss:945945122045067306>"
exxp = "<:exp:945951310027575316>"
trong = "<:trong:921038769874935910>"


######################
async def s(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author
    time.sleep(0)


#phân loại cúp
    if users[str(user.id)]["pickaxe1"] == 2:
        loại_cúp_bạn_đang_sử_dụng = pickaxe1
        loại_khoáng_sản_1 = [f"{rock}", f"{smooth_stone}", f"{đồng}"]
        tên_cúp = "**Rock pickaxe**"

        số_lượng_rock = random.randint(0, 10)
        if số_lượng_rock == 0:
            loại_khoáng_sản_1[0] = ""
            sa = ""
        if số_lượng_rock >= 1:
            sa = f"+`{số_lượng_rock} Rock`{loại_khoáng_sản_1[0]}\n"
            users[str(user.id)]["rock"] += số_lượng_rock
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_smoothstone = random.randint(0, 10)
        if số_lượng_smoothstone == 0:
            loại_khoáng_sản_1[1] = ""
            sas = ""
        if số_lượng_smoothstone >= 1:
            sas = f"+`{số_lượng_smoothstone} Smooth Stone`{loại_khoáng_sản_1[1]}\n"
            users[str(user.id)]["smoothstone"] += số_lượng_smoothstone
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_copper = random.randint(0, 10)
        if số_lượng_copper == 0:
            loại_khoáng_sản_1[2] = ""
            sass = ""
        if số_lượng_copper >= 1:
            sass = f"+`{số_lượng_copper} Copper`{loại_khoáng_sản_1[2]}"
            users[str(user.id)]["copper"] += số_lượng_copper
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


    if users[str(user.id)]["pickaxe2"] == 2:
        loại_cúp_bạn_đang_sử_dụng = pickaxe2
        loại_khoáng_sản_2 = [f"{đồng}", f"{sắt}", f"{vàng}"]
        tên_cúp = "**Copper pickaxe**"


        số_lượng_copper = random.randint(0, 10)
        if số_lượng_copper == 0:
            loại_khoáng_sản_2[0] = ""
            sa = ""
        if số_lượng_copper >= 1:
            sa = f"+`{số_lượng_copper} Copper`{loại_khoáng_sản_2[0]}\n"
            users[str(user.id)]["copper"] += số_lượng_copper
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_sắt = random.randint(0, 10)
        if số_lượng_sắt == 0:
            loại_khoáng_sản_2[1] = ""
            sas = ""
        if số_lượng_sắt >= 1:
            sas = f"+`{số_lượng_sắt} Iron`{loại_khoáng_sản_2[1]}\n"
            users[str(user.id)]["iron"] += số_lượng_sắt
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_vàng = random.randint(0, 10)
        if số_lượng_vàng == 0:
            loại_khoáng_sản_2[2] = ""
            sass = ""
        if số_lượng_vàng >= 1:
            sass = f"+`{số_lượng_vàng} Gold`{loại_khoáng_sản_2[2]}"
            users[str(user.id)]["gold"] += số_lượng_vàng
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


    if users[str(user.id)]["pickaxe3"] == 2:
        loại_cúp_bạn_đang_sử_dụng = pickaxe3
        loại_khoáng_sản_3 = [f"{sắt}", f"{vàng}", f"{diamond}"]
        tên_cúp = "**Iron pickaxe**"


        số_lượng_sắt = random.randint(0, 10)
        if số_lượng_sắt == 0:
            loại_khoáng_sản_3[0] = ""
            sa = ""
        if số_lượng_sắt >= 1:
            sa = f"+`{số_lượng_sắt} Iron`{loại_khoáng_sản_3[0]}\n"
            users[str(user.id)]["iron"] += số_lượng_sắt
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_vàng = random.randint(0, 10)
        if số_lượng_vàng == 0:
            loại_khoáng_sản_3[1] = ""
            sas = ""
        if số_lượng_vàng >= 1:
            sas = f"+`{số_lượng_vàng} Gold`{loại_khoáng_sản_3[1]}\n"
            users[str(user.id)]["gold"] += số_lượng_vàng
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_diamond = random.randint(0, 10)
        if số_lượng_diamond == 0:
            loại_khoáng_sản_3[2] = ""
            sass = ""
        if số_lượng_diamond >= 1:
            sass = f"+`{số_lượng_diamond} Diamond`{loại_khoáng_sản_3[2]}"
            users[str(user.id)]["diamond"] += số_lượng_diamond
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


    if users[str(user.id)]["pickaxe4"] == 2:
        loại_cúp_bạn_đang_sử_dụng = pickaxe4
        loại_khoáng_sản_4 = [f"{diamond}", f"{ruby}", f"{glowstone}"]
        tên_cúp = "**Gold pickaxe**"


        số_lượng_diamond = random.randint(0, 10)
        if số_lượng_diamond == 0:
            loại_khoáng_sản_4[0] = ""
            sa = ""
        if số_lượng_diamond >= 1:
            sa = f"+`{số_lượng_diamond} Diamond`{loại_khoáng_sản_4[0]}\n"
            users[str(user.id)]["diamond"] += số_lượng_diamond
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_ruby = random.randint(0, 7)
        if số_lượng_ruby == 0:
            loại_khoáng_sản_4[1] = ""
            sas = ""
        if số_lượng_ruby >= 1:
            sas = f"+`{số_lượng_ruby} Ruby`{loại_khoáng_sản_4[1]}\n"
            users[str(user.id)]["ruby"] += số_lượng_ruby
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_glowstone = random.randint(0, 7)
        if số_lượng_glowstone == 0:
            loại_khoáng_sản_4[2] = ""
            sass = ""
        if số_lượng_glowstone >= 1:
            sass = f"+`{số_lượng_glowstone} Glow Stone`{loại_khoáng_sản_4[2]}"
            users[str(user.id)]["glowstone"] += số_lượng_glowstone
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


    if users[str(user.id)]["pickaxe5"] == 2:
        loại_cúp_bạn_đang_sử_dụng = pickaxe5
        loại_khoáng_sản_5 = [f"{glowstone}", f"{magma}", f"{obsidian}"]
        tên_cúp = "**Diamond pickaxe**"


        số_lượng_glowstone = random.randint(0, 7)
        if số_lượng_glowstone == 0:
            loại_khoáng_sản_5[0] = ""
            sa = ""
        if số_lượng_glowstone >= 1:
            sa = f"+`{số_lượng_glowstone} Glow Stone`{loại_khoáng_sản_5[0]}\n"
            users[str(user.id)]["glowstone"] += số_lượng_glowstone
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_magma = random.randint(0, 5)
        if số_lượng_magma == 0:
            loại_khoáng_sản_5[1] = ""
            sas = ""
        if số_lượng_magma >= 1:
            sas = f"+`{số_lượng_magma} Magma`{loại_khoáng_sản_5[1]}\n"
            users[str(user.id)]["magma"] += số_lượng_magma
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_obsidian = random.randint(0, 5)
        if số_lượng_obsidian == 0:
            loại_khoáng_sản_5[2] = ""
            sass = ""
        if số_lượng_obsidian >= 1:
            sass = f"+`{số_lượng_obsidian} Obsidian`{loại_khoáng_sản_5[2]}"
            users[str(user.id)]["obsidian"] += số_lượng_obsidian
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


    if users[str(user.id)]["pickaxe6"] == 2:
        loại_cúp_bạn_đang_sử_dụng = pickaxe6
        loại_khoáng_sản_6 = [f"{moon_stone}", f"{obsidian_moon}", f"{stone_ancestor}"]
        tên_cúp = "**Obsidian pickaxe**"


        số_lượng_moon_stone = random.randint(0, 5)
        if số_lượng_moon_stone == 0:
            loại_khoáng_sản_6[0] = ""
            sa = ""
        if số_lượng_moon_stone >= 1:
            sa = f"+`{số_lượng_moon_stone} Moon Stone`{loại_khoáng_sản_6[0]}\n"
            users[str(user.id)]["moonstone"] += số_lượng_moon_stone
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_obsidian_moon = random.randint(0, 5)
        if số_lượng_obsidian_moon == 0:
            loại_khoáng_sản_6[1] = ""
            sas = ""
        if số_lượng_obsidian_moon >= 1:
            sas = f"+`{số_lượng_obsidian_moon} Obsidian Moon`{loại_khoáng_sản_6[1]}\n"
            users[str(user.id)]["obsidianmoon"] += số_lượng_obsidian_moon
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        số_lượng_stone_ancestor = random.randint(0, 1)
        if số_lượng_stone_ancestor == 0:
            loại_khoáng_sản_6[2] = ""
            sass = ""
        if số_lượng_stone_ancestor >= 1:
            sass = f"+`{số_lượng_stone_ancestor} Stone Ancestor`{loại_khoáng_sản_6[2]}"
            users[str(user.id)]["stoneancestor"] += số_lượng_stone_ancestor
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


#exp
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


#embed
    if users[str(user.id)]["language"] == 0:
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"You have mined the following ores: ", value=f"{eexxpp}{sa}{sas}{sass}{trong}", inline=False)
        embed.add_field(name="You are using pickaxe type:", value=f"→{loại_cúp_bạn_đang_sử_dụng}{tên_cúp}\n→Level: **{users[str(user.id)]['lvl']}**", inline=False)
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed.set_footer(text=f"{trong}") 
        await ctx.send(embed=embed)

    if users[str(user.id)]["language"] >= 1:
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Bạn đã khai thác các khoáng sản sau: ", value=f"{eexxpp}{sa}{sas}{sass}{trong}", inline=False)
        embed.add_field(name="Bạn đang sử dụng loại cúp", value=f"→{loại_cúp_bạn_đang_sử_dụng}{tên_cúp}\n→Level: **{users[str(user.id)]['lvl']}**", inline=False)
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
        # embed.set_footer(text=f"{trong}") 
        await ctx.send(embed=embed)


######################
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