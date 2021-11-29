import math
import random
#반올림


print(round(2.54))

#올림
print(math.ceil(2.11))

#버림
print(math.floor(5.12))

#제곱근 (루트)
print(math.sqrt(25))

#난수
print(random.random())

#주사위
print(math.floor(random.random()*6))

#원주율
r = 4 #반지름
area = math.pi*r**2
print("원의 넓이 :%.2f"%area)