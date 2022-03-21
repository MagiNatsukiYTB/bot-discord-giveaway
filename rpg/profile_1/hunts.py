import discord
from discord.ext import commands
import random
import time
import json
import asyncio
from discord.utils import get
###################
snake = "<:snakes:950266413589868544>"
water_slime = "<:water_slime:950266435471564870>"
exp_slime = "<:exp_slime:950266444757737522>"
light_slime = "<:light_slime:950266455289630760>"
pilin = "<:pilin:950266475015462932>"
white_tiger = "<:white_tiger:950266500760076288>"

coin="<:coinss:945945122045067306>"
exxp = "<:exp:945951310027575316>"
trong = "<:trong:921038769874935910>"

#########################
async def hunt(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author

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

    loại_thú_săn = [
        f"{snake}",
        f"{water_slime}",
        f"{exp_slime}",
        f"{light_slime}",
        f"{pilin}",
        f"{white_tiger}"
    ]

    if users[str(user.id)]["health"] <= 0:
        users[str(user.id)]["health"] = 0
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)
            return

    săn = random.choice(loại_thú_săn)
    số_lượng = random.randint(1, 3)
    if săn == loại_thú_săn[0]:
        icon = loại_thú_săn[0]
        tên = "Snake"
        số_tiền = 30
        ha = "https://i.imgur.com/RiXPA8r.png"
        mất_máu = random.randint(0, 3)
        users[str(user.id)]["health"] -= mất_máu
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

    if săn == loại_thú_săn[1]:
        icon = loại_thú_săn[1]
        tên = "Water Slime"
        số_tiền = 35
        ha = "https://i.imgur.com/xoOcgOd.png"
        mất_máu = random.randint(0, 4)
        users[str(user.id)]["health"] -= mất_máu
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

    if săn == loại_thú_săn[2]:
        icon = loại_thú_săn[2]
        tên = "Exp Slime"
        số_tiền = 40
        ha = "https://i.imgur.com/QzpxDuJ.png"
        mất_máu = random.randint(1, 4)
        users[str(user.id)]["health"] -= mất_máu
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

    if săn == loại_thú_săn[3]:
        icon = loại_thú_săn[3]
        tên = "Light Slime"
        số_tiền = 42
        ha = "https://i.imgur.com/lmiasQI.png"
        mất_máu = random.randint(1, 5)
        users[str(user.id)]["health"] -= mất_máu
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

    if săn == loại_thú_săn[4]:
        icon = loại_thú_săn[4]
        tên = "Pilin"
        số_tiền = 45
        ha = "https://i.imgur.com/rRTKDRq.png"
        mất_máu = random.randint(1, 6)
        users[str(user.id)]["health"] -= mất_máu
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

    if săn == loại_thú_săn[5]:
        icon = loại_thú_săn[5]
        tên = "White Tiger"
        số_tiền = 50
        ha = "https://i.imgur.com/DJDhiIF.png"
        mất_máu = random.randint(1, 8)
        users[str(user.id)]["health"] -= mất_máu
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

    users[str(user.id)]["wallet"] += số_tiền*số_lượng
    with open("rpg.json", "w") as f:
        json.dump(users, f, indent=4)

    embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
    embed.add_field(name=f"You have hunted", value=f"+`{số_lượng} {tên}`{icon}\n+{eexxpp}\n+`{users[str(user.id)]['health']}`/`100`\n→**Level:** {users[str(user.id)]['lvl']}\n**Looking for a buyer**", inline=False)
    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
    embed.set_image(url=ha)
    a = await ctx.send(embed=embed)
    await asyncio.sleep(1.5)
    
    embed.clear_fields()
    embed.add_field(name=f"You sold {số_lượng} {tên}{icon}", value=f"+`{số_lượng} {tên}`{icon}\n+`{số_tiền*số_lượng}`{coin}\n+`{users[str(user.id)]['health']}`/`100`\n+{eexxpp}\n→**Level:** {users[str(user.id)]['lvl']}", inline=False)
    await a.edit(embed=embed)


########################
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