import turtle
import colorsys

screen = turtle.Screen()
screen.title('Vicsek Fractal Colored - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)
screen.bgcolor('dark gray')
turtle.speed(0)
turtle.hideturtle()

def draw_cross(x,y,length):
    turtle.up()
    turtle.goto(x-length/2,y-length/6)
    turtle.down()
    turtle.seth(0)
    h = (x**2+y**2)**0.5/L*1.7
    c = colorsys.hsv_to_rgb(h,1,1)
    turtle.color(c)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length/3)
        turtle.right(90)
        turtle.fd(length/3)
        turtle.left(90)
        turtle.fd(length/3)
        turtle.left(90)      
    turtle.end_fill()

def vicsek(x,y,length,n):
    if n==0:
        draw_cross(x,y,length)
        return

    vicsek(x,y,length/3,n-1)
    vicsek(x+length/3,y,length/3,n-1)
    vicsek(x-length/3,y,length/3,n-1)
    vicsek(x,y+length/3,length/3,n-1)
    vicsek(x,y-length/3,length/3,n-1)

L = 1600   
vicsek(0,0,L,5)
screen.update()
a=input()