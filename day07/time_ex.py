import math
import time

print(time.time()) #1970.1.1 자정 이후 초로 환산
day = round(time.time()/(24*60*60)) #초를 일로 환산
year =round(time.time()/(24*60*60*365)) #초를 년으로 환산
print(day)
print(year)

#time.sleep(x) x초만큼 시간 간격을 둠
#for문 수행시간 측정
start = time.time()

for i in range(10):
    print(i)
    time.sleep(1) #파이썬 1-1초, 다른언어 1000 - 1초

end = time.time()
et = math.floor(end - start)
print("for문 수행 시간 : {}초".format(et))