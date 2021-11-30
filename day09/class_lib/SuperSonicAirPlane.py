
from day09.class_lib.airplane import Airplane

class SuperSonicAirPlane(Airplane) :

    NORMAL = 1 #클래스 상수 (대문자로 표기)
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL #멤버 - 비행모드

    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC :
            print("뱅기가 초음속으로 비행합니다.")
        else:
            super().fly()