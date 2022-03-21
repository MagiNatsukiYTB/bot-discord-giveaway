# @client.command()
# async def ketnoi(ctx):
#     with open('channel.json', 'r') as f:
#         channels = json.load(f)
    
#     idchannel = ctx.channel.id

#     channels[str(ctx.channel.id)] = idchannel
#     with open('channel.json', 'w') as f:
#         json.dump(channels, f, indent=4)


# @client.command()
# async def đánh_giá(ctx, danhgia:int):
#     user = ctx.author
#     if danhgia >5:
#         await ctx.send("Bạn đánh giá ko hợp lệ. Đánh giá tối đa 5 sao")
#         return

#     if danhgia <0:
#         await ctx.send("Bạn đánh giá ko hợp lệ. Đánh giá tối đa 5 sao")
#         return

#     if danhgia >=0 <=5:
#         with open('channel.json', 'r') as f:
#             channels = json.load(f)
        
#         channels[str(user.id)] = danhgia
#         with open('channel.json', 'w') as f:
#             json.dump(channels, f, indent=4)
#         await ctx.send(f"Bạn đã đánh giá bot {danhgia} sao")
#         return