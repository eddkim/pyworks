#다각형 그리기

import turtle as t
t.shape('turtle')
def poly(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def poly2(n,d):
    for x in range(n):
        t.forward(d)
        t.left(360/n)

poly(3)
poly(5)

t.forward(100)

poly2(3,100)
t.mainloop()
