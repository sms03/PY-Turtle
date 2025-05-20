import turtle
screen = turtle.Screen()
screen.title('Curvy Fractal Tree - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def tree(x,y,length,direction):
    if length < 2: return    
    turtle.up()
    turtle.goto(x,y)
    turtle.pensize(length/30)
    turtle.down()
    turtle.seth(direction)
    if length<10: turtle.color('dim gray')
    else: turtle.color('black')
    
    turtle.fd(length)

    px,py = turtle.xcor(), turtle.ycor()
    tree(px,py,length*0.9,direction+25)
    tree(px,py,length*0.45,direction-90)

tree(400,-500,300,90)
screen.update()