import turtle
import math

screen = turtle.Screen()
screen.title('Pentagon Spiral of Pentagon Spirals - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)

def draw_spiral(x,y,r,direction):
    if r < 1: return
    d = direction
    r_ratio = math.cos(math.radians(36))/math.cos(math.radians(36-alpha))
    d_ratio = math.sin(math.radians(36))-r_ratio*math.sin(math.radians(36-alpha))
    for _ in range(5):
        px = x + r*math.cos(math.radians(direction))
        py = y + r*math.sin(math.radians(direction))
        r2 = r
        d = direction
        c = 0
        flag = False
        while True:
            dist = r2*d_ratio
            if c > 10 and dist < 1: break
            if dist > 3:
                draw_spiral(px,py,dist*0.5,d)
                turtle.up()
                turtle.goto(px,py)
                turtle.seth(d+180-54)
                turtle.fd(dist)
                px,py = turtle.xcor(), turtle.ycor()
            elif not flag:
                turtle.up()
                turtle.goto(px,py)
                turtle.down()
                flag = True
                turtle.seth(d+180-54)
                turtle.fd(dist)
            else:   
                turtle.seth(d+180-54)
                turtle.fd(dist)
    
            r2 = r2*r_ratio
            d += alpha
            c += 1
        direction += 360/5
    
    
alpha = 20
draw_spiral(0,0,800,90)
screen.update()
ts=turtle.getscreen()
ts.getcanvas().postscript(file = "spiral.eps")