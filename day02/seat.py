#자리배치 프로그램
#고객 수를 열로 나눠 행을 구해서 for문으로 배치

customer = int(input("머릿 수 : "))

col = int(input("좌석 열 : "))

if customer % col == 0:
    row = int(customer/col)
else :
    row = customer //col + 1

for i in range(0,row):
    for j in range(1, col+1):
        seat = i*col+j
        print(seat, end=' ')
    print()

