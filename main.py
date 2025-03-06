from manim import *

class DrawRectangle(Scene):
    def construct(self):

        for i in range(99):
            rect = DrawableRectangle(random_color(), 5, 5, 1, 1)
            object = rect.create_rectangle()
            self.play(Create(object))

class DrawableRectangle():
    def __init__(self, color, height, width, grid_xstep, grid_ystep):
        self.color = color
        self.height = height
        self.width = width
        self.grid_xstep = grid_xstep
        self.grid_ystep = grid_ystep


    def create_rectangle(self):
        new_rectangle = Rectangle(
                color = self.color,
                height = self.height,
                width = self.width, 
                grid_xstep = self.grid_xstep,
                grid_ystep = self.grid_ystep)

        return new_rectangle
