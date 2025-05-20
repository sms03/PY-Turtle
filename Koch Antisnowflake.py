import turtle
import math

screen = turtle.Screen()
screen.title('Koch Antisnowflake - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()
turtle.fillcolor('blue')

def koch_anti(x1,y1,x2,y2):
    dist = ((x2-x1)**2+(y2-y1)**2)**0.5
    if dist<50:
        turtle.goto(x2,y2)
        return
    direction = math.atan2(y2-y1,x2-x1)
    px1, py1 = x1+dist/3*math.cos(direction), y1+dist/3*math.sin(direction)
    px2, py2 = px1+dist/3*math.cos(direction-math.radians(60)), py1+dist/3*math.sin(direction-math.radians(60))
    px3, py3 = x1+2*dist/3*math.cos(direction), y1+2*dist/3*math.sin(direction)
        
    koch_anti(x1,y1,px1,py1)
    koch_anti(px1,py1,px2,py2)
    koch_anti(px2,py2,px3,py3)
    koch_anti(px3,py3,x2,y2)

turtle.up()
turtle.goto(800,-600)
turtle.down()
koch_anti(800,-600,-800,-600)
koch_anti(-800,-600,0,-600+1600*3**0.5/2)
koch_anti(0,-600+1600*3**0.5/2,800,-600)

a=input()