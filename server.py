from multiprocessing import Process
from pro import Pro
from datetime import datetime
import sys

import config as cfg
devices=cfg.devices

import coloredlogs, logging
now=datetime.now().strftime("tcp4cat.log")
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

p=[]
obj=[]

for i in range(len(devices)):
    obj.append(Pro(logger, devices[i][0], devices[i][1], devices[i][2], devices[i][3], devices[i][4]))

for i in range(len(obj)):
    try:
        obj[i].start()
    except Exception as e:
        logger.critical(e)
        logger.info("ending script, systemd will restart it in a few seconds.")
        exit(1)
    p.append(Process(target=obj[i].loop))

for i in range(len(p)):
    p[i].start()
for i in range(len(p)):
    p[i].join()
sys.exit(1)