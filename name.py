import turtle

screen = turtle.Screen()
screen.setup(width=1000, height=400)
screen.bgcolor("white")
pen = turtle.Turtle()
pen.color("black")
pen.pensize(3)
pen.speed(1)

# draw M
# pen.up()
# pen.goto(-300,0)
# pen.left(50)
# pen.down()
# pen.forward(150)
# pen.up()
# pen.right(140)
# pen.down()
# pen.forward(200)
# pen.up()
# pen.goto(0,0)
# pen.left(220)
# pen.down()
# pen.forward(150)
# pen.up()
# pen.left(140)
# pen.down()
# pen.forward(200)
# pen.up()
#
# #draw 0
# pen.goto(200,0)
# pen.down()
# pen.circle(115)
# pen.up()
pen.down()
# pen.right(180)
for i in range(90):
    pen.forward(2)
    pen.right(2)


while True:
    screen.update()
