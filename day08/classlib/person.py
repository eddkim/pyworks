#Person 클래스
#접근 제한 방법 - 변수 이름 앞에 _(언더바)
#접근 방법 - get +변수이름(), set + 변수이름으로 만들어 속성을 public으로 만듬

class Person :
    def __init__(self):
        self._name = "" #멤버 초기화, _ 접근제한
        self._age = 0

    def setname(self, name): #이름을 입력하는 함수
        self._name = name

    def getname(self): #이름을 가져오는 함수
        return self._name

    def setage(self,age):
        self._age=age

    def getage(self):
        return self._age
            
p1 = Person()
p1.setname("김하늘")
print(p1.getname())
p1.setage(25)
print(p1.getage())