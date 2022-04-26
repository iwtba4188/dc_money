import datetime
from discord.ext import commands
import discord

from .func import *


class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='現金', style=discord.ButtonStyle.green)
    async def confirm_cash(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("已新增資料！", ephemeral=True)
        self.value = "cash"
        self.stop()

    @discord.ui.button(label='Line Pay', style=discord.ButtonStyle.green)
    async def confirm_line_pay(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("已新增資料！", ephemeral=True)
        self.value = "Line Pay"
        self.stop()

    @discord.ui.button(label='取消', style=discord.ButtonStyle.danger)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("取消新增", ephemeral=True)
        self.value = "cancel"
        self.stop()


class Data():
    def __init__(self, id, name, price, creat_time=today_YYMMDD(), last_modifying_time=today_YYMMDD(), bought_time=today_YYMMDD(), place="default", pay_type="cash", remark="default"):
        self._id = id
        self._creat_time = creat_time
        self._last_modifying_time = last_modifying_time
        self._bought_time = bought_time
        self._name = name
        self._place = place
        self._price = price
        self._pay_type = pay_type
        self._remark = remark
        pass

    def make_dic(self):
        res = {"id": self._id,
               "creat_time": self._creat_time,
               "last_modifying_time": self._last_modifying_time,
               "bought_time": self._bought_time,
               "name": self._name,
               "place": self._place,
               "price": self._price,
               "pay_type": self._pay_type,
               "remark": self._remark, }

        return res

    def generate_embed_message(self, check=False):
        if check:
            embed = discord.Embed(title="確認新增資料", description="請確認以下資料內容是否正確。", color=0x009dff)
        else:
            embed = discord.Embed(color=0x009dff)

        embed.add_field(name="購買時間", value=self._bought_time, inline=True)
        embed.add_field(name="名稱", value=self._name, inline=False)
        embed.add_field(name="價格", value=self._price, inline=True)
        embed.add_field(name="地點", value=self._place, inline=True)
        embed.add_field(name="備註", value=self._remark, inline=True)

        return embed
