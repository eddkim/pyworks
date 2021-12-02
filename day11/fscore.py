#파일

with open('score.txt','a') as f:
    try:
        name = input("이름 입력 : ")
        kor = int(input("국어 점수 : "))
        math = int(input("수학 점수 : "))
        sum_v = kor + math
        avg = sum_v/2

        f.write(name+ ' ')
        f.write(str(kor)+ ' ')
        f.write(str(math)+ ' ')
        f.write(str(sum_v)+' ')
        f.write(str(avg)+'\n')

    except ValueError:
        print("유효한 숫자가 아닙니다.")
