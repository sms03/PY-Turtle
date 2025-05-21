import turtle

screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
screen.title('Recursive Triangles - PythonTurtle.Academy')
turtle.hideturtle()

def draw_triangle(x,y,s,angle):
    turtle.up()
    turtle.seth(angle)
    turtle.goto(x,y)
    turtle.fd(s/3**0.5)
    turtle.right(150)
    turtle.down()
    turtle.color('dodger blue')
    turtle.begin_fill()
    turtle.fd(s)
    turtle.right(120)
    turtle.fd(s)
    turtle.right(120)
    turtle.fd(s)
    turtle.end_fill()
    
def recursive_triangles(x,y,s,angle,n):
    if n==0: return
    turtle.goto(x,y)
    draw_triangle(x,y,s,angle)
    a = angle+60
    for _ in range(3):
        turtle.up()
        turtle.goto(x,y)
        turtle.seth(a)
        turtle.fd(1.3*s)
        x1,y1 = turtle.xcor(), turtle.ycor()
        recursive_triangles(x1,y1,s/2.1,a,n-1)
        a += 120

recursive_triangles(0,50,200,90,7)

screen.update()