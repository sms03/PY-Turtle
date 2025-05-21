import turtle

screen = turtle.Screen()
screen.title('Slanted Fractal Tree - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def slanted_tree(x,y,length,direction):
    if length < 7: return
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(direction)
    turtle.pensize(length/50)
    turtle.fd(length)
    px,py = turtle.xcor(), turtle.ycor()
    slanted_tree(px,py,length*0.75,direction+45)
    slanted_tree(px,py,length*0.75,direction-15)
    
slanted_tree(100,-500,300,90)