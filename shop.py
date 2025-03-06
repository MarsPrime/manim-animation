from manim import *

color = ( '#710008', '#FF5964')
#color = ('#232B39', '#7284A8')
#color = ('#241024', '#6D326D')
#color = ('#077C63', "#95F9E3")
#color = ('#685307', '#F4D35E')
class ShopAnimation(Scene):
    def construct(self):
        self.camera.background_color = convert_color(color[0])
        text = Text("Магазин", color=convert_color(color[1]), font_size=30, font="Russo One")
        text.shift(LEFT * -6)
        text.shift(DOWN * 3)

        rect = Rectangle(width=4, height=9, fill_opacity=1, color=convert_color(color[1]))
        rect.shift(LEFT * 6)
        # the beginning of animation
        self.play(Write(text), Create(rect))
        self.play(Wait(5))

        # idle animation
        self.play(text.animate.shift(LEFT * 20), run_time=10)

        text.shift(RIGHT * 25)
        self.play(text.animate.shift(LEFT * 5), run_time=10)


def convert_color(color : str):
    return rgb_to_color(hex_to_rgb(color))

