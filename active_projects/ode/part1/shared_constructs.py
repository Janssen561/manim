from big_ol_pile_of_manim_imports import *


Lg_formula_config = {
    "tex_to_color_map": {
        "\\theta_0": WHITE,
        "{L}": BLUE,
        "{g}": YELLOW,
    },
}


class You(PiCreature):
    CONFIG = {
        "color": BLUE_C,
    }


def get_ode():
    tex_config = {
        "tex_to_color_map": {
            "{\\theta}": BLUE,
            "{\\dot\\theta}": YELLOW,
            "{\\ddot\\theta}": RED,
            "{t}": WHITE,
            "{\\mu}": WHITE,
        }
    }
    ode = TexMobject(
        "{\\ddot\\theta}({t})", "=",
        "-{\\mu} {\\dot\\theta}({t})",
        "-{g \\over L} \\sin\\big({\\theta}({t})\\big)",
        **tex_config,
    )
    return ode


def pendulum_vector_field_func(point, mu=0.1, g=9.8, L=3):
    theta, omega = point[:2]
    return np.array([
        omega,
        -np.sqrt(g / L) * np.sin(theta) - mu * omega,
        0,
    ])


def get_vector_symbol(*texs, **kwargs):
    config = {
        "include_background_rectangle": True,
        "bracket_h_buff": SMALL_BUFF,
        "bracket_v_buff": SMALL_BUFF,
        "element_alignment_corner": ORIGIN,
    }
    config.update(kwargs)
    array = [[tex] for tex in texs]
    return Matrix(array, **config)
