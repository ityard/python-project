from turtle import *
from random import randrange, choice

# 气球
balloons = []
# 颜色
color_option = ["red", "blue", "green", "purple", "pink", "yellow", "orange"]
# 气球大小
size = 50
# 气球线
def line(x, y, a, b, line_width=1, color_name="black"):
    up()
    goto(x, y)
    down()
    color(color_name)
    width(line_width)
    goto(a, b)

def distance(x, y, a, b):
    # 判断鼠标点击位置和气球坐标的距离
    return ((a - x) ** 2 + (b - y) ** 2) ** 0.5
def tap(x, y):
    for i in range(len(balloons)):
        # 判断是否点击气球队列中的其中一个
        if distance(x, y, balloons[i][0], balloons[i][1]) < (size / 2):
            # 删除气球
            balloons.pop(i)
            return
def draw():
    # 清除画布
    clear()
    for i in range(1, (len(balloons) + 1)):
        line(balloons[-i][0], balloons[-i][1], balloons[-i][0], balloons[-i][1] - size * 1.5, 1)
        up()
        goto(balloons[-i][0], balloons[-i][1])
        # 画原点，参数为大小和颜色
        dot(size, balloons[-i][2])
        # 改变纵坐标，模仿气球上升
        balloons[-i][1] = balloons[-i][1] + 1
    # 修改画布
    update()
def gameLoop():
    # 1/20 的概率生成一个气球
    if randrange(0, 20) == 1:
        # 气球坐标，在边框位置减去气球大小
        x = randrange(-300 + size, 300 - size)
        # 随机在颜色队列选择一个颜色
        c = choice(color_option)
        # 添加气球队列
        balloons.append([x, -200 - size, c])
    draw()
    ontimer(gameLoop, 10)

# 画布大小为 600*600，初始坐标为(0,0)
setup(600, 600, 0, 0)
# 隐藏小乌龟
hideturtle()
# 隐藏绘制过程
tracer(False)
listen()
# 如果单机，调用tap方法
onscreenclick(tap)
gameLoop()
# 结束函数，画布停留
done()