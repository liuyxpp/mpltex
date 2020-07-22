# -*- coding: utf-8 -*-

import matplotlib as mpl
mpl.use('Agg')  # To avoid launching interactive plot, such as wxAgg.
import matplotlib.pyplot as plt

import mpltex

import numpy as np

def plot(ax):
    # Set the random seed for consistency
    np.random.seed(12)

    # Show the whole color range
    for i in range(8):
        y = np.random.normal(size=1000).cumsum()
        x = np.arange(1000)

        ax.plot(x, y, label=str(i))

    ax.set_xlabel('$\\text{Number of steps,}\; N$')
    ax.set_ylabel('$\\text{Distance,}\; \lambda$')
    ax.legend(loc='best', ncol=4)


@mpltex.presentation_decorator
def test_plot_presentation():
    fig, ax = plt.subplots(1)
    plot(ax)
    fig.tight_layout(pad=0.35)
    fig.savefig('test_plot_presentation')
    plt.close()


@mpltex.acs_decorator
def test_plot_acs():
    fig, ax = plt.subplots(1)
    plot(ax)
    fig.tight_layout(pad=0.35)
    fig.savefig('test_plot_acs')
    plt.close()


@mpltex.rsc_decorator
def test_plot_aps():
    fig, ax = plt.subplots(1)
    plot(ax)
    fig.tight_layout(pad=0.35)
    fig.savefig('test_plot_aps')
    plt.close()


@mpltex.aps_decorator
def test_plot_rsc():
    fig, ax = plt.subplots(1)
    plot(ax)
    fig.tight_layout(pad=0.35)
    fig.savefig('test_plot_aps')
    plt.close()


@mpltex.web_decorator
def test_plot_web():
    fig, ax = plt.subplots(1)
    plot(ax)
    fig.tight_layout(pad=0.35)
    fig.savefig('test_plot_web')
    plt.close()


@mpltex.web_decorator
def test_plot_scatter():
    # Set the random seed for consistency
    np.random.seed(12)

    fig, ax = plt.subplots(1)

    # The default line style is iterating over color, line, and marker with
    # hollow types.
    linestyle = mpltex.linestyle_generator(colors=[],
                                           lines=['-', ':'],
                                           markers=['o', 's'],
                                           hollow_styles=[False, False, True, True],
                                           )
    for i in range(8):
        y = np.random.normal(size=10).cumsum()
        x = np.arange(10)
        ax.plot(x, y, label=str(i), **next(linestyle))

    ax.locator_params(nbins=5)
    ax.set_xlabel('Number of steps')
    ax.set_ylabel('Distance')
    ax.legend(loc='best', ncol=4)

    fig.tight_layout(pad=0.35)
    fig.savefig('test_special_custom_linestyle_generator')


if __name__ == '__main__':
    test_plot_presentation()
    test_plot_acs()
    test_plot_rsc()
    test_plot_web()
    test_plot_aps()
    test_plot_scatter()
