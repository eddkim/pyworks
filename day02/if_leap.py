year = int(input("년도 입력 : "))

if year % 4 == 0 and year % 100 != 0 :
    print(str(year),"년은 윤년입니다.")
else :
    print(str(year),"년은 평년")
    
