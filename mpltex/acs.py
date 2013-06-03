# -*- coding: utf-8 -*-
"""
acs.py
======

The figure format options for American Chemical Society.

"""

import matplotlib.pyplot as plt

params = {'font.family' : 'serif',
          'font.serif' : ['Times', 'Computer Modern Roman'],
          'font.sans-serif' : ['Helvetica', 'Computer Modern Sans serif'],
          'text.usetex' : True,

          'axes.labelsize' : 9,
          'axes.linewidth' : 1,

          'figure.figsize' : (3.25, 2.45),
          'figure.subplot.left' : 0.125,
          'figure.subplot.right' : 0.95,
          'figure.subplot.bottom' : 0.1,
          'figure.subplot.top' : 0.95,

          'figure.dpi' : 150,
          'savefig.dpi' : 600,

          'text.fontsize' : 8,
          'legend.fontsize' : 7.5,
          'xtick.labelsize' : 8,
          'ytick.labelsize' : 8,

          'lines.linewidth' : 1,
          'lines.markersize' : 4,
          #'lines.markeredgewidth' : 0, # it will make the tick width 0
         }

plt.rcParams.update(params)

