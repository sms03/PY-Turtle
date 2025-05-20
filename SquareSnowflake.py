import turtle

screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
screen.title('Square Snowflake - PythonTurtle.Academy')
turtle.hideturtle()

def draw_square(x,y,s):
    turtle.up()
    turtle.goto(x-s/2,y-s/2)
    turtle.down()
    turtle.seth(0)
    turtle.fillcolor('sky blue')
    turtle.begin_fill()
    turtle.fd(s)
    turtle.left(90)
    turtle.fd(s)
    turtle.left(90)
    turtle.fd(s)
    turtle.left(90)
    turtle.fd(s)
    turtle.left(90)
    turtle.end_fill()
    
def draw_squares(x,y,s,n):
    if n == 0: return

    draw_square(x,y,s)
    draw_squares(x+s*1.5,y,s/2.5,n-1)
    draw_squares(x,y+s*1.5,s/2.5,n-1)
    draw_squares(x,y-s*1.5,s/2.5,n-1)
    draw_squares(x-s*1.5,y,s/2.5,n-1)

draw_squares(0,0,200,6)
screen.update()