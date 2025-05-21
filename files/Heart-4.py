import turtle

pen=turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(111.65)
    curve()
    pen.left(120)
    curve()
    pen.forward(111.65)
    pen.end_fill()

def text():
        pen.up()
        pen.setpos(0, -20)
        pen.down()
        pen.color('Red')
        pen.write("I Love You!", font=("Arial", 12, "bold"))

heart()
text()
pen.ht()
turtle.done()
a=input()