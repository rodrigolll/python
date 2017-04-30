import turtle
t = turtle.Pen()


def draw_star(size,point):
    for x in range(1,point):
        t.forward(size)
        t.left(95)
