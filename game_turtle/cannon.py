#거북이 대포 게임
#각도를 맞춰 대포를 발사해 목표지점을 맞히는 게임
import turtle as t
import random as r


#좌표 이동
"""
t.shape('turtle')
t.up()
t.goto(0,200)
t.goto(0,-200)
t.goto(200,0)
"""
def turn_up() :
    t.left(2)

def turn_down():
    t.right(2)

def fire ():
    ang = t.heading() #거북이가 바로보는 각도 저장

    while t.ycor() > 0 : #거북이의 y좌표가 0보다 크면 (땅 위에 있는 동안)
        t.forward(15) # 15픽셀 이동
        t.right(5) #오른쪽으로 5도 돌림

        #while 반복문을 빠져 나오면 땅에 닿은 상태임
    d = t.distance(target,0) #거북이와 목표지점과의 거리 저장
    t.sety(r.randint(10,100))
    if d < 25 :
        t.write(" Good ! ", False, "center", ("",15))
    else :
        t.color('red')
        t.write("Bad", False,"center",("",15))
        t.color('black')
        t.goto(-200,10)
        t.setheading(ang)






#땅그리기

t.goto(-300,0)
t.goto(300,0)



#목표지점 그리기
target = r.randint(50,150)
t.color('green')
t.pensize(2)
t.up()
t.goto(target-25, 2) #x좌표, y좌표 :2
t.down() #선 내리기
t.goto(target+25, 2) #x좌표, y좌표 :2

#거북이의 처음 위치 선정
t.color('black')
t.up()
t.goto(-200,10)
t.setheading(20)

#동작하는 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
"""t.onkeypress(fire, "space")"""
t.listen()

t.mainloop()
