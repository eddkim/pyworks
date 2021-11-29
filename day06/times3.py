

def times(a):
    x= a * 3
    return x

print(times(3))

def time(x):
    count = 0
    for i in range(1,101):
        if i % 3 == 0:
            count +=1
            print(i, end=' ')
            print(count)
time(3)
