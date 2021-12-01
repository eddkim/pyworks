class Animal :
    def cry(self):
        raise NotImplementedError

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
