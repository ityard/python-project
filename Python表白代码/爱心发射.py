from turtle import *

Turtle().screen.delay(0)

def go_to(x, y):
    up()
    goto(x, y)
    down()
    
def ring(a,b,c,d):
    for i in range(a):
        forward(b)
        if d == 'right':
            right(c)
        else:
            left(c)

def heart(x, y, size):
    go_to(x, y)
    left(150)
    begin_fill()
    forward(51*size)
    ring(150,size,0.3,'right')
    ring(210,size,0.786,'right')
    left(120)
    ring(210,size,0.786,'right')
    ring(150,size,0.3,'right')
    forward(51*size)
    end_fill()

#头部
color('black')
go_to(-228, 72)
pensize(3)
left(150)
ring(350,1,0.8,'right')

#手臂
left(150)
forward(70)
left(90)
forward(10)
ring(200,0.1,0.9,'right')
forward(10)
left(90)
forward(20)
ring(200,0.1,0.9,'right')
forward(10)
left(90)
ring(200,0.2,0.9,'right')
left(100)
left
forward(80)

#身体
go_to(-228, 72)
left(40)
forward(40)
ring(120,0.2,0.9,'left')

go_to(-219,52)
right(95)
forward(80)
right(85)
ring(205,0.1,0.9,'left')
forward(40)
left(90)
forward(10)
ring(200,0.1,0.9,'right')
forward(10)
left(90)
forward(40)
ring(205,0.1,0.9,'left')
right(92)
forward(90)

#左眼
go_to(-217,155)
fillcolor('black')
begin_fill()
circle(5)
end_fill()

#右眼
go_to(-169,158)
fillcolor('black')
begin_fill()
circle(5)
end_fill()

#微笑
go_to(-210,132)
right(180)
ring(200,0.2,0.9,'left')

#腮红
color('#ffa0a0')
pensize(5)
left(170)

go_to(-235, 135)
forward(11)
go_to(-225, 135)
forward(11)
go_to(-155, 140)
forward(11)
go_to(-165, 140)
forward(11)

#比心
setheading(0)
heart(-35, 135, 0.10)
setheading(0)
heart(5, 150, 0.13)
setheading(0)
heart(52, 165, 0.15)


# 写字
go_to(-39, 69)
write("520",  align="left", font=("黑体", 30, "normal"))

hideturtle()
done()