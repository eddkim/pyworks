seasons = ['봄','여름','가을','겨울']
print(seasons[2])

number = [10,20,30,40,50,60]

print(len(number))

for i in number:
    print(i)

for i in range(0,4):
    print(i)

num = [10,20,30,40]

for i in num :
    print(i, end=' ')
    print()

n = len(num)
for i in range(0,n):
    print(num[i], end=' ')
print()

#성적 만들기
#list score

score = [70,80,90,20,40]

len(score) # 갯수
sum = 0

for i in score :
    sum += i

print('합계 : ', sum)
print('평균 : ',sum/len(score))
print('최고점 : ', max(score))


a = [10,20,30,40]
print(sum(a))










