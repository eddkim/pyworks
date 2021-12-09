import re

str = "123?45yy7890"
m = re.findall("[0-9]{1,3}",str)  #리스트로 반환
print(m)