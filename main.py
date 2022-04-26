import json
import datetime

import discord
from discord.ui import Button, View
from discord.ext import commands

from tinydb import TinyDB, Query

from L_utils import *

SAVE_LOG_TO_FILE = True

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned_or("$"), intents=intents)


@bot.command(name="add")
async def add_record(ctx, *arg):
    """
    $add <str:name> <int:price>
    $add <str:name> <str:place> <int:price>
    $add <YYMMDD:bought_time> <str:name> <int:price>
    $add <YYMMDD:bought_time> <str:name> <str:place> <int:price>
    """

    """ parser """
    if (len(arg) == 2):
        data = Data(id=get_last_id(), name=str(arg[0]), price=int(arg[1]))
    # elif(len(arg) == 3):
    #     # if (len(arg[1]) == ):
    #     pass
    elif(len(arg) == 4):
        data = Data(
            id=get_last_id(),
            bought_time=str(arg[0]),
            name=str(arg[1]),
            place=str(arg[2]),
            price=int(arg[3]))

    view = Confirm()
    msg = await ctx.send(embed=data.generate_embed_message(check=True), view=view)
    await view.wait()

    if view.value == "cancel":
        await log("cancel adding")
        await msg.delete()
        return

    data._pay_type = view.value

    await log(f"add {data.make_dic()} successfully")
    await msg.edit(embed=data.generate_embed_message(), view=None)
    save_data(data)

    return


@bot.command(name="edit")
async def edit_data(ctx, *arg):
    """
    $edit <int:id> <YYMMDD:time>
    $edit <int:id> <YYMMDD:time> <str:name>
    $edit <int:id> <YYMMDD:time> <str:name> <int:price>
    $edit <int:id> <str:name>
    $edit <int:id> <str:name> <int:price>
    $edit <int:id> <int:price>
    """

    return


@bot.command(name="delete")
async def delete_data(ctx, *arg):
    """
    """

    return


@bot.command(name="view")
async def view_data(ctx, start_time="000000", end_time="999999"):
    """
    $view
    $view <int:start>
    $view <int:start> <int:end>
    """

    data = TinyDB("user_data.json")
    search_time = Query()
    print(type(search_time.bought_time))
    search_result = data.search(start_time <= search_time.bought_time <= end_time)

    print(search_result)
    for i in search_result:
        await ctx.send(i)

    return


@bot.command(name="analyze")
async def analyze_data(ctx, *arg):
    """
    """

    return


@bot.command(name="set")
async def setting(ctx, *arg):
    """
    """

    return


@bot.command(name="export")
async def export_data(ctx, *arg):
    """
    """

    return


async def log(message):
    """
    print out log and send log to log_channel.
    """

    now_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    log_message = f"[Log: {now_time}] {message}"

    print(log_message)

    if SAVE_LOG_TO_FILE:
        with open("log_file.txt", "a") as log_file:
            log_file.write(log_message+"\n")

    log_channel = bot.get_channel(951778979768070194)
    await log_channel.send(log_message)

    return


@bot.command(name="end")
async def end_bot(ctx):
    """
    end bot.
    """

    await log("end bot succesfully")

    return


@bot.event
async def on_ready():
    """
    when ready print log data.
    """

    general_channel = bot.get_channel(951781907690037278)

    await log("We have logged in as {0.user}".format(bot))
    await log("set the channel successfully")
    await general_channel.send(f"再次啟動ㄌ ({now_time_stamp()})")

    return

if __name__ == '__main__':
    # log("start running")
    with open("config.json") as file:
        data = json.load(file)
        token = data["token"]

    bot.run(token)
