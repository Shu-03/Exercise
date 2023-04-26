# 作者：shu qi
# 开发时间：2023/2/28 9:13

#奥运五环图

import turtle
turtle.pensize(10)

turtle.color("blue")
turtle.penup()
turtle.goto(-110,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("black")
turtle.penup()
turtle.goto(0,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("red")
turtle.penup()
turtle.goto(110,-25)
turtle.pendown()
turtle.circle(45)

turtle.color("yellow")
turtle.penup()
turtle.goto(-55,-75)
turtle.pendown()
turtle.circle(45)

turtle.color("green")
turtle.penup()
turtle.goto(55,-75)
turtle.pendown()
turtle.circle(45)

turtle.exitonclick()