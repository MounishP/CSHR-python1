import turtle

name = input("please enter your name : ")
turtle.speed(1)
turtle.color("blue")
turtle.write(name, align="right", font=("Bembo", 32, "bold"))
turtle.done()