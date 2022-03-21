import discord
from discord.ext import commands, tasks
import random
import time
import os
import json
import asyncio
import youtube_dl
from discord.utils import get
import DiscordUtils
from discord_buttons_plugin import *
from lyricsgenius import Genius


##################################
trong = "<:trong:921038769874935910>"
t112="▬"
play = "<:play:934976179885207562>"
stopppp = "<:stop:934979874429493289>"
logoo = "<:logomusic:934996839122501663>"
giaidi="<:giaidieu:934996556447363163>"
tainghe="<:tainghe:934997168073359370>"
tickkk = "<:tickkkk:934997492066574357>"
skipp="<:skip:937334580485185597>"
người_làm_bot = "© MAGI_NATSUKI#3206"


###################################
prefixes = "s!"
intents = discord.Intents.default()
intents = discord.Intents.all()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix = prefixes, intents=intents)
client.remove_command("help")
buttons = ButtonsClient(client)
TOKEN="ODk1OTkwODgyNTUyMTI3NDg5.YWAmiQ.358JLYCuFz4yRv4TD2wjNci7Vog"
genius_client = Genius(TOKEN)


#########################
#event
@client.event
async def on_ready():
    print(f'Bot {client.user.name} đã hoạt động')
    await client.wait_until_ready()
    sta = ['Magi and DuySino', 's!help[s!h]',f'Với {len(client.guilds)} máy chủ']
    while not client.is_closed():
        a = random.choice(sta)
        await client.change_presence(activity=discord.Streaming(name=a, url='https://www.twitch.tv/your_channel_here'))
        await asyncio.sleep(5)

def split(query):
    print("ĐÂY LÀ THÔNG ĐIỆP ĐÃ ĐƯỢC GỬI\n")
    array = query.split()
    return array 

def getSong(song_name):
    full_song_name = ""
    for i in range(1, len(song_name)):
        full_song_name += song_name[i] + " "
    songObj = genius_client.search_song(full_song_name)
    return songObj

def getArtist(artist_name):
    full_artist_name = ""
    for i in range(1, len(artist_name)):
        full_artist_name += artist_name[i] + " "
    artistObj = genius_client.search_artist(full_artist_name)
    return artistObj


@client.event
async def on_message(message):
    if message.author.bot == False:
        guild = message.guild
        print(f'Sv: {message.guild.name} Name: {message.author}\n')
    if message.content.startswith('s!lyrics'): 
        song_name = split(message.content)
        songObject = getSong(song_name)
        if(len(songObject.lyrics) >= 2000):
            await message.channel.send("**Đây là lời bài hát **" + "\n" + songObject.lyrics[0:1500] + "\n\n**Đây là liên kết đến của bài hát**" + "\n" + songObject.url)
            return
        await message.channel.send("**Đây là lời bài hát **" + "\n" + songObject.lyrics + "\n\n**Đây là liên kết đến của bài hát**" + "\n" + songObject.url)
    await client.process_commands(message)





#######################################
#bot discord music
youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {'options': '-vn'}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.duration = data.get('duration')
        self.download = data.get('download')
        self.video_url = data["webpage_url"]
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.uploader = data["uploader"] if "uploader" in data else ""
        self.thumbnail = data["thumbnail"] if "thumbnail" in data else None
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False, play=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(f"ytsearch:{url}", download=not stream or play))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

tasker = None
song_queue = []
timenhac = 0
np = None

@buttons.click
async def leaves(ctx):
  await ra(ctx=ctx)

@buttons.click
async def quanhac(ctx):
  await skip(ctx=ctx)

@buttons.click
async def danhsach(ctx):
  await danh_sách(ctx=ctx)

@buttons.click
async def stops(ctx):
  await stop(ctx=ctx)

@client.command(aliases=['join'])
async def vào(ctx):
  channel = ctx.message.author.voice.channel
  if not ctx.message.author.voice:
    await ctx.send(f"**{ctx.message.author.name} :warning:không được kết nối với một kênh thoại.**")
  else:
    await channel.connect()
    await ctx.send(f"Bot đã vào Kênh thoại **{channel}!**")

