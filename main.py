import os
import interactions as it
from interactions import Client, Button, ButtonStyle, SelectMenu, SelectOption, ActionRow, Modal, TextInput,TextStyleType
from interactions import CommandContext as CC
from interactions import ComponentContext as CPC
import datetime

import time
import math
import config
from config import TOKEN



presence = it.PresenceActivity(name="Over CoA Community", type=it.PresenceActivityType.WATCHING)
bot = Client(token=TOKEN,presence=it.ClientPresence(activities=[presence]),disable_sync=False)


@bot.event
async def on_ready():
    bot_name = bot.me.name
    print(f"Logged in as {bot_name}!")


bot.load("cogs.guilds")

bot.start()