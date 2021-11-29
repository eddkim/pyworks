#지역 변수, 전역 변수

def one_up():
    global x
    x += 1
    return x



x = 1
print(one_up())
print(one_up())