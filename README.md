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
pip install manim
```

## First Project
Create `scene.py` :
```python
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
```
Save this file. Then, run the following command:
```sh
# Saves @ 1080p60f and preview the scene
manim scene.py Shapes -p
```

If you want to render and save this scene in different resolutions:
```sh
# Saves @ 480p15f (add -p to preview)
manim scene.py Shapes -ql

# Saves @ 2160p60f
manim scene.py Shapes -qk
```
To save every frame as png:
```sh
# Saves low quality png
manim scene.py -ql --format=png
```

## Working with text
`textscene.py` :
```python
from manim import *

class Txt(Scene):
    def construct(self):
        t1 = Text('Text Animations')
        t2 = Text('In Manim', color=BLUE)

        t2.next_to(t1, DOWN)

        self.play(Write(t1))
        self.play(write(t2))
        self.wait(1)
```

## Working with Tex
`formula.py` :
```python
from manim import *

class Formula(Scene):
    def construct(self):
        f1 = Tex('$E = mc^2')

        self.play(Write(f1))
        self.wait(1)