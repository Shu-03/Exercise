# 作者：shu qi
# 开发时间：2023/2/28 8:56

#绘制彩色斜螺旋线

import turtle

turtle.speed("fastest")
turtle.pensize(2)
colors=["red","yellow","purple","blue"]
for x in range(100):
    turtle.pencolor(colors[x%4])
    turtle.forward(2*x)
    turtle.left(91)
turtle.exitonclick()

