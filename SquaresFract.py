import turtle
screen = turtle.Screen()
screen.title('Squares - PythonTurtle.Academy')
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()
turtle.color('green')

def squares(x,y,length,n):
    if n==0: return       
    turtle.up()
    turtle.goto(x-length/2,y-length/2)
    turtle.down()
    turtle.seth(0)
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)

    squares(x,y+3*length/4,length/2,n-1)
    squares(x,y-3*length/4,length/2,n-1)
    squares(x+3*length/4,y,length/2,n-1)
    squares(x-3*length/4,y,length/2,n-1)
    
squares(0,0,500,6)
screen.update()