import telethon.utils

from telethon.tl.functions.users import GetFullUserRequest

from .session import Cyborg, H2, H3, H4, H5
from cyborgbot.sql.gvar_sql import gvarstat


async def clients_list(Config, Cyborg, H2, H3, H4, H5):
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await Cyborg.get_me()
    user_ids.append(main_id.id)

    try:
        if H2 is not None:
            id2 = await H2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if H3 is not None:
            id3 = await H3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if H4 is not None:
            id4 = await H4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if H5 is not None:
            id5 = await H5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        Arnav_xD = uid.user.id
        CYBORG_USER = uid.user.first_name
        cyborg_mention = f"[{CYBORG_USER}](tg://user?id={Arnav_xD})"
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        Arnav_xD = uid
        CYBORG_USER = client.first_name
        cyborg_mention = f"[{CYBORG_USER}](tg://user?id={Arnav_xD})"
    return Arnav_xD, CYBORG_USER, cyborg_mention
