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


########################
#cúp
pickaxe1 = "<:pickaxe1:945939722268721152>"
pickaxe2 = "<:pickaxe2:945939722293882940>"
pickaxe3 = "<:pickaxe3:945939761502244914>"
pickaxe4 = "<:pickaxe4:945939774160642080>"
pickaxe5 = "<:pickaxe5:946338341077528586>"
pickaxe6 = "<:pickaxe6:946338366847320116>"

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


##################################
async def profile(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author

    if users[str(user.id)]["wallet"] >0:
        wallet_amount = users[str(user.id)]["wallet"]
        coins = coin
    if users[str(user.id)]["wallet"] <=0:
        wallet_amount = "0"
        coins = coin
    

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


    máu = users[str(user.id)]["health"]
    lvls = users[str(user.id)]["lvl"]
    dame = users[str(user.id)]["dame"]
    defence = users[str(user.id)]["defence"]

    if users[str(user.id)]["health"] >= 100:
        a = f"{thanhmau2*10}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health** `{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP** `{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=90 <100:
        a = f"{thanhmau2*9}{thanhmautrong}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=80 <90:
        a = f"{thanhmau2*8}{thanhmautrong*2}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=70 <80:
        a = f"{thanhmau2*7}{thanhmautrong*3}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=60 <70:
        a = f"{thanhmau2*6}{thanhmautrong*4}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=50 <60:
        a = f"{thanhmau2*5}{thanhmautrong*5}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=40 <50:
        a = f"{thanhmau2*4}{thanhmautrong*6}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=30 <40:
        a = f"{thanhmau2*3}{thanhmautrong*7}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=20 <30:
        a = f"{thanhmau2*2}{thanhmautrong*8}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] >=10 <20:
        a = f"{thanhmau2*1}{thanhmautrong*9}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        await ctx.send(embed=embed)
        return
    if users[str(user.id)]["health"] <10:
        a = f"{thanhmau2*0}{thanhmautrong*10}"
        embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
        embed.add_field(name=f"Achievements", value=f"{trái_tim} **Health**`{máu}`**/**`100`\n{thanhmau1}{a}\n"
                                            f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*10}\n", inline=True)

        embed.add_field(name=f"Profile", value=f"{coins}**Coin**\n`{wallet_amount}`\n:medal:**Level**\n`{lvls}`", inline=True)

        embed.add_field(name=f"Fight", value=f":shield:**Defence**\n`{defence}`\n:crossed_swords:**Dame**\n`{dame}`", inline=True)
        embed.set_author(name=f"{ctx.author.name}'s Profile", icon_url=f"{user.avatar_url}")
        embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
        # embed.set_footer(text=f"{trong}")
        await ctx.send(embed=embed)
        return


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