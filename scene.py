from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(circle))
        self.wait(1)
        self.play(FadeOut(circle))
        self.wait(1)
        self.play(Create(square))
        self.play(FadeOut(square))
