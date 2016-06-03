import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    
    
    raekwon = turtle.Turtle()
    raekwon.shape("turtle")
    raekwon.color("blue")

    rae_line = 0

    while (rae_line < 4):
        raekwon.forward(100)
        raekwon.right(90)
        rae_line = rae_line + 1

    queen = turtle.Turtle()
    queen.color("yellow")
    queen.circle(100)

    premiere = turtle.Turtle()
    premiere.color("white")

    primo = 0

    while (primo < 3):
        premiere.forward(100)
        premiere.right(120)
        primo = primo + 1



    window.exitonclick()

draw_shapes()
