from exercise.calculator import Calculator
class UpgradeCalculator(Calculator):
    def minus(self,val):
        self.value-=val
        return self.value

cal = UpgradeCalculator()
cal.add(10);cal.minus(3)
print(cal.value)
