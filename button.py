from manim import *
import numpy

class ButtonAnimation(Scene):
    def construct(self):
        rectangle = Button_Rectangle('#D9C5B2', width=10, height=4).set_parameters()
        self.play(DrawBorderThenFill(rectangle), run_time=1)
        text = Button_Text("Начать игру", '#34312D').set_parameters()
        self.play(Wait(2))


class Button_Rectangle():
    def __init__(self, color, width, height):
        self.color = hex_to_rgb(color)
        self.width = width
        self.height = height

    def set_parameters(self):
        self.rect = Rectangle(color=self.color, width=self.width, 
                              height=self.height, fill_opacity=1)
        return self.rect
