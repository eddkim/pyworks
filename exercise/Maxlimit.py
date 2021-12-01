from exercise.calculator import Calculator

class Max(Calculator):
    def add(self,val):
        self.value += val
        if self.value > 100 :
            self.value = 100

        return self.value


cal = Max()
cal.add(50);cal.add(60)
print(cal.value)