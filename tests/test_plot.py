# -*- coding: utf-8 -*-
"""
test_plot
=========



"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

import mpltex

import numpy as np

@mpltex.acs
def test():
    # Set the random seed for consistency
    np.random.seed(12)

    fig, ax = plt.subplots(1)

    # Show the whole color range
    for i in range(8):
        y = np.random.normal(size=1000).cumsum()
        x = np.arange(1000)

        ax.plot(x, y, label=str(i))

    plt.legend(loc='best', ncol=4)

    fig.savefig('test_plot')

@mpltex.presentation
def test2():
    # Set the random seed for consistency
    np.random.seed(12)

    fig, ax = plt.subplots(1)

    # Show the whole color range
    for i in range(8):
        y = np.random.normal(size=10).cumsum()
        x = np.arange(10)

        # The default line style is iterating over color, line, and marker with
        # hollow types.
        linestyle = mpltex.nextlinestyle(#no_line=True,
                                         #is_line=True,
                                         #is_marker=False,
                                         #is_hollow=False,
                                         )
        ax.plot(x, y, label=str(i), **linestyle)
                #linestyle=mpltex.lines.next(),
                #marker=mpltex.markers.next(),
                #mew=0.15, mec=mpltex.almost_black,
                #label=str(i))
        ax.locator_params(nbins=5)
        ax.set_xlabel('Numer of steps')
        ax.set_ylabel('Distance')

    ax.legend(loc='best', ncol=4)

    fig.tight_layout(pad=0.1)
    fig.savefig('test_plot_scatter')

if __name__ == '__main__':
    #test()
    test2()


