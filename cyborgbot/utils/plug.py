import asyncio
import datetime
import importlib
import inspect
import logging
import math
import os
import re
import sys
import time
import traceback
from pathlib import Path
from time import gmtime, strftime

from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from cyborgbot import *
from cyborgbot.clients import *
from cyborgbot.helpers import *
from cyborgbot.config import *
from cyborgbot.utils import *


# ENV
ENV = bool(os.environ.get("ENV", False))
if ENV:
    from cyborgbot.config import Config
else:
    if os.path.exists("Config.py"):
        from Config import Development as Config


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import cyborgbot.utils

        path = Path(f"cyborgbot/plugins/{shortname}.py")
        name = "cyborgbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("CyborgBot - Successfully imported " + shortname)
    else:
        import cyborgbot.utils

        path = Path(f"cyborgbot/plugins/{shortname}.py")
        name = "cyborgbot.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Cyborg
        mod.H1 = Cyborg
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Cyborg = Cyborg
        mod.CyborgBot = CyborgBot
        mod.tbot = CyborgBot
        mod.tgbot = bot.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        # support for uniborg
        sys.modules["uniborg.util"] = cyborgbot.utils
        mod.Config = Config
        mod.borg = bot
        mod.cyborgbot = bot
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_cyborg = delete_cyborg
        mod.eod = delete_cyborg
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.cyborg_cmd = cyborg_cmd
        mod.sudo_cmd = sudo_cmd
        # support for other userbots
        sys.modules["userbot.utils"] = cyborgbot.utils
        sys.modules["userbot"] = cyborgbot
        # support for paperplaneextended
        sys.modules["userbot.events"] = cyborgbot
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["cyborgbot.plugins." + shortname] = mod
        LOGS.info("🤖 Cyborg  🤖Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                bot.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"cyborgbot.plugins.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                ev, cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

