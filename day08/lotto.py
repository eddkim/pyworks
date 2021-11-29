import random

"""lotto = []

for i in range(0,6):
    num = random.randint(1,45)
    if num not in lotto :
        lotto.append(num)
print(lotto)"""

lotto = []
while len(lotto) < 6 :
    num = random.randint(1,45)
    if num not in lotto :
        lotto.append(num)

print(lotto)