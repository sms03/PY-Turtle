import turtle
turtle.title('Fractal Tree - PythonTurtle.Academy')
turtle.setworldcoordinates(-2000,-2000,2000,2000)
screen = turtle.Screen()
screen.tracer(0,0)
turtle.hideturtle()

def sierpinski_tree(x,y,length,tilt,n):
    if n==0: return
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),n-1)
    
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt+20)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),n-1)

    turtle.up()
    turtle.goto(x,y)
    turtle.seth(tilt-20)
    turtle.down()
    turtle.fd(length)
    sierpinski_tree(turtle.xcor(),turtle.ycor(),length/2,turtle.heading(),n-1)

sierpinski_tree(0,-250,1000,90,7)
screen.update()
a=input()