import turtle
import random
import time

screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
screen.title('Insertion Sort Animation - PythonTurtle.Academy')
turtle.speed(0)
turtle.hideturtle()

def draw_bar(x,y,w,h):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

def draw_bars(v,n):
    x = -400
    w = 800/n
    for  i in range(n):
        draw_bar(x,-400,w,v[i])
        x += w

def insert(v,k):
    x = v[k]
    for i in range(k-1,-1,-1):
        if v[i] > x: v[i+1] = v[i]
        else:
            v[i+1] = x
            return
        turtle.clear()
        draw_bars(v,n)
        screen.update()
    v[0] = x
    
def insertion_sort(v,k):
    if k == 1: return
    insertion_sort(v,k-1)
    insert(v,k-1)
    
n = 50
v = [0] * n
for i in range(n):
    v[i] = random.randint(1,800)

t1 = time.time()
insertion_sort(v,n)
t2 = time.time()
print('elapsed time=', t2-t1)