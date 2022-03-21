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
#####################
exxp = "<:exp:945951310027575316>"
trong = "<:trong:921038769874935910>"
expthanh1 = "<:expthanh1:946971108295458916>"
expthanh2 = "<:expthanh2:946971108316442634>"
thanhmautrong = "<:thanhmautrong:946966723100307546>"


######################
async def level(ctx):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author

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


    embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
    embed.add_field(name=f"Achievements", value=f"{exxp} **XP**`{users[str(user.id)]['exp']}`**/**`{users[str(user.id)]['exp_after']}`\n{expthanh1}{expthanh2*5}", inline=False)
    embed.add_field(name=f"Profile", value=f":medal:**Level**\n`{users[str(user.id)]['lvl']}`", inline=False)
    embed.set_author(name=f"{ctx.author.name}'s level", icon_url=f"{user.avatar_url}")
    embed.set_thumbnail(url="https://i.imgur.com/kYW2xJp.png")
    # embed.set_footer(text=f"{trong}")
    await ctx.send(embed=embed)


###########################
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