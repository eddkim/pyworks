#온도 변환기 : 화씨 온도(F) = 섭씨 온도(C) x1.8 +32

from day09.class_lib.scaleconverter import ScaleConverter

class Converter(ScaleConverter):
    def __init__(self,units_from,units_to,factor,offset):
        super().__init__(units_from,units_to,factor)    # C, F, 1.8, 32
        self.offset = offset

    def convert(self,value):   # 부모 메서드 재정의 (overriding)
        return self.factor*value+self.offset # (단위값 x 수) + 단위2 값

Cv = Converter('C','F',1.8,32)
print("converting 21'C")
#print(Cv.convert(21),Cv.units_to)
print("%.2f"% Cv.convert(21),Cv.units_to)