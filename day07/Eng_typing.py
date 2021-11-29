import  random
import time

word = ['sky','earth','moon','flower','tree','strawberry','grape','garlic','onion','potato']
"""rand = random.choice(word)
print(rand)
print(word[-1])"""
n = 1 #문제 번호
input("[타자게임] 준비되면 엔터 ! ")
start = time.time()
while n < 11 :
    print('문제',n)
    question = random.choice(word) #문제 단어 출제
    print(question)
    answer = input("입력하세요 : ")
    if question == answer :
        print('통과')
        n+=1
    elif question != answer :
        print('다시 도전')
        n = 1

end = time.time()

print("게임 소요 시간 : %.2f"%(end-start))

