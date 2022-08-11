import discord
import asyncio
from embeds import *
from tut_nicho_net import *
from discord.ext import commands
client = discord.Client()

bot = commands.Bot(command_prefix='d!')

cats = 'http://i.imgur.com/bTPC8q9.jpg https://i.redd.it/ivbnkl62jdly.jpg https://i.redd.it/lyvjttzv41jy.jpg https://i.redd.it/7y066tkjcgxy.jpg https://i.imgur.com/gallery/IHyI3wa.jpg'
dogs = 'https://i.imgur.com/xkbxhoR.jpg https://i.imgur.com/gkXx3fi.jpg https://i.imgur.com/wEeMv6c.jpg https://i.reddituploads.com/94cb5666b8794aafa0a08e1ca64c78c8?fit=max&h=1536&w=1536&s=af417498d45951ee7f83d8dd87c10bb0 https://i.reddituploads.com/1ca54ec233b947ceb53254a6c0ac81ba?fit=max&h=1536&w=1536&s=5304ef629e87596dee1af0d0f746e92b'
aww = 'https://i.imgur.com/4WNi9KB.jpg http://i.imgur.com/lL9L7F9.jpg http://i.imgur.com/RYhTpxF.gif https://i.imgur.com/B7zInR1.jpg https://i.redd.it/cxrfhlguc8yy.jpg'


@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.idle)
  print(f"Бот запущен ({bot.user.name})")





@bot.command()
async def dogbomb(ctx):
  await ctx.send(dogs) 

@bot.command()
@commands.has_permissions(manage_messages = True)
async def cm(ctx, amount = 50):
  if amount > 100:
    await ctx.reply(embed = clearError)
  else:
    await ctx.reply("Чистим чистим чистим...")
    await ctx.channel.purge(limit = amount + 2)
    await ctx.send(f":white_check_mark:**, {amount} сообщений удалены.**")
    print(f'{amount} сообщений удалены в канале {ctx.message.channel.name} на сервере {ctx.message.guild.name} ({ctx.message.guild.id})')

@bot.command()
@commands.has_permissions(kick_members = True)
async def warn(ctx, member : discord.Member,*, reason = 'Причина не указана'):
    if member == ctx.author:
      await ctx.reply(embed = warnError)
      return
    if member == bot.user.mention:
      await ctx.reply(embed = warnYaObidelsya)

    else:
      warn = discord.Embed(
        title = f'{member} получил варн.',
        description = f'Участник {member} получил варн. \n Причина: {reason} \n Варн дал {ctx.message.author.mention}. \n Больше так не делай!',
        colour = 0x3ee42d
      )
      warn.set_thumbnail(url = 'https://files.catbox.moe/n7v04d.png')
      await ctx.send(embed = warn)
      warnDM = discord.Embed(
        title = f'Ты получил варн на сервере {ctx.message.guild.name}.',
        description = f'Ты получил варн на сервере {ctx.message.guild.name}. \n Причина: {reason}. \n Варн дал {ctx.message.author.name}. \n Больше так не делай!',
        colour = 0xff0000
      )
      warnDM.set_thumbnail(url = 'https://files.catbox.moe/o3hosf.png')
      await member.send(embed = warnDM)
      print(f'{member} получил варн на сервере {ctx.message.guild.name} от {ctx.message.author.name} по причине {reason}')


@bot.command()
async def commands(ctx):
  await ctx.send(embed=help1)
  await ctx.send(embed=help2)
  await ctx.send("https://discord.gg/EmEKCXhtpJ")

@bot.command()
async def hedgehog(ctx):
  await ctx.send('https://i.imgur.com/YZmdx3A.jpg')

@bot.command()
async def awwbomb(ctx):
  await ctx.send(aww)


@bot.command()  
async def say(ctx, arg):  
    await ctx.reply(arg) 
    print(f'Я сказал {arg} в канале {ctx.message.channel.name} на сервере {ctx.message.guild.name} ({ctx.message.guild.id})') 


@bot.command()
async def catbomb(ctx):
  await ctx.send(cats)

@bot.command()
async def status(ctx):
  await ctx.send(embed = status_dima)


@bot.command(pass_context=True)  
async def spam(ctx, arg):  
    await ctx.send(arg)
    await ctx.send(arg)
    await ctx.send(arg)
    await ctx.send(arg)
    await ctx.send(arg)

class avatar():
    def ___init___(bot):
      self.bot = bot


    @bot.command()
    async def avatar(ctx, member : discord.Member = None):

          if member is None:
            await ctx.send(embed=noneMember)
            return

          else:
            avatar = discord.Embed(
            title = f'Аватарка {member}:',
            color = 0x3ee42d
            )  
            avatar.set_image(url=member.avatar_url)
            await ctx.send(embed=avatar)

def setup(bot):
  bot.add_cog(avatar(bot))

@bot.command()
async def servinfo(ctx):
  servinfo = discord.Embed(
  title='Информация о сервере', color = 0x00FFFF
  )
  bugfix = f"<@{ctx.message.guild.owner_id}>"
  boosts = f"{ctx.message.guild.premium_subscription_count}"
  boostLevel = "0"
  if boosts == "0":
    boosts = f"{ctx.message.guild.premium_subscription_count} <:sadcat:1001067205338869790>"
    boostLevel = "0 <:sadcat:1001067205338869790>"
  if boosts >= "2":
    boostLevel = "1 уровень"
  if boosts >= "7":
    boostLevel = "2 уровень"
  if boosts == "14":
    boostLevel = "3 уровень (максимальный)"
  servinfo.set_thumbnail(url=ctx.message.guild.icon_url)
  servinfo.add_field(name = 'Название сервера', value = ctx.message.guild.name, inline = True)
  servinfo.add_field(name = 'Участники', value = (ctx.message.guild.member_count))
  servinfo.add_field(name = 'Каналы', value = len(ctx.message.guild.channels))
  servinfo.add_field(name = 'Айди сервера', value = ctx.message.guild.id, inline = True)
  servinfo.add_field(name = 'Количество бустов', value = boosts, inline = True)
  servinfo.add_field(name = 'Уровень бустов', value = boostLevel, inline = True)
  servinfo.add_field(name = 'Сервер создан ', value = ctx.message.guild.created_at, inline = True)
  servinfo.add_field(name = 'Владелец сервера', value = bugfix, inline = True)
  await ctx.send(embed=servinfo)

bot.run(TOKEN)