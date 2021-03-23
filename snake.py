from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.blocks = []
        self.__create_snake()
        self.head = self.blocks[0]

    def move(self):
        for block in range(len(self.blocks) - 1, 0, -1):
            xcor = self.blocks[block - 1].xcor()
            ycor = self.blocks[block - 1].ycor()
            self.blocks[block].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def __create_snake(self):
        for position in POSITIONS:
            self.add_blocks(position)

    def add_blocks(self, position):
        block = Turtle('square')
        block.color('white')
        block.penup()
        block.goto(position)
        self.blocks.append(block)

    def extend(self):
        self.add_blocks(self.blocks[-1].position())
