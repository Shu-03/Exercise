# 作者：shu qi
# 开发时间：2023/2/28 9:33

#爱心绘制❤
import turtle
turtle.setup(1000,800)
turtle.pensize(10)
turtle.pencolor("red")
#turtle.fillcolor("pink")
turtle.begin_fill()

turtle.left(50)
turtle.circle(-100,180)
turtle.right(10)
turtle.forward(200)
turtle.right(80)
turtle.forward(200)
turtle.right(10)
turtle.circle(-100,180)

turtle.end_fill()
turtle.exitonclick()