#여러 개의 원 그리기
import turtle as t

n = 100
t.speed(0) #1~10, 가장 빠른속도 - 0
t.color('green')
t.bgcolor('black')
for i in range(n):
    t.circle(100)
    t.left(360/n) #7.5

t.mainloop()
