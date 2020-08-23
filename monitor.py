import redis 
import datetime as dt
import time

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
i = 0
with r.monitor() as m:
        for command in m.listen():
            #print(command)
            i += 1
            print(f"{dt.datetime.fromtimestamp(command['time'])} {command['client_address']} {command['command']} ")
            if i > 10:
                break
time.sleep(30)
