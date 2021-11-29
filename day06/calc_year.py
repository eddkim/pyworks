#나이가 100세 도ㅓㅣ는 해의 연도 계싼학;ㅣ

import datetime_ex

today = datetime.datetime.now()
print(today.year)

age = int(input("나이 : "))

result =(100 - (age+1))+today.year
print("100세 되는 해 : ",result)