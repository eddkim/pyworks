from day09.class_lib.airplane import Airplane
from day09.class_lib.SuperSonicAirPlane import SuperSonicAirPlane

sa = SuperSonicAirPlane()
sa.take_off()
sa.fly()
sa.fly_mode=SuperSonicAirPlane.SUPERSONIC
sa.fly()
sa.fly_mode = SuperSonicAirPlane.NORMAL
sa.fly()
sa.land()