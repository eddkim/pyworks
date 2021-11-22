#3의 배수

a = []
count = 0
sum = 0
for i in range(1,21):
    if i % 3 == 0 :
        count += 1
        a.append(i)
        print(i, end=' ')

print()
print(sum(a))
print()
print('3의 배수의 갯수 : ', len(a))

print ()
print('3의 배수의 갯수 : ', count)
