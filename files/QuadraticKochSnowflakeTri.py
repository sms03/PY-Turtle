import turtle

screen = turtle.Screen()
screen.title('Quadratic Koch Curve From Triangle - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('midnight blue')
turtle.color('white')

def koch(x1,y1,x2,y2):
    distance=((x2-x1)**2 + (y2-y1)**2)**0.5
    if distance<10:
        turtle.up()
        turtle.goto(x1,y1)
        turtle.down()
        turtle.goto(x2,y2)
        return
    turtle.up()
    turtle.goto(x1,y1)
    direction=turtle.towards(x2,y2)
    turtle.seth(direction)
    turtle.fd(distance/3)
    x3,y3 = turtle.xcor(), turtle.ycor()
    turtle.left(90)
    turtle.fd(distance/3)
    x4,y4 = turtle.xcor(), turtle.ycor()
    turtle.right(90)
    turtle.fd(distance/3)
    x5,y5 = turtle.xcor(), turtle.ycor()
    turtle.right(90)
    turtle.fd(distance/3)
    x6,y6 = turtle.xcor(), turtle.ycor()
    koch(x1,y1,x3,y3)
    koch(x3,y3,x4,y4)
    koch(x4,y4,x5,y5)
    koch(x5,y5,x6,y6)
    koch(x6,y6,x2,y2)
    

koch(500,-200,-500,-200)
koch(-500,-200,0,500*3**0.5-200)
koch(0,500*3**0.5-200,500,-200)
screen.update()