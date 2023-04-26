# 作者：shu qi
# 开发时间：2023/4/23 16:10

import turtle

def main():
    turtle.setup(1024,768,0,0)
    turtle.pencolor("red")
    turtle.width(5)
    turtle.speed(5)
    result=[]
    file = open('data.txt','r')
    for line in file:
        result.append(list(map(float,line.split(','))))
    print(result)
    for i in range(len(result)):
        turtle.pencolor(result[i][3],result[i][4],result[i][5])
        turtle.forward(result[i][0])
        if result[i][1]:
            turtle.rt(result[i][2])
        else:
            turtle.lt(result[i][2])
    turtle.goto(0,0)

if __name__ == '__main__':
    main()
turtle.mainloop()