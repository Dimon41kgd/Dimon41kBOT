import discord
from discord.ext import commands
client = discord.Client()

help1 = discord.Embed(
  title = 'Команды',
  description = '**Развлечения:** \n d!spam <что-нибудь> - бот проспамит это слово 5 раз. \n d!say <что-то> - бот повторит то, что вы напишите. \n d!catbomb - Атака котами (5 картинок с котами) \n d!dogbomb - Атака собачками (5 картинок с котами) \n d!hedgehog - картинка с ёжиком \n d!awwbomb - Атака милыми картинками (5 милых картинок) \n **Модерация:** \n d!cm [кол-во сообщений] - удалить сообщения в текущем канале (если не вводить число, будет удалено 50 сообщений. Команда доступна только людям с правом "Управлять сообщениями") \n d!warn <участник> [причина] дать участнику варн (командой могут пользоваться только люди с правом "Кикать участников")\n **Инструменты:** \n d!avatar <участник> - показать аватарку участника) \n d!servinfo - показать информацию о сервере',
  color=0x3ee42d
)

help2 = discord.Embed(
  title = 'Заходи на официальный сервер Dimon41kBOT',
  description = 'Если у тебя есть идея, которую можно добавить в бота, или ты нашел баг в работе бота, заходи на официальный сервер Dimon41kBOT и напиши об этом!' ,
  color=0xffa03d
)
help1.set_thumbnail(url = 'https://files.catbox.moe/4vllk6.jpg')

status_dima = discord.Embed(
  title = 'Статус бота',
  description = 'Шард #1: :white_check_mark: Онлайн \n Шард #2: :white_check_mark: Онлайн \n Шард #3 : :white_check_mark: Оффлайн',
  colour = 0x3ee42d
)

noneMember = discord.Embed(
  title = 'Ошибка: не указан участник',
  description = 'Укажите участника, который находится на этом сервере.',
  colour = 0xff0000
)
noneMember.set_thumbnail(url = 'https://files.catbox.moe/tjgjlk.png')

clearError = discord.Embed(
  title = 'Ошибка: слишком большое число',
  description = 'Вы ввели слишком большое число. За 1 раз можно удалить не более 100 сообщений, это сделано в целях безопаности.',
  colour = 0xff0000
)
clearError.set_thumbnail(url = 'https://files.catbox.moe/tjgjlk.png')

warnError = discord.Embed(
  title = 'Ошибка: вы не можете варнить самого себя.',
  description = 'Вы не можете дать варн самому себе, только кому-либо другому. Укажите другого участника',
  colour = 0xff0000
)
warnError.set_thumbnail(url = 'https://files.catbox.moe/tjgjlk.png')

warnYaObidelsya = discord.Embed(
  title = 'Я обиделся',
  description = 'После всего хорошего, это то, как ты меня награждаешь? Что за позор',
  color = 0xff0000
)
warnYaObidelsya.set_thumbnail(url = 'https://files.catbox.moe/o3hosf.png')