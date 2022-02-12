import os

from . import *


@cyborg_cmd(pattern="mediainfo$")
async def mediainfo(event):
    CYBORG_MEDIA = None
    reply = await event.get_reply_message()
    logo = "https://telegra.ph/file/d09cdb53e72cd7215892e.jpg"
    if not reply:
        return await eod(event, "Reply to a media to fetch info...")
    if not reply.media:
        return await eod(event, "Reply to a media file to fetch info...")
    cyborg = await eor(event, "`Fetching media info...`")
    CYBORG_MEDIA = reply.file.mime_type
    if not CYBORG_MEDIA:
        return await cyborg.edit("Reply to a media file to fetch info...")
    elif CYBORG_MEDIA.startswith(("text")):
        return await cyborg.edit("Reply to a media file to fetch info ...")
    hel_ = await mediadata(reply)
    file_path = await reply.download_media(Config.TMP_DOWNLOAD_DIRECTORY)
    out, err, ret, pid = await runcmd(f"mediainfo '{file_path}'")
    if not out:
        out = "Unknown Format !!"
    paster = f"""
<h2>📃 MEDIA INFO 📃</h2>
<code>
{hel_}
</code>
<h2>🧐 MORE DETAILS 🧐</h2>
<code>
{out} 
</code>
<img src='{logo}'/>"""
    paste = await telegraph_paste(f"{CYBORG_MEDIA}", paster)
    await cyborg.edit(f"📌 Fetched  Media Info Successfully !! \n\n**Check Here :** [{CYBORG_MEDIA}]({paste})")
    os.remove(file_path)

CmdHelp("mediainfo").add_command(
  "mediainfo", "<reply to a media>", "Fetches the detailed information of replied media."
).add_info(
  "Everything About That Media."
).add_warning(
  "✅ Harmless Module."
).add()
