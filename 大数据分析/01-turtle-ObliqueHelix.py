# 作者：shu qi
# 开发时间：2023/2/28 8:58

#斜螺旋线

import turtle

turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2*x)
    turtle.left(91)
turtle.exitonclick()