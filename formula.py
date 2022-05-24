from manim import *

class Formula(Scene):
    def construct(self):
        f1 = Tex('$E = mc^2')

        self.play(Write(f1))
        self.wait(1)
