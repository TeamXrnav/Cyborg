import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from cyborgbot.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i> Cyborg Is Running Perfect! </b></i>
<i><b>↼ Owner ⇀</i></b> : 『 <a href='tg://user?id={}'>{}</a> 』
╭──────────────
┣─ <b>» Telethon ~</b> <i>{}</i>
┣─ <b>» Version ~</b> <i>{}</i>
┣─ <b>» Sudo ~</b> <i>{}</i>
┣─ <b>» Uptime ~</b> <i>{}</i>
┣─ <b>» Ping ~</b> <i>{}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/CyborgUpdates'>[ Updates ]</a> «««</i></b>
"""
#-------------------------------------------------------------------------------

@cyborg_cmd(pattern="alive$")
async def up(event):
    cid = await client_id(event)
    ForGo10God, CYBORG_USER, cyborg_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    cyborg = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    if a is not None:
        b = a.split(" ")
        c = []
        if len(b) >= 1:
            for d in b:
                c.append(d)
        PIC = random.choice(c)
    else:
        PIC = "https://telegra.ph/file/50cc2ee99fbb455fd074a.jpg"
    cyborg_pic = PIC
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, CYBORG_USER, tel_ver, cyborg_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=cyborg_pic, caption=omk, parse_mode="HTML")
    await cyborg.delete()


msg = """{}\n
<b><i>🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅</b></i>
<b>Telethon ≈</b>  <i>{}</i>
<b>Version ≈</b>  <i>{}</i>
<b>Uptime ≈</b>  <i>{}</i>
<b>Abuse ≈</b>  <i>{}</i>
<b>Sudo ≈</b>  <i>{}</i>
"""
botname = Config.BOT_USERNAME

@cyborg_cmd(pattern="aliveu$")
async def cyborg_a(event):
    cid = await client_id(event)
    ForGo10God, CYBORG_USER, cyborg_mention = cid[0], cid[1], cid[2]
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» Cyborg Is Running!  ««</b>"
    try:
        cyborg = await event.client.inline_query(botname, "alive")
        await cyborg[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, cyborg_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "aliveu", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
