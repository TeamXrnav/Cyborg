import asyncio
import io
import os

from datetime import datetime
from pathlib import Path

from telethon import events, functions, types
from telethon.tl.types import InputMessagesFilterDocument

from . import *


@cyborg_cmd(pattern="cmds$")
async def kk(event):
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    cids = await client_id(event)
    ForGo10God, CYBORG_USER, cyborg_mention = cids[0], cids[1], cids[2]
    cmd = "ls cyborgbot/plugins"
    thumb = cyborg_logo
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"List of Plugins in bot :- \n\n{o}\n\n<><><><><><><><><><><><><><><><><><><><><><><><>\nHELP:- If you want to know the commands for a plugin, do :- \n.plinfo <plugin name> without the < > brackets. \nJoin {cyborg_grp} for help."
    if len(OUTPUT) > 69:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "cmd_list.text"
            cyborg_file = await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                thumb=thumb,
                reply_to=reply_to_id,
            )
            await edit_or_reply(cyborg_file, f"Output Too Large. This is the file for the list of plugins in bot.\n\n**BY :-** {CYBORG_USER}")
            await event.delete()


@cyborg_cmd(pattern="send ([\s\S]*)")
async def send(event):
    cids = await client_id(event)
    ForGo10God, CYBORG_USER, cyborg_mention = cids[0], cids[1], cids[2]
    message_id = event.message.id
    thumb = cyborg_logo
    input_str = event.pattern_match.group(1)
    omk = f"**• Plugin name ≈** `{input_str}`\n**• Uploaded by ≈** {cyborg_mention}\n\n⚡ **[🤖 Cyborg 🤖]({chnl_link})** ⚡"
    the_plugin_file = "./cyborgbot/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await eod(event, "File not found..... Kek")


@cyborg_cmd(pattern="install(?:\s|$)([\s\S]*)")
async def install(event):
    cids = await client_id(event)
    ForGo10God, CYBORG_USER, cyborg_mention = cids[0], cids[1], cids[2]
    b = 1
    owo = event.text[9:]
    cyborg = await eor(event, "__Installing.__")
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "./cyborgbot/plugins/"  # pylint:disable=E0602
            )
            if owo != "-f":
                op = open(downloaded_file_name, "r")
                rd = op.read()
                op.close()
                try:
                    for harm in HARMFUL:
                        if harm in rd:
                            os.remove(downloaded_file_name)
                            return await cyborg.edit(f"**⚠️ WARNING !!** \n\n__Replied plugin file contains some harmful codes. Please consider checking the file. If you still want to install then use__ `{hl}install -f`. \n\n**Codes Detected :** \n• {harm}")
                except BaseException:
                    pass
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**Commands found in** `{}`\n".format((os.path.basename(downloaded_file_name)))
                    for i in CMD_LIST[shortname]:
                        string += "  •  `" + i 
                        string += "`\n"
                        if b == 1:
                            a = "__Installing..__"
                            b = 2
                        else:
                            a = "__Installing...__"
                            b = 1
                        await cyborg.edit(a)
                    return await cyborg.edit(f"✅ **Installed module** :- `{shortname}` \n✨ BY :- {cyborg_mention}\n\n{string}\n\n        ⚡ **[🤖 Cyborg 🤖]({chnl_link})** ⚡", link_preview=False)
                return await cyborg.edit(f"Installed module `{os.path.basename(downloaded_file_name)}`")
            else:
                os.remove(downloaded_file_name)
                return await eod(cyborg, f"**Failed to Install** \n`Error`\nModule already installed or unknown format")
        except Exception as e: 
            await eod(cyborg, f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)


@cyborg_cmd(pattern="uninstall ([\s\S]*)")
async def uninstall(event):
    shortname = event.text[11:]
    if ".py" in shortname:
        shortname = shortname.replace(".py", "")
    cyborg = await eor(event, f"__Trying to uninstall plugin__ `{shortname}` ...")
    dir_path =f"./cyborgbot/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await eod(cyborg, f"**Uninstalled plugin** `{shortname}` **successfully.**")
    except OSError as e:
        await eod(cyborg, f"**Error !!** \n\n`{dir_path}` : __{e.strerror}__")


@cyborg_cmd(pattern="unload ([\s\S]*)")
async def unload(event):
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded `{shortname}`")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@cyborg_cmd(pattern="load ([\s\S]*)")
async def load(event):
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )

CmdHelp("core").add_command(
  "install", "<reply to a .py file>", "Installs the replied python file if suitable to Cyborg's codes.`\n**🚩 Flags :** `-f"
).add_command(
  "uninstall", "<plugin name>", "Uninstalls the given plugin from Cyborg. To get that again do .restart", "uninstall alive"
).add_command(
  "load", "<plugin name>", "Loades the unloaded plugin to your userbot", "load alive"
).add_command(
  "unload", "<plugin name>", "Unloads the plugin from your userbot", "unload alive"
).add_command(
  "send", "<file name>", "Sends the given file from your userbot server, if any.", "send alive"
).add_command(
  "cmds", None, "Gives out the list of modules in CyborgBot."
).add_warning(
  "❌ Install External Plugin On Your Own Risk. We won't help if anything goes wrong after installing a plugin."
).add()
