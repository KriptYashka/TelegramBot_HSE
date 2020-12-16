import threading
import datetime
import asyncio
import time

import discord
from discord.ext import commands
import Classes.DB_class as DataTool
import bot_requests as br

TOKEN = "Nzg4NzM1MzI4NTQxNjA1ODk4."+"X9n1BA._Q6m7lybjSyQhrT_neMv7G71qZI"  # Чтобы не переделывать токен
bot = commands.Bot(command_prefix='Бот ')

select = {
    "сотрудник": [6, br.add_worker, br.select_worker],
    "должность": [3, br.add_post],
    "местоработы": [3, br.add_workplace]
}

@bot.event
async def on_ready():
    print("{0.user} пришел на сервера".format(bot))

@bot.command(pass_context=True)
async def добавь(ctx, *args):
    cmd = args[0]
    if cmd in select.keys() is None:
        await ctx.send("Неизвестная команда")
        return
    if select[cmd][0] != len(args) - 1:
        await ctx.send("Неверное количество переменных.\nТребуется {} полей.".format(select[cmd][0]))
        return
    func = select[cmd][1]
    error = func(args[1:])
    text = "Команда выполнена"
    if error is not None:
        text = error
    await ctx.send(text)

@bot.command(pass_context=True)
async def покажи(ctx, *args):
    cmd = args[0]
    if cmd in select.keys() is None:
        await ctx.send("Неизвестная команда")
        return
    func = select[cmd][2]
    text = func(args[1])
    await ctx.send(text)

def main():
    db = DataTool.DataBase()
    bot.run(TOKEN)


if __name__ == "__main__":
    main()