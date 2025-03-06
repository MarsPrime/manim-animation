from manim import *
import numpy

class MainMenuAnimation(Scene):
    def construct(self):
        self.camera.background_color = rgb_to_color(hex_to_rgb('#946CCD'))
        rect = BackGroundRectangle('#660099', 9, 6, -5, 3).return_new_rectangle()
        rect2 = BackGroundRectangle('#660099', 7, 5, -4, -4).return_new_rectangle()
        rect3 = BackGroundRectangle('#7748B7', 7, 9, -9, -1).return_new_rectangle()

        self.play(Rotate(rect, angle=-45),
                  Rotate(rect2, angle=-45),
                  Rotate(rect3, angle=-125),
                  run_time=0.001)
        self.wait(.1)
        self.add(rect, rect2)
        self.add(rect3)

        self.play(GrowFromCenter(rect), GrowFromCenter(rect2), GrowFromCenter(rect3), run_time=0.5)


class BackGroundRectangle():
    def __init__(self, color, width, height, position_x, position_y):
        self.color = color
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y

    def return_new_rectangle(self):
        self.rectangle = Rectangle(
                color=(rgb_to_color(hex_to_rgb(self.color))),
                width=self.width,
                height=self.height,
                fill_opacity=1
                                   )
        self.rectangle.shift(LEFT * self.position_x)
        self.rectangle.shift(UP * self.position_y)

        return self.rectangle
