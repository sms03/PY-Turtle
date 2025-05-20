import turtle

screen = turtle.Screen()
screen.setup(1000,1000)
screen.title("Arrow Tessellation - PythonTurtle.Academy")
#screen.tracer(0)
#turtle.speed(0)
#turtle.hideturtle()

def draw_arrow(x,y,size,tilt,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.pensize(2)
    turtle.pencolor((0.4,0.4,0.4))
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.seth(tilt)
    turtle.fd(size)
    turtle.right(90)
    turtle.fd(size/4)
    turtle.left(120)
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(size/4)
    turtle.right(90)
    turtle.fd(size)
    turtle.left(90)
    turtle.fd(size/2)
    turtle.end_fill()

size = 100
for y in range(-500,600,size):
    x = -500
    for i in range(6):
        draw_arrow(x,y,size,0,'red')
        draw_arrow(x+size,y,size,180,'light green')
        x += size + 3**0.5/2*size
#screen.update()