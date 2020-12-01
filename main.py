import math

import matplotlib.pyplot as plt
import plotly.graph_objects as go


def p(w: float):
    return (19.5 * w ** 2) / ((0.36 * w ** 2 + 1) * (0.03 * w ** 2 + 1))


def q(w):
    return (25 * (w - 0.1 * w ** 3)) / ((0.36 * w ** 2 + 1) * (0.03 * w ** 2 + 1))


def simple(w):
    return w


def get_value_list_in_range(f, fro: float, to: float, delta: float):
    res = []
    num = fro
    while num <= to:
        res.append(round(f(num), 3))
        num += delta
    return res


def get_table(p: list, q: list, w: list):
    fig = go.Figure(data=[go.Table(header=dict(values=['W', 'P', 'Q']),
                                   cells=dict(values=[w, p, q],
                                              align='center'))
                          ])

    fig.show()


def add_annotations(ax, p: list, q: list, w: list):
    for i, dig in enumerate(w):
        annotation = f"w={dig}"
        if dig < 7:
            ax.annotate(annotation, (p[i], q[i]), ha='center', va='bottom')


def first_rgr_function(t):
    return 2 * t ** 2 / 27 + 4 * t / 81 + 3800 / 243 * math.exp(-3 * t) - 1804 / 243 * math.exp(
        -3 * t / 2) + 3218 / 81 * t * math.exp(-3 * t / 2) - 52 / 43


def show_simple_graph(f):
    fig, ax = plt.subplots()
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    data = get_value_list_in_range(f, 0, 20, 0.2)
    x = get_value_list_in_range(simple, 0, 20, 0.2)
    ax.scatter(x, data)

    plt.show()


if __name__ == '__main__':
    fig, ax = plt.subplots()
    w_min = 0
    w_max = 50
    step = 0.5
    ax.set_xlabel('P')
    ax.set_ylabel('Q')
    p = get_value_list_in_range(p, w_min, w_max, step)
    q = get_value_list_in_range(q, w_min, w_max, step)
    w = get_value_list_in_range(simple, w_min, w_max, step)
    ax.scatter(p, q)
    add_annotations(ax, p, q, w)
    ax.set(title=f'График для w от {w_min} до {w_max}')

    plt.show()
    get_table(p, q, w)
