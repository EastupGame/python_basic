import datetime
from time import sleep
while True:
    d = datetime.datetime.now()
    print(50 - d.minute)
    sleep(1)

