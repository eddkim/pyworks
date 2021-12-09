import re

#compile -> byte 코드로 바꿈
p = re.compile("[a-z]+")
m = p.match("afternoon")
print(m)

m2 = p.match("2021 python")
print(m2)