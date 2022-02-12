import datetime
import time

from cyborgbot import *
from cyborgbot.clients import *
from cyborgbot.config import Config
from cyborgbot.helpers import *
from cyborgbot.utils import *
from cyborgbot.random_strings import *
from cyborgbot.version import __cyborg__
from cyborgbot.sql.gvar_sql import gvarstat
from telethon import version

cyborg_logo = "./cyborgbot/resources/pics/cyborgbot_logo.jpg"
cjb = "./cyborgbot/resources/pics/cjb.jpg"
restlo = "./cyborgbot/resources/pics/rest.jpeg"
shuru = "./cyborgbot/resources/pics/shuru.jpg"
shhh = "./cyborgbot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
cyborg_ver = __cyborg__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "CyborgUpdates"
my_group = Config.MY_GROUP or "CyborgSupportChat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/CyborgUpdates"
cyborg_channel = f"[Updates]({chnl_link})"
grp_link = "https://t.me/CyborgSupportChat"
cyborg_grp = f"[Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# cyborgbot
