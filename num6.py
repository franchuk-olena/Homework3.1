import turtle

class number6:
    def __init__(self):
        self.position = (0, -235)

    def draw(self):
        turtle.color("#800080")
        turtle.penup()
        turtle.goto(self.position)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(13)
        turtle.setheading(300)
        turtle.forward(27)
        turtle.setheading(240)
        turtle.forward(27)
        turtle.setheading(180)
        turtle.forward(27)
        turtle.setheading(120)
        turtle.forward(27)
        turtle.setheading(60)
        turtle.forward(27)
        turtle.setheading(0)
        turtle.forward(13)
        turtle.setheading(180)
        turtle.forward(13)
        turtle.setheading(240)
        turtle.forward(27)
        turtle.setheading(90)
        turtle.forward(49)
        turtle.setheading(60)
        turtle.forward(27)
        turtle.setheading(0)
        turtle.forward(27)
        turtle.setheading(300)
        turtle.forward(27)

if __name__ == '__main__':
    six=number6()
    six.draw()
    turtle.mainloop()