# Manim Cheat Sheet

## Requirements
1. Install [miniforge](https://github.com/conda-forge/miniforge)
2. ffmpeg
3. MacTex
    ```sh
   brew install mactex
    ```
4. pango
    ```sh
   brew install pango
    ```

## Installation
```sh
# Inside conda environment
pip install manimlib
```

## First Project
`scene.py` Shapes class:
```python
from manimlib.imports import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        self.play(ShowCreation(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))
        self.wait(1)
```
Save this file. Then, run the following command:
```sh
# Saves @ 1440p60f
manim scene.py Shapes
```

If you want to render and save this scene in different resolutions:
```sh
# Saves @ 480p15f (add -p to preview)
manim scene.py Shapes -ql

# Render in desired resolution
manim scene.py Shapes -r 2160,3840
```
To save every last frame as png:
```sh
manim scene.py -s
```

## Working with text
`scene.py`  Txt class:
```python
class Txt(Scene):
    def construct(self):
        text1 = TextMobject("Dirac's Equation", color=BLUE)
        text1.scale(1.5).to_edge(UP)

        eqn = TexMobject(r"(i \partial - m)\psi = 0")

        where = TextMobject("Where, ").scale(0.75)

        i_num = TexMobject(r"i = \text{imaginary number}").scale(0.75)
        p_d = TexMobject(r"\partial = \text{differential in 4-Dimension}").scale(0.75)
        m = TexMobject(r"m = \text{fermion mass}").scale(0.75)
        psi = TexMobject(r"\psi = \text{fermion wave function}").scale(0.75)

        self.play(Write(text1))

        self.play(Write(eqn))
        self.play(ApplyMethod(eqn.shift, 2*UP))

        self.play(Write(where.shift(0.5*UP + 4*LEFT)))
        self.play(Write(i_num.shift(2*LEFT)))
        self.play(Write(p_d.shift(1.35*LEFT + 0.5*DOWN)))
        self.play(Write(m.shift(2.5*LEFT + 1*DOWN)))
        self.play(Write(psi.shift(1.7*LEFT + 1.5*DOWN)))
```