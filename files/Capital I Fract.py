import turtle
screen = turtle.Screen()
screen.title('Capital I - PythonTurtle.Academy')
turtle.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()
turtle.color('blue')

def capitalI(x,y,length,n):
    if n==0: return       
    turtle.up()
    turtle.goto(x-length,y+length)
    turtle.down()
    turtle.seth(0)
    turtle.fd(2*length)
    turtle.up()
    turtle.goto(x-length,y-length)
    turtle.down()
    turtle.fd(2*length)
    turtle.up()
    turtle.goto(x,y+length)
    turtle.down()
    turtle.seth(270)
    turtle.fd(2*length)
    
    capitalI(x-length,y+length,length/2,n-1)
    capitalI(x+length,y+length,length/2,n-1)
    capitalI(x+length,y-length,length/2,n-1)
    capitalI(x-length,y-length,length/2,n-1)
    
capitalI(0,0,450,4)
screen.update()