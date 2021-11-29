name = input("이름을 입력하세요 : ")
height = float(input("키를 입력하세요 :"))
weight = float(input("몸무게를 입력하세요 :"))

BMI = round(weight/(height/100)**2,2)
print(name,"님의 BMI는",BMI,"입니다.")
if BMI < 20 :
    print("저체중입니다")
elif BMI >=20 and BMI <=25:
    print("정상입니다ㅋ")
elif BMI >=25.1 and BMI <=29 :
    print("과체중입니다.")
else : print("비만비만")