@client.command(aliases=['leave'])
async def ra(ctx):
    channel = ctx.message.author.voice.channel
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.reply(f":white_check_mark:Bot đã ra khỏi kênh thoại **{channel}.**")
    else:
        await ctx.reply("**:warning:Tôi hiện không ở trong một kênh thoại nào cả!**")

@client.command(aliases=['play'])
async def mở(ctx, *, url:str):
  global song_queue
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  try :
    if(voice == None):
      if not ctx.message.author.voice:
        await ctx.send(f"**{ctx.message.author.name} :warning:không được kết nối với một kênh thoại.**")
      else:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    async with ctx.typing():
      voice_client = ctx.message.guild.voice_client
      if not voice_client.is_playing():
        song_queue.clear()
      player = await YTDLSource.from_url(url, loop=client.loop, stream=True)
      if len(song_queue) == 0:
        await start_playing(ctx, player)
      else:
        song_queue.append(player)
        await ctx.send(f"{tickkk}**Vị trí {len(song_queue)-1}:** {player.title}")
  except Exception as e:
      print(f"{e}")

async def start_playing(ctx, player):
    voice_client = ctx.message.guild.voice_client
    channel = ctx.guild.voice_client.channel
    user = ctx.author
    global tasker
    global timenhac
    global song_queue
    song_queue.append(player)
    x = time.strftime('%M:%S', time.gmtime(timenhac))
    y = time.strftime('%H:%M:%S', time.gmtime(int(song_queue[0].duration)))
    if(song_queue[0] == None):
      return
    i = 0
    while i < len(song_queue):
          ctx.voice_client.play(song_queue[0], after=lambda e: print('Lỗi trình phát: %s' % e) if e else None)
          embed = discord.Embed(timestamp=ctx.message.created_at, color = (0xF76841))
          embed.add_field(name = f"Uploader: {song_queue[0].uploader}:", value =f"[{song_queue[0].title}]({song_queue[0].video_url})\n**[s!nowplaying: để điều khiển bài hát]**", inline=False)
          embed.set_thumbnail(url = song_queue[0].thumbnail)
          embed.set_footer(text=f"Reqest: {user}")
          embed.set_author(name="Music", icon_url="https://i.imgur.com/ZKbaIi2.gif")
          message = await ctx.send(embed=embed)
          await ctx.guild.change_voice_state(channel=channel, self_mute=False, self_deaf=True)
          while True:
            if not voice_client.is_playing():
                song_queue[0].duration -= song_queue[0].duration
                timenhac -= timenhac
                embed.add_field(name=f"Nhạc đã kết thúc:", value=f"{stopppp}{trong}[{t112*7}]({song_queue[0].video_url}){logoo}{trong}{y}", inline=False)
                await message.edit(embed=embed)
                break
            if voice_client.is_playing():
              await asyncio.sleep(1)
              timenhac += 1
              if x == y:
                 x-=x
                 timenhac = 0
                 break
              if timenhac >= int(song_queue[0].duration):
                 song_queue[0].duration -= song_queue[0].duration
                 timenhac = 0
                 break
          if(len(song_queue) > 0):
            song_queue.pop(0)

@client.command()
async def nowplaying(ctx):
    voice_client = ctx.message.guild.voice_client
    global song_queue
    global timenhac
    x = time.strftime('%H:%M:%S', time.gmtime(timenhac))
    y = time.strftime('%H:%M:%S', time.gmtime(int(song_queue[0].duration)))
    if voice_client.is_playing():
          embed = discord.Embed(timestamp=ctx.message.created_at, color = (0xF76841))
          embed.add_field(name = f"🎧**Uploader:**\n`{song_queue[0].uploader}`", value =f"> "
                                                                                f"\n❔**Views:**\n`{song_queue[0].views}`\n> "
                                                                                f"\n:thumbsup:**Like:**\n`{song_queue[0].likes}`")
          embed.add_field(name = "⏱**Duration:**", value=f"`{x} / {y}`\n> "
                                                          f"\n❔**Video:**\n[Click Me]({song_queue[0].video_url})\n> "
                                                          f"\n🔊**Volume:**\n`{ctx.voice_client.source.volume*100}%`")
          embed.set_thumbnail(url = song_queue[0].thumbnail)
          embed.set_author(name=song_queue[0].title, icon_url="https://i.imgur.com/ZKbaIi2.gif")
          await buttons.send(
            content=None,
            embed=embed,
            channel = ctx.channel.id,
            components = [
              ActionRow([
                Button(
                  style = ButtonType().Primary,
                  label = "▶️ Leave",
                  custom_id = "leaves",
                ),
                Button(
                  style = ButtonType().Success,
                  label = "⏭️ Skip",
                  custom_id = "quanhac"
                ),
                Button(
                  style = ButtonType().Danger,
                  label = "💎 Queue",
                  custom_id = "danhsach",
                ),
                Button(
                  style = ButtonType().Secondary,
                  label = "🏠 Stop",
                  custom_id = "stops",)])])
    if not voice_client.is_playing():
            await ctx.send("Chưa mở nhạc nha nhóc!")

async def coro(ctx,duration):
  await asyncio.sleep(duration)

@client.command(aliases=['queue'])
async def danh_sách(ctx):
    global song_queue
    a = ""
    i = 0
    for f in song_queue:
      if i > 0:
       a = a + str(i) +". " + f.title + "\n "
      i += 1
    await ctx.reply("**Bài hát được xếp hàng đợi: \n **" + a)

@client.command(aliases=['pause'])
async def dừng(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await ctx.reply(f"{stopppp}**Đã tạm dừng phát nhạc __{song_queue[0].title}__.**")
        voice_client.pause()
    else:
        await ctx.reply(f"{tickkk}**Bot đã dừng phát nhạc.**")
    
@client.command(aliases=['remuse'])
async def tiếp(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await ctx.reply(f"{play}**Đã tiếp tục mở phát nhạc __{song_queue[0].title}__.**")
        voice_client.resume()
    else:
        await ctx.reply(f"{tickkk}**Bot đang phát nhạc**")

@client.command()
async def stop(ctx):
    global tasker
    global song_queue
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        song_queue.clear()
        voice_client.stop()
        tasker.cancel()
        await ctx.reply(f"{stopppp}**Đã dừng phát nhạc __{song_queue[0].title}__.**")
    else:
        await ctx.reply(f"{tickkk}**Bot không phát bất cứ thứ gì vào lúc này.**")

@client.command()
async def skip(ctx):
    global tasker
    global song_queue
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()
        await ctx.reply(f"{stopppp}**Đã skip bài nhạc __{song_queue[0].title}__.**")
    else:
        await ctx.reply(f"{tickkk}**Bot không phát bất cứ thứ gì vào lúc này.**")

@client.command(aliases=['vol','volume'])
async def âm(ctx, volume: int):
    ctx.voice_client.source.volume = volume / 100
    await ctx.reply(f"Đã đổi âm lượng thành **{volume}%**")

@client.command(aliases=['h'])
async def help(ctx):
    embed = discord.Embed(timestamp=ctx.message.created_at, color = (0xF76841))
    embed.add_field(name="**:notes:Music Commands:notes:**", value="\n`s!join`: cho bot vào kênh"
                                                                   "\n`s!leave`: cho bot thoát kênh"
                                                                   "\n`s!play`: mở nhạc"
                                                                   "\n`s!nowplaying`: điều khiển bài hát đang phát"
                                                                   "\n`s!queue`: xem danh sách nhạc chờ"
                                                                   "\n`s!skip`: cho qua nhạc đang phát"
                                                                   "\n`s!stop`: dừng nhạc đang phát và xóa tất cả bài nhạc chờ"
                                                                   "\n`s!volume`: thay đổi âm lượng nhạc đang phát"
                                                                   "\n`s!pause`: tạm dừng nhạc đang phát"
                                                                   "\n`s!remuse`: phát tiếp tục nhạc đang dừng hoặc chưa dừng"
                                                                   "\n`s!lyrics`: xem lời nhạc bài hát bạn muốn xem", inline=False)
    embed.set_footer(text=f"{người_làm_bot}")
    embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.send(embed=embed)


##########################
client.run(TOKEN)