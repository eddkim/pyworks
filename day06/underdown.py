import random

com = random.randint(1,100)
min_v = 1
max_v = 100
for i in range(10):
 try:
    guess = int(input("맞혀보셈[%d회]%d~%d : "%(i+1,min_v,max_v)))
    if guess == com :
        print("정답 !")
        break
    elif guess > 100 or guess<1:
        print("입력 범위를 초과했습니다. 다시 입력하세요.")
    elif guess > com :
        print("넘 커요")
        print()

    else :
        print("넘 작아요")
        print()
 except :
    print("숫자가 아닙니다.")

print("정답 : %d" %com)
print("점수 : %d"%((10-i)*10))