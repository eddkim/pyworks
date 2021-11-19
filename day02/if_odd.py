num = int(input("숫자 : "))

if num >10:
    if num &2 == 0:
        print("10보다 큰 짝수입니다.")
    else :
        print("10보다 큰 홀수입니다.")

else :
    if num &2 == 0:
        print("10 이하의  짝수입니다.")
    else :
        print("10 이하의  홀수입니다.")

num2 = int(input("숫자를 입력 : "))
if num2 > 10 :
    if num2 & 2 == 0 :
        print("10보다 큰 짝수입니다")
    elif num2 & 2 !=0 :
        print("10보다 큰 홀수입니다")
else :
    if num2 & 2 ==0:
        print("10 이하의 짝수 입니다.")
    elif num2 & 2 !=0:
        print("10 이하의 홀수입니다")
    
