import os 
import subprocess
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger("Helper")
os.system("git clone https://github.com/TeamXrnav/Cyborg cyborgbot")
os.chdir("cyborgbot")
process = subprocess.Popen(
        ["python3", "-m", "cyborgbot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    LOGS.warning(er.decode())
print("::::::::::::::")
if out:
    LOGS.info(out.decode())
