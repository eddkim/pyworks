class Dog :
    #tricks = []

    def __init__(self,name):
        self.name = name
        self.tricks = []

    def add_trick(self,trick):
        self.tricks.append(trick)

dog1 = Dog("Elsa")
dog2 = Dog("Buddy")

dog1.add_trick("play dead")
dog2.add_trick("roll over")

print(dog1.tricks)
print(dog2.tricks)