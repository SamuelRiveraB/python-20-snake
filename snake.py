from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.start = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for p in self.start:
            new = Turtle('square')
            new.color('white')
            new.up()
            new.teleport(p[0], p[1])
            self.segments.append(new)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        for seg in self.segments:
            if seg.heading() != DOWN:
                seg.setheading(UP)

    def down(self):
        for seg in self.segments:
            if seg.heading() != UP:
                seg.setheading(DOWN)

    def left(self):
        for seg in self.segments:
            if seg.heading() != RIGHT:
                seg.setheading(LEFT)

    def right(self):
        for seg in self.segments:
            if seg.heading() != LEFT:
                seg.setheading(RIGHT)