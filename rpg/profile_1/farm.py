import re
from turtle import width
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
#normal fruit
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

#magic fruit
herbal_stone_ring = "<:herbal_stone_ring:946352883975204914>"
flying_cucumber = "<:flying_cucumber:946352883916501083>"
flying_potatoes = "<:flying_potatoes:946352883710976061>"

ganoderma = "<:ganoderma:946352883966820382>"
purple_sweet_potato = "<:purple_sweet_potato:946352883971031050>"

red_grapes = "<:red_grapes:946352883765489726>"
crocodile_foot_herb = "<:crocodile_foot_herb:946352883920691230>"

#hoe
wood_hoe = "<:wood_hoe:947384545156669550>"
rock_hoe = "<:rock_hoe:947384556569391115>"
iron_hoe = "<:iron_hoe:947384570704166962>"
gold_hoe = "<:gold_hoe:947384901118853142>"
diamond_hoe = "<:diamond_hoe:947384936804003890>"
obsidian_hoe = "<:obsidian_hoe:947384949969920011>"

#lặt vặt
trong = "<:trong:921038769874935910>"
exxp = "<:exp:945951310027575316>"


############################
async def harvest(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author

    if users[str(user.id)]["hoe"] == 1:
      loại_lương_thực = [f'{orange}', f'{apple}', f'{pear}']
      loại_hoe = wood_hoe
      tên_hoe = "**Wood Hoe**"

      thu_hoạch_đc_số_lượng_orange = random.randint(0, 6)
      if thu_hoạch_đc_số_lượng_orange == 0:
        loại_lương_thực[0] = ""
        sa = ""
      if thu_hoạch_đc_số_lượng_orange > 0:
        sa = f"+`{thu_hoạch_đc_số_lượng_orange} orange` {loại_lương_thực[0]}\n"
        users[str(user.id)]["orange"] += thu_hoạch_đc_số_lượng_orange
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      thu_hoạch_đc_số_lượng_apple = random.randint(0, 6)
      if thu_hoạch_đc_số_lượng_apple == 0:
        loại_lương_thực[1] = ""
        sas = ""
      if thu_hoạch_đc_số_lượng_apple > 0:
        sas = f"+`{thu_hoạch_đc_số_lượng_apple} apple` {loại_lương_thực[1]}\n"
        users[str(user.id)]["apple"] += thu_hoạch_đc_số_lượng_apple
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      thu_hoạch_đc_số_lượng_pear = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_pear == 0:
        loại_lương_thực[2] = ""
        sass = ""
      if thu_hoạch_đc_số_lượng_pear > 0:
        sass = f"+`{thu_hoạch_đc_số_lượng_pear} pear` {loại_lương_thực[2]}\n"
        users[str(user.id)]["pear"] += thu_hoạch_đc_số_lượng_pear
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

      sasss = ""


    if users[str(user.id)]["hoe"] == 2:
      loại_lương_thực = [f'{watermelon}', f'{dragonfruit}', f'{grape}']
      loại_hoe = rock_hoe
      tên_hoe = "**Rock Hoe**"

      thu_hoạch_đc_số_lượng_watermelon = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_watermelon == 0:
        loại_lương_thực[0] = ""
        sa = ""
      if thu_hoạch_đc_số_lượng_watermelon > 0:
        sa = f"+`{thu_hoạch_đc_số_lượng_watermelon} watermelon` {loại_lương_thực[0]}\n"
        users[str(user.id)]["watermelon"] += thu_hoạch_đc_số_lượng_watermelon
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      thu_hoạch_đc_số_lượng_dragonfruit = random.randint(0, 5)
      if thu_hoạch_đc_số_lượng_dragonfruit == 0:
        loại_lương_thực[1] = ""
        sas = ""
      if thu_hoạch_đc_số_lượng_dragonfruit > 0:
        sas = f"+`{thu_hoạch_đc_số_lượng_dragonfruit} dragonfruit` {loại_lương_thực[1]}\n"
        users[str(user.id)]["dragonfruit"] += thu_hoạch_đc_số_lượng_dragonfruit
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      thu_hoạch_đc_số_lượng_grape = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_grape == 0:
        loại_lương_thực[2] = ""
        sass = ""
      if thu_hoạch_đc_số_lượng_grape > 0:
        sass = f"+`{thu_hoạch_đc_số_lượng_grape} grape` {loại_lương_thực[2]}"
        users[str(user.id)]["grape"] += thu_hoạch_đc_số_lượng_grape
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)
      
      sasss = ""


    if users[str(user.id)]["hoe"] == 3:
      loại_lương_thực = [f'{strawberry}', f'{blueberry}']
      loại_hoe = iron_hoe
      tên_hoe = "**Iron Hoe**"

      thu_hoạch_đc_số_lượng_strawberry = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_strawberry == 0:
        loại_lương_thực[0] = ""
        sa = ""
      if thu_hoạch_đc_số_lượng_strawberry > 0:
        sa = f"+`{thu_hoạch_đc_số_lượng_strawberry} strawberry` {loại_lương_thực[0]}\n"
        users[str(user.id)]["strawberry"] += thu_hoạch_đc_số_lượng_strawberry
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

      sas = ""

      thu_hoạch_đc_số_lượng_blueberry = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_blueberry == 0:
        loại_lương_thực[2] = ""
        sass = ""
      if thu_hoạch_đc_số_lượng_blueberry > 0:
        sass = f"+`{thu_hoạch_đc_số_lượng_blueberry} blueberry` {loại_lương_thực[2]}"
        users[str(user.id)]["blueberry"] += thu_hoạch_đc_số_lượng_blueberry
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

      sasss = ""


    if users[str(user.id)]["hoe"] == 4:
      loại_lương_thực = [f'{herbal_stone_ring}', f'{flying_cucumber}']
      loại_hoe = gold_hoe
      tên_hoe = "**Gold Hoe**"

      thu_hoạch_đc_số_lượng_herbal_stone_ring = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_herbal_stone_ring == 0:
        loại_lương_thực[0] = ""
        sa = ""
      if thu_hoạch_đc_số_lượng_herbal_stone_ring > 0:
        sa = f"+`{thu_hoạch_đc_số_lượng_herbal_stone_ring} herbal_stone_ring` {loại_lương_thực[0]}\n"
        users[str(user.id)]["herbal_stone_ring"] += thu_hoạch_đc_số_lượng_herbal_stone_ring
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      thu_hoạch_đc_số_lượng_flying_cucumber = random.randint(0, 5)
      if thu_hoạch_đc_số_lượng_flying_cucumber == 0:
        loại_lương_thực[1] = ""
        sas = ""
      if thu_hoạch_đc_số_lượng_flying_cucumber > 0:
        sas = f"+`{thu_hoạch_đc_số_lượng_flying_cucumber} flying_cucumber` {loại_lương_thực[1]}\n"
        users[str(user.id)]["flying_cucumber"] += thu_hoạch_đc_số_lượng_flying_cucumber
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      sass = ""

      sasss = ""


    if users[str(user.id)]["hoe"] == 5:
      loại_lương_thực = [f'{ganoderma}', f'{purple_sweet_potato}']
      loại_hoe = diamond_hoe
      tên_hoe = "**Diamond Hoe**"

      thu_hoạch_đc_số_lượng_ganoderma = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_ganoderma == 0:
        loại_lương_thực[0] = ""
        sa = ""
      if thu_hoạch_đc_số_lượng_ganoderma > 0:
        sa = f"+`{thu_hoạch_đc_số_lượng_ganoderma} ganoderma` {loại_lương_thực[0]}\n"
        users[str(user.id)]["ganoderma"] += thu_hoạch_đc_số_lượng_ganoderma
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      thu_hoạch_đc_số_lượng_purple_sweet_potato = random.randint(0, 5)
      if thu_hoạch_đc_số_lượng_purple_sweet_potato == 0:
        loại_lương_thực[1] = ""
        sas = ""
      if thu_hoạch_đc_số_lượng_purple_sweet_potato > 0:
        sas = f"+`{thu_hoạch_đc_số_lượng_purple_sweet_potato} purple_sweet_potato` {loại_lương_thực[1]}"
        users[str(user.id)]["purple_sweet_potato"] += thu_hoạch_đc_số_lượng_purple_sweet_potato
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

      sass = ""

      sasss = ""


    if users[str(user.id)]["hoe"] == 6:
      loại_lương_thực = [f'{red_grapes}', f'{crocodile_foot_herb}']
      loại_hoe = obsidian_hoe
      tên_hoe = "**Obsidian Hoe**"

      thu_hoạch_đc_số_lượng_red_grapes = random.randint(0, 4)
      if thu_hoạch_đc_số_lượng_red_grapes == 0:
        loại_lương_thực[0] = ""
        sa = ""
      if thu_hoạch_đc_số_lượng_red_grapes > 0:
        sa = f"+`{thu_hoạch_đc_số_lượng_red_grapes} red_grapes` {loại_lương_thực[0]}\n"
        users[str(user.id)]["red_grapes"] += thu_hoạch_đc_số_lượng_red_grapes
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)


      thu_hoạch_đc_số_lượng_crocodile_foot_herb = random.randint(0, 3)
      if thu_hoạch_đc_số_lượng_crocodile_foot_herb == 0:
        loại_lương_thực[1] = ""
        sas = ""
      if thu_hoạch_đc_số_lượng_crocodile_foot_herb > 0:
        sas = f"+`{thu_hoạch_đc_số_lượng_crocodile_foot_herb} crocodile_foot_herb` {loại_lương_thực[1]}"
        users[str(user.id)]["crocodile_foot_herb"] += thu_hoạch_đc_số_lượng_crocodile_foot_herb
        with open("rpg.json", "w") as f:
            json.dump(users, f, indent=4)

      sass = ""

      sasss = ""


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
      embed.add_field(name="Let's go to the mountain to pick some fruit", value="You're going up the mountain")
      a=await ctx.send(embed=embed)
      await asyncio.sleep(1.5)
      embed.clear_fields()
      embed.add_field(name=f"After going up the mountain you harvest: ", value=f"{eexxpp}{sa}{sas}{sass}{sasss}{trong}", inline=False)
      embed.add_field(name="You are using hoe type:", value=f"→{loại_hoe} {tên_hoe}\n→Level: **{users[str(user.id)]['lvl']}**", inline=False)
      embed.set_author(name=f"{ctx.author.name}'s harvest", icon_url=f"{user.avatar_url}")
      await a.edit(embed=embed)

    if users[str(user.id)]["language"] >= 1:
      embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
      embed.add_field(name="Lên núi hái quả nào", value="Bạn đang đi lên núi")
      a=await ctx.send(embed=embed)
      await asyncio.sleep(1.5)
      embed.clear_fields()
      embed.add_field(name=f"Sau khi lên núi, bạn thu hoạch: ", value=f"{eexxpp}{sa}{sas}{sass}{sasss}{trong}", inline=False)
      embed.add_field(name="Bạn đang sử dụng loại cuốc", value=f"→{loại_hoe} {tên_hoe}\n→Level: **{users[str(user.id)]['lvl']}**", inline=False)
      embed.set_author(name=f"{ctx.author.name}'s harvest", icon_url=f"{user.avatar_url}")
      await a.edit(embed=embed)


##########################
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