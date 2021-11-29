#리턴이 있는 함수 (반환값이 있는 함수)
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

a = add(10,11) #두 수를 입력
b = sub(10,20)
print(a)
print("두수의 합은 = {}".format(a))
print("두수의 차은 = {}".format(b))