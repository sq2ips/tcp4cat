from multiprocessing import Process
from pro import Pro

import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

p=[]
obj=[]

obj.append(Pro(logger, 8888, '', '/dev/pts/1', 115200, "cat"))
obj.append(Pro(logger, 8889, '', '/dev/pts/5', 115200, "rot"))

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

#print("x")
#pro.append(Process(target=r.start))
#print("y")
#pro[0].start()
#print("z")
#pro[0].join()
#print("i")