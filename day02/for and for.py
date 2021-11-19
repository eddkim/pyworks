#중첩 for
#5행 5열

for i in range(0,5):
    for j in range(0,5):
        print("*",end=' ')
    print("\n"*2)

#직각
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=' ')
    print("\n"*2)

#역직각
for i in range(0,5):
    for j in range(0,5-i):
        print("*",end=' ')
    print("\n")

#5행 5열 안에 1부터 순차적으로 증가

for i in range(0,5):
    for j in range(1,6):
        num=i*5+j
        print(num,end=' ')
    print("\n"*2)
