from manim import *
import random


drawn_objects = []
class DrawMenu(Scene):
    def construct(self):
        DrawLines(self)
        MoveLinesToCenter(self)




class RandomLine():
    def __init__(self):
        self.color = random_color()
        self.start_point = Point(location=[0, 10, 0])
        self.end_point = Point(location = [0, -10, 0])

    def set_new_line_parameters(self):
        line = Line(
                color=self.color,
                start = self.start_point,
                end = self.end_point
                )
        return line

def DrawLines(self):
    for i in range(30):
        new_right_line = RandomLine().set_new_line_parameters()
        new_right_line.shift(RIGHT * 6)
        new_right_line.shift(LEFT * i * 0.09)

        new_left_line = RandomLine().set_new_line_parameters()
        new_left_line.shift(LEFT * 6)
        new_left_line.shift(RIGHT * i * 0.09)

        self.play(Create(new_right_line), Create(new_left_line), run_time=0.0001)
        drawn_objects.append(new_right_line)
        drawn_objects.append(new_left_line)

def MoveLinesToCenter(self):
    for i in range(len(drawn_objects)):
        if i % 2 == 0:
            drawn_objects[i].shift(RIGHT * -6)
            self.play(drawn_objects[i].animate,  run_time=0.001)
        else:
            drawn_objects[i].shift(LEFT * -6)
            self.play(drawn_objects[i].animate,  run_time=0.001)
        

