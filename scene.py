from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))
        self.wait()

class Txt(Scene):
    def construct(self):
        text1 = Text("Dirac's Equation", color=BLUE)
        text1.scale(1.5).to_edge(UP)

        eqn = Tex(r'(i$\partial$ - m)$\psi$ = 0')

        where = Text('Where, ').scale(0.75)

        i_num = Tex(r'i = \text{imaginary number}').scale(0.75)
        p_d = Tex(r'$\partial$ = \text{differential in 4-Dimension}').scale(0.75)
        m = Tex(r'm = \text{fermion mass}').scale(0.75)
        psi = Tex(r'$\psi$ = \text{fermion wave function}').scale(0.75)

        self.play(Write(text1))

        self.play(Write(eqn))
        self.play(ApplyMethod(eqn.shift, 2*UP))

        self.play(Write(where.shift(0.5*UP + 4*LEFT)))
        self.play(Write(i_num.shift(2*LEFT)))
        self.play(Write(p_d.shift(1.35*LEFT + 0.5*DOWN)))
        self.play(Write(m.shift(2.5*LEFT + 1*DOWN)))
        self.play(Write(psi.shift(1.7*LEFT + 1.5*DOWN)))

class ScalarField(ThreeDScene):
    def construct(self):
        title = Text("Trying out 3D Graphs", color=GREEN, font="Noto Sans")
        
        axes = ThreeDAxes(x_range=[-4,4], x_length=4)

        func = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU]
        ) 

        self.play(Write(title))
        self.wait(1)

        self.play(Uncreate(title))

        self.move_camera(0.8*np.pi / 2, -0.45 * np.pi)

        self.play(Write(axes))
        self.play(Write(func))
        self.begin_ambient_camera_rotation()
        self.wait(4)

    @staticmethod
    def func(u,v):
       return np.array([
            u,
            v,
            np.sin(5*u)*(np.cos(5*v))/5
        ])
