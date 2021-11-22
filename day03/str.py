#문자열 함수 - 특별한 1차원 함수

s = 'banana, grape, apple'
x = s.split(',')
print(x)

s2 = 'a:b:c:d'
s2= s2.split(':')
print(s2)
print(s2[-1])
print(s2[1:])

#n1 = int(input('수 1 입력 : '))
#n2 = int(input('수 2 입력 : '))
n1 , n2 = input('두 수 입력 : ').split()
add = int(n1) + int(n2)
print(add)