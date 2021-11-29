[70,60,55,75,95,90,80,80,85,100]
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A :
    total += score
avg = total / len(A)

print(total)
print(avg)
#2
customer = int(input("머릿 수 : "))

col = int(input("좌석 열 : "))

if customer % col == 0:
    row = int(customer/col)
else :
    row = customer //col + 1

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
t = 0
for s in A :
    t+=s
avg = t/len(A)

print(t)
print(avg)


