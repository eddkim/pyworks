import random
import math

"""for x in range(10):
    dice = random.randint(1,6)
    print(dice)"""

for x in range(10):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1+dice2
    print(total)
    if dice1 == dice2 :
        print("Double !")
        