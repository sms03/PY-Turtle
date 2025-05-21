import turtle
import math

screen = turtle.Screen()
screen.title('6 Line Snowflake Fractal - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.tracer(0,0)
turtle.hideturtle()
turtle.speed(0)

def line(x,y,length,direction,pensize):
  turtle.up()
  turtle.pensize(pensize)
  turtle.goto(x,y)
  turtle.down()
  turtle.seth(direction)
  turtle.fd(length)

def line_fractal(x,y,length,direction,pensize,n):
  if n==0: return
  line(x,y,length,direction,pensize)
  line_fractal(x+math.cos(direction*math.pi/180)*length*2/5,
               y+math.sin(direction*math.pi/180)*length*2/5,
               length*3/5,
               direction-25,
               pensize*3/5,
               n-1)
  line_fractal(x+math.cos(direction*math.pi/180)*length*2/5,
               y+math.sin(direction*math.pi/180)*length*2/5,
               length*3/5,
               direction+25,
               pensize*3/5,
               n-1)

def snowflake():
  for i in range(6):
    line_fractal(0,0,400,i*60,5,5)

snowflake()
screen.update()