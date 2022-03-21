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


#######################
async def use(ctx, duu=None):
    await open_acc(ctx.author)
    users = await get_bank()
    user = ctx.author
    if users[str(user.id)]["language"] == 0:
        if duu == None:
            await ctx.send("Which pickaxe do you want to use?")
            return
    if users[str(user.id)]["language"] >= 1:
        if duu == None:
            await ctx.send("Bạn muốn dùng cái cuốc nào?")
            return


    if users[str(user.id)]["language"] == 0:
        ngôn_ngữ_đ = "You have changed to using a"
        ngôn_ngữ_đ2 = "You are using a"
        ngôn_ngữ_đ3 = "You don't have a"
    if users[str(user.id)]["language"] >= 1:
        ngôn_ngữ_đ = "Bạn đã chuyển sang sử dụng"
        ngôn_ngữ_đ2 = "Bạn đang sử dụng"
        ngôn_ngữ_đ3 = "Bạn không có"

#dùng pickaxe
    if duu.lower() == "rock":
        if users[str(user.id)]["pickaxe1"] >= 2:
            await ctx.send(f"{ngôn_ngữ_đ2} {pickaxe1}rock pickaxe")
            return
        if users[str(user.id)]["pickaxe1"] < 1:
            await ctx.send(f"{ngôn_ngữ_đ3} {pickaxe1}rock pickaxe")
            return

        if users[str(user.id)]["pickaxe1"] == 1:
            await ctx.send(f"{ngôn_ngữ_đ} {pickaxe1}rock pickaxe")
            users[str(user.id)]["pickaxe1"] = 2
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)
        
        if users[str(user.id)]["pickaxe2"] == 2:
            users[str(user.id)]["pickaxe2"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe3"] == 2:
            users[str(user.id)]["pickaxe3"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe4"] == 2:
            users[str(user.id)]["pickaxe4"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe5"] == 2:
            users[str(user.id)]["pickaxe5"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe6"] == 2:
            users[str(user.id)]["pickaxe6"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe2"] == 1:
            pass
        if users[str(user.id)]["pickaxe3"] == 1:
            pass
        if users[str(user.id)]["pickaxe4"] == 1:
            pass
        if users[str(user.id)]["pickaxe5"] == 1:
            pass
        if users[str(user.id)]["pickaxe6"] == 1:
            pass
        return

    if duu.lower() == "copper":
        if users[str(user.id)]["pickaxe2"] >= 2:
            await ctx.send(f"{ngôn_ngữ_đ2} {pickaxe2}copper pickaxe")
            return
        if users[str(user.id)]["pickaxe2"] < 1:
            await ctx.send(f"{ngôn_ngữ_đ3} {pickaxe2}copper pickaxe")
            return

        if users[str(user.id)]["pickaxe2"] == 1:
            await ctx.send(f"{ngôn_ngữ_đ} {pickaxe2}copper pickaxe")
            users[str(user.id)]["pickaxe2"] = 2
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 2:
            users[str(user.id)]["pickaxe1"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)


        if users[str(user.id)]["pickaxe3"] == 2:
            users[str(user.id)]["pickaxe3"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe4"] == 2:
            users[str(user.id)]["pickaxe4"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe5"] == 2:
            users[str(user.id)]["pickaxe5"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe6"] == 2:
            users[str(user.id)]["pickaxe6"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 1:
            pass
        if users[str(user.id)]["pickaxe3"] == 1:
            pass
        if users[str(user.id)]["pickaxe4"] == 1:
            pass
        if users[str(user.id)]["pickaxe5"] == 1:
            pass
        if users[str(user.id)]["pickaxe6"] == 1:
            pass
        return

    if duu.lower() == "iron":
        if users[str(user.id)]["pickaxe3"] >= 2:
            await ctx.send(f"{ngôn_ngữ_đ2} {pickaxe3}iron pickaxe")
            return
        if users[str(user.id)]["pickaxe3"] < 1:
            await ctx.send(f"{ngôn_ngữ_đ3} {pickaxe3}iron pickaxe")
            return

        if users[str(user.id)]["pickaxe3"] == 1:
            await ctx.send(f"{ngôn_ngữ_đ} {pickaxe3}iron pickaxe")
            users[str(user.id)]["pickaxe3"] = 2
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 2:
            users[str(user.id)]["pickaxe1"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe2"] == 2:
            users[str(user.id)]["pickaxe2"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe4"] == 2:
            users[str(user.id)]["pickaxe4"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe5"] == 2:
            users[str(user.id)]["pickaxe5"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe6"] == 2:
            users[str(user.id)]["pickaxe6"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 1:
            pass
        if users[str(user.id)]["pickaxe2"] == 1:
            pass
        if users[str(user.id)]["pickaxe4"] == 1:
            pass
        if users[str(user.id)]["pickaxe5"] == 1:
            pass
        if users[str(user.id)]["pickaxe6"] == 1:
            pass
        return

    if duu.lower() == "gold":
        if users[str(user.id)]["pickaxe4"] >= 2:
            await ctx.send(f"{ngôn_ngữ_đ2} {pickaxe4}gold pickaxe")
            return
        if users[str(user.id)]["pickaxe4"] < 1:
            await ctx.send(f"{ngôn_ngữ_đ3} {pickaxe4}gold pickaxe")
            return
            
        if users[str(user.id)]["pickaxe4"] == 1:
            await ctx.send(f"{ngôn_ngữ_đ} {pickaxe4}gold pickaxe")
            users[str(user.id)]["pickaxe4"] = 2
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 2:
            users[str(user.id)]["pickaxe1"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe2"] == 2:
            users[str(user.id)]["pickaxe2"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe3"] == 2:
            users[str(user.id)]["pickaxe3"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe5"] == 2:
            users[str(user.id)]["pickaxe5"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe6"] == 2:
            users[str(user.id)]["pickaxe6"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 1:
            pass
        if users[str(user.id)]["pickaxe2"] == 1:
            pass
        if users[str(user.id)]["pickaxe3"] == 1:
            pass
        if users[str(user.id)]["pickaxe5"] == 1:
            pass
        if users[str(user.id)]["pickaxe6"] == 1:
            pass
        return

    if duu.lower() == "diamond":
        if users[str(user.id)]["pickaxe5"] >= 2:
            await ctx.send(f"{ngôn_ngữ_đ2} {pickaxe5}diamond pickaxe")
            return
        if users[str(user.id)]["pickaxe5"] < 1:
            await ctx.send(f"{ngôn_ngữ_đ3} {pickaxe5}diamond pickaxe")
            return
            
        if users[str(user.id)]["pickaxe5"] == 1:
            await ctx.send(f"{ngôn_ngữ_đ} {pickaxe5}diamond pickaxe")
            users[str(user.id)]["pickaxe5"] = 2
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 2:
            users[str(user.id)]["pickaxe1"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe2"] == 2:
            users[str(user.id)]["pickaxe2"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe3"] == 2:
            users[str(user.id)]["pickaxe3"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe4"] == 2:
            users[str(user.id)]["pickaxe4"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe6"] == 2:
            users[str(user.id)]["pickaxe6"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 1:
            pass
        if users[str(user.id)]["pickaxe2"] == 1:
            pass
        if users[str(user.id)]["pickaxe3"] == 1:
            pass
        if users[str(user.id)]["pickaxe4"] == 1:
            pass
        if users[str(user.id)]["pickaxe6"] == 1:
            pass
        return

    if duu.lower() == "obsidian":
        if users[str(user.id)]["pickaxe6"] >= 2:
            await ctx.send(f"{ngôn_ngữ_đ2} {pickaxe6}obsidian pickaxe")
            return
        if users[str(user.id)]["pickaxe6"] < 1:
            await ctx.send(f"{ngôn_ngữ_đ3} {pickaxe6}obsidian pickaxe")
            return
            
        if users[str(user.id)]["pickaxe6"] == 1:
            await ctx.send(f"{ngôn_ngữ_đ} {pickaxe6}obsidian pickaxe")
            users[str(user.id)]["pickaxe6"] = 2
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 2:
            users[str(user.id)]["pickaxe1"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe2"] == 2:
            users[str(user.id)]["pickaxe2"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe3"] == 2:
            users[str(user.id)]["pickaxe3"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe4"] == 2:
            users[str(user.id)]["pickaxe4"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe5"] == 2:
            users[str(user.id)]["pickaxe5"] = 1
            with open("rpg.json", "w") as f:
                json.dump(users, f, indent=4)

        if users[str(user.id)]["pickaxe1"] == 1:
            pass
        if users[str(user.id)]["pickaxe2"] == 1:
            pass
        if users[str(user.id)]["pickaxe3"] == 1:
            pass
        if users[str(user.id)]["pickaxe4"] == 1:
            pass
        if users[str(user.id)]["pickaxe5"] == 1:
            pass
        return

    else:
        if users[str(user.id)]["language"] == 0:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
            embed.add_field(name=f"There is no such pickaxe", value=f"-What kind of pickaxe do you want to switch to?\n-For details on how to change the pickaxe.\n-Please, write the command **mhow**")
            await ctx.send(embed=embed)
        if users[str(user.id)]["language"] >= 1:
            embed = discord.Embed(timestamp=ctx.message.created_at, color = discord.Color.red())
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{user.avatar_url}")
            embed.add_field(name=f"Không có cái cuốc như vậy", value=f"-Bạn muốn chuyển sang loại cuốc nào?\n-Để biết chi tiết về cách thay đổi cái cuốc.\n-Vui lòng viết lệnh **mhow**")
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