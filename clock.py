import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Analog clock")
screen.tracer()

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(10)


def drawClock():
    pen.up()
    pen.goto(0,-210)


while True:
    drawClock()
    screen.update()