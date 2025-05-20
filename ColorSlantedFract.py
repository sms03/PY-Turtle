import turtle

screen = turtle.Screen()
screen.title('Slanted Fractal Tree - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
turtle.speed(0)
turtle.hideturtle()

def slanted_tree(x,y,length,direction):
    if length < 2: return
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(direction)
    turtle.pensize(length/50)
    if length > 20: turtle.color('saddle brown')
    else: turtle.color('green')
    turtle.fd(length)
    px,py = turtle.xcor(), turtle.ycor()
    slanted_tree(px,py,length*0.7,direction-30)
    slanted_tree(px,py,length*0.7,direction+60)

L=400
slanted_tree(100,-500,L,90)
screen.update()