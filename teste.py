import datetime
import time

t = datetime.datetime.now()
time.sleep(5)
print(datetime.datetime.now())
ss = datetime.datetime.strptime(t,'%H:%M:%S')
print(ss)
