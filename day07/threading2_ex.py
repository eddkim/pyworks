import datetime
import threading

def call():
    print("타이머 종료 !")
    print(datetime.datetime.now())


print(datetime.datetime.now())
timer=threading.Timer(10,call)
timer.start()

repeat()