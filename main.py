from multiprocessing import Process
from pro import Pro

import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

obj=[]

obj.append(Pro(logger, 8888, '', '/dev/pts/5', 115200, "cat"))
#rot = Req(logger, 8888, '', '/dev/zero', 115200, "rotor")
for i in range(len(obj)):
    try:
        obj[0].start()
    except Exception as e:
        logger.critical(e)
        logger.info("ending script, systemd will restart it in a few seconds.")
        exit(1)



#print("x")
#pro.append(Process(target=r.start))
#print("y")
#pro[0].start()
#print("z")
#pro[0].join()
#print("i")