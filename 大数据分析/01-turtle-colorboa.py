# 作者：shu qi
# 开发时间：2023/2/28 9:08


#彩色蟒蛇
import turtle

turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.seth(-40)
colors = [ "purple","red","yellow", "pink","blue","green"]
for i in range(6):
    turtle.pencolor(colors[i % 6])
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.exitonclick()