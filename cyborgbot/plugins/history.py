from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest

from . import *


@cyborg_cmd(pattern="history(?:\s|$)([\s\S]*)")
async def _(cyborgevent):
    if not cyborgevent.reply_to_msg_id:
       await eod(cyborgevent, "`Please reply to a user to get his history`")
       return
    reply_message = await cyborgevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eod(cyborgevent, "Need actual users. Not Bots")
       return
    cyborg = await eor(cyborgevent, "Checking...")
    async with cyborgevent.client.conversation(chat) as conv:
          try:     
              first = await conv.send_message(f"/search_id {victim}")
              response1 = await conv.get_response()
              response2 = await conv.get_response() 
              response3 = await conv.get_response()
          except YouBlockedUserError: 
              await eod(cyborgevent, "Please unblock @Sangmatainfo_bot")
              return
          if response1.text.startswith("Name History"):
              await cyborg.edit(response1.text)
              await cyborgevent.client.delete_messages(conv.chat_id, [first.id, response1.id, response2.id, response3.id])
          elif response2.text.startswith("Name History"):
              await cyborg.edit(response2.text)
              await cyborgevent.client.delete_messages(conv.chat_id, [first.id, response1.id, response2.id, response3.id])
          elif response3.text.startswith("Name History"):
              await cyborg.edit(response3.text)
              await cyborgevent.client.delete_messages(conv.chat_id, [first.id, response1.id, response2.id, response3.id])
          else: 
              await cyborg.edit("No Records Found !")


@cyborg_cmd(pattern="unh(?:\s|$)([\s\S]*)")
async def _(cyborgevent):
    if not cyborgevent.reply_to_msg_id:
       await eod(cyborgevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await cyborgevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eod(cyborgevent, "Need actual users. Not Bots")
       return
    cyborg = await eor(cyborgevent, "Checking...")
    async with cyborgevent.client.conversation(chat) as conv:
          try:     
              first = await conv.send_message(f"/search_id {victim}")
              response1 = await conv.get_response() 
              response2 = await conv.get_response()
              response3 = await conv.get_response()
          except YouBlockedUserError: 
              await eod(cyborgevent, "Please unblock @Sangmatainfo_bot")
              return
          if response1.text.startswith("Username History"):
              await cyborg.edit(response1.text)
              await cyborgevent.client.delete_messages(conv.chat_id, [first.id, response1.id, response2.id, response3.id])
          elif response2.text.startswith("Username History"):
              await cyborg.edit(response2.text)
              await cyborgevent.client.delete_messages(conv.chat_id, [first.id, response1.id, response2.id, response3.id])
          elif response3.text.startswith("Username History"):
              await cyborg.edit(response3.text)
              await cyborgevent.client.delete_messages(conv.chat_id, [first.id, response1.id, response2.id, response3.id])
          else: 
              await cyborg.edit("No Records Found !")


CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
  "unh", "<reply to user>", "Fetches the Username History of replied users."
).add_info(
  "Telegram Name History"
).add_warning(
  "✅ Harmless Module."
).add()
