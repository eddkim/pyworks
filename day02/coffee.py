

i = 5
coffee = 400
while i>0:
    money = int(input("돈을 넣어주세요 : "))
    
    if money == coffee :
        print("맛있게 드세요.")
        i=i-1
        print("남은 커피의 갯수는 ",i,"잔 입니다.")
    elif money > coffee :
        print("맛있게 드세요.\n 거스름돈은",money-coffee, "원 입니다.")
        i=i-1
        print("남은 커피의 갯수는 ",i,"잔 입니다.")
    else :
        print("금액이 부족합니다.")

    """if i ==0:
        print("장사 끝")
        break"""
        

    
