# Configs imports from here

import os


if os.path.exists("config.py"):
    from config import Development as Config
else:
    from .cyborg_config import Config



