import turtle
screen = turtle.Screen()
screen.title('Sierpinski with Squares - PythonTurtle.Academy')
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def sierpinkski_square(x,y,length,n):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(0)
    if n>0: turtle.color('light gray')
    else: turtle.color('blue')
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)
    if n==0: return       
    
    sierpinkski_square(x+length,y,length/2,n-1)
    sierpinkski_square(x+length,y+length,length/2,n-1)
    sierpinkski_square(x,y+length,length/2,n-1)

sierpinkski_square(-800,-800,800,6)
screen.update()