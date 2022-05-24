from manim import *

class Txt(Scene):
    def construct(self):
        t1 = Text('Text Animations')
        t2 = Text('In Manim', color=BLUE)

        t2.next_to(t1, DOWN)

        self.play(Write(t1))
        self.play(write(t2))
        self.wait(1)
