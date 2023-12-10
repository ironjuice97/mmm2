
import turtle
from Point import Point

MARBLE_RADIUS = 15

class Marble:
    shared_pen = turtle.Turtle()
    shared_pen.hideturtle()
    shared_pen.speed(0)

    def __init__(self, position, color, size=MARBLE_RADIUS):
        self.pen = Marble.shared_pen
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.size = size

    def set_color(self, color):
        self.color = color
        self.is_empty = False

    def draw(self):
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)

    def erase(self):
        self.visible = False
        self.pen.clear()

    def get_color(self):
        return self.color

    def clicked_in_region(self, x, y):
        return abs(x - self.position.x) <= self.size * 2 and abs(y - self.position.y) <= self.size * 2

    def move(self, dx, dy):
        self.position.x += dx
        self.position.y += dy
        if self.visible:
            if self.is_empty:
                self.draw_empty()
            else:
                self.draw()
