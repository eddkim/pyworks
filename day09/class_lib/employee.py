
from day09.class_lib.person import Person

class Employee(Person) : #Person 클래스 상속 받음
    def __init__(self,name,age,employeeID):
        super().__init__(name,age) #부모 멤버 super 키워드로 명시
        self.employeeID = employeeID #자기 멤버 초기화

    def __str__(self):
        return super().__str__()+", 사번 : "+str(self.employeeID) #튜플형이라 " , " (콤마)가 안됨, 숫자 앞에 str 붙혀야함

    




e = Employee("김홍연", 28,101)
print(e)

#print("이름 : ",e.name)
#print("나이 : ",e.age)
#print("사번 : ",e.employeeID)