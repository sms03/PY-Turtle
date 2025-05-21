import turtle
import random
import math

screen = turtle.Screen()
screen.title('Sierpinski Pentagon with Chaos Game - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-250,-250,250,250)
screen.tracer(0,0)
turtle.hideturtle()
turtle.speed(0)
turtle.up()

m=5
angle = math.pi/2
V = []
for i in range(m):
    p = (400*math.cos(angle),400*math.sin(angle))
    V.append(p)
    angle += math.pi*2/m

for v in V:
    turtle.goto(v)
    turtle.dot('red')

n = 100000 # number of points to draw
p = V[0] # start from first vertex
t = turtle.Turtle()
t.up()
t.hideturtle()
for i in range(n):
    t.goto(p)
    t.dot(2,'orange')
    q = V[random.randrange(len(V))] # pick a random vertex
    p = ((q[0]+p[0])/2.6,(q[1]+p[1])/2.6) # go to mid point between the random vertex and point   
    if i % 1000 == 0: # update for every 1000 moves, this part is for performance reason only
        t = turtle.Turtle() # use new turutle
        t.up()
        t.hideturtle()
        screen.update()