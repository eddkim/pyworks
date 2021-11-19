age = int(input("나이를 입력해라 : "))

if age < 8 :
    print("미취학 아동입니다.");charge = 1000
    
elif age >=8 and age<14:
    print("초딩입니다");charge = 2000
    
elif age >=14 and age <20:
    print("중고딩");charge = 3000
    
else :
    print("일반인 입니다.");charge = 5000

print("입장료는 ",charge,"원 입니다.")
