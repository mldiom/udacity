import turtle


def triangle():
    window = turtle.Screen()
    window.bgcolor("red")

    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.color("yellow")
    bob.speed(5)

    for a in range (1,30):

        side = 0
        while side < 3:
            bob.forward(100)
            bob.right(120)
            side = side + 1
        if side == 3:
            bob.right(10)
            side = side - 3


triangle()
