import datetime

today = datetime.datetime.now()
print(today.year)

age = int(input("나이 : "))

result =(100 - (age+1))+today.year
print("100세 되는 해 : ",result)