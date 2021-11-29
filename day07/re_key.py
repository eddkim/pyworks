#키보드로 조종하기

import turtle as t

t.bgcolor('black')
t.color('white')
def turn_right():
    t.setheading(0) #거북이 머리 0도
    t.forward(10)

def turn_left():
    t.setheading(180) #거북이 머리 0도
    t.forward(10)

def turn_up():
    t.setheading(90) #거북이 머리 0도
    t.forward(10)

def turn_down():
    t.setheading(270) #거북이 머리 0도
    t.forward(10)



t.shape('turtle')
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()








t.mainloop()