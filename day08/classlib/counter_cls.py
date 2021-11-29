class Counter :
    x = 0 #클래스 변수(self)를 사용하지 않음

    def __init__(self):
        Counter.x += 1 #클래스 변수 이름은 클래스 이름으로 직접

    def getcount(self):
        return Counter.x #self. 이게 아니라 클래스이름.x <- 전역변수 같은거

c1 = Counter()
print(c1.getcount())

c2 = Counter()
print(c2.getcount())