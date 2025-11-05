from manim import *

class ParabolaAnimada(Scene):
    def construct(self):
        # Parâmetros fixos
        a = 1
        c = 0

        # Cria o ValueTracker de b antes de usar
        self.b = ValueTracker(-4)

        # Eixos
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 10, 2],
            x_length=8,
            y_length=5,
            axis_config={"color": GREY_A},
        ).add_coordinates()
        labels = axes.get_axis_labels("x", "y")

        self.play(Create(axes), Write(labels))

        # Texto explicativo
        title = Text("Variação do coeficiente b", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Função parabólica genérica
        parabola = always_redraw(lambda: axes.plot(
            lambda x: a*x**2 + self.b.get_value()*x + c,
            color=BLUE
        ))

        # Vértice (depende de b)
        vertex_dot = always_redraw(lambda: Dot(
            axes.c2p(
                -self.b.get_value() / (2 * a),
                - (self.b.get_value() ** 2) / (4 * a) + c
            ),
            color=YELLOW
        ))

        # Linha vertical x = -b/(2a)
        vertex_line = always_redraw(lambda: axes.get_vertical_line(
            axes.c2p(-self.b.get_value() / (2 * a), 0),
            color=YELLOW, stroke_width=2
        ))

        # Valor de b mostrado na tela
        b_label = always_redraw(lambda: MathTex(
            f"b = {self.b.get_value():.1f}"
        ).to_corner(UL).set_color(WHITE))

        # Adiciona objetos
        self.add(parabola, vertex_dot, vertex_line, b_label)

        # Anima a variação de b
        self.play(self.b.animate.set_value(4), run_time=8, rate_func=there_and_back)

        self.wait(1)
