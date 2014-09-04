# -*- coding: utf-8 -*-
"""
acs.py
======

Context decorator for producing figures which is ready to publish
in American Chemical Society.

"""
import numpy as np

from .general import MPLdecorator
from .colors import brewer_set1

__all__ = ['acs', ]

# Constants from ACS Authour Guidelines.
width_single_column = 3.25
width_double_column = 7.00

# Default ratio for a single plot figure
# Golden ratio
height_width_ratio = (np.sqrt(5) - 1) / 2  # = height / width

_width = width_single_column
_height = width_single_column * height_width_ratio

params = {'font.family' : 'serif',
          'font.serif' : ['Times', 'Computer Modern Roman'],
          'font.sans-serif' : ['Helvetica', 'Computer Modern Sans serif'],
          'text.usetex' : True,

          'axes.color_cycle': brewer_set1,
          'axes.labelsize' : 9,
          'axes.linewidth' : 1,

          'figure.figsize' : (_width, _height),
          'figure.subplot.left' : 0.125,
          'figure.subplot.right' : 0.95,
          'figure.subplot.bottom' : 0.1,
          'figure.subplot.top' : 0.95,
          'figure.dpi' : 300,

          'savefig.dpi' : 300,
          'savefig.format': 'eps',
          #'savefig.bbox': 'tight',
          # this will crop white spaces around images that will make
          # width/height no longer the same as the specified one.

          'legend.fontsize' : 7.5,
          'legend.frameon' : False,
          'legend.numpoints' : 1,
          'legend.handlelength' : 2,
          'legend.scatterpoints' : 1,

          'text.fontsize' : 8,
          'xtick.labelsize' : 8,
          'ytick.labelsize' : 8,

          'lines.linewidth' : 1,
          'lines.markersize' : 4,
          #'lines.markeredgewidth' : 0,
          # 0 will make line-type markers, such as '+', 'x', invisible
         }

acs = MPLdecorator(params)

