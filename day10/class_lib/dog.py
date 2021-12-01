class Dog :
    kind = "진돗개" #클래스 변수

    def __init__(self,name):
        self.name = name #인스턴스 변수

dog1 = Dog("백구")
dog2 = Dog("흰둥이")
print(dog1.name)  #유니크 이름
print(dog1.kind)  #shared 종류
print(dog2.name)
