# -*- coding: utf-8 -*-
"""
presentation.py
===============

Context decorator for producing figures suitable in presentation for
Mac OS Keynote or Microsoft PowerPoint.

"""
import numpy as np

from .general import MPLdecorator, point2inch, GOLDEN_RATIO
from .colors import brewer_set1

__all__ = ['presentation', ]

# Constants for presentation
_width_full_pt = 1024
_width_normal_pt = int(_width_full_pt / 3.0)
width_normal = point2inch(_width_normal_pt)
width_tiny = 0.5 * width_normal
width_small = 0.8 * width_normal
width_large = 1.2 * width_normal
width_large2 = 1.5 * width_normal
width_huge = 1.8 * width_normal
width_full = 0.9 * point2inch(_width_full_pt)  # use 90% of presentation page.

# Default ratio for a single plot figure
# Golden ratio
height_width_ratio = GOLDEN_RATIO  # = height / width

_width = width_normal
_height = width_normal * height_width_ratio

_params = {'font.family' : 'sans-serif',
          'font.serif' : ['Times', 'Computer Modern Roman'],
          'font.sans-serif' : ['Helvetica', 'Computer Modern Sans serif'],
          'text.usetex' : True,

          'axes.color_cycle': brewer_set1,
          'axes.labelsize' : 14,
          'axes.linewidth' : 1.5,

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

          'legend.fontsize' : 12,
          'legend.frameon' : False,
          'legend.numpoints' : 1,
          'legend.handlelength' : 2,
          'legend.scatterpoints' : 1,

          'text.fontsize' : 12,

          'xtick.major.size' : 6,
          #'xtick.minor.size' : 2,
          'xtick.major.width' : 1.5,
          #'xtick.minor.width' : 0.5,
          #'xtick.major.pad' : 4,
          #'xtick.minor.pad' : 4,
          #'xtick.color' : k,
          'xtick.labelsize' : 12,
          #'xtick.direction' : 'in',

          'ytick.major.size' : 6,
          #'ytick.minor.size' : 2,
          'ytick.major.width' : 1,
          #'ytick.minor.width' : 0.5,
          #'ytick.major.pad' : 4,
          #'ytick.minor.pad' : 4,
          #'ytick.color' : k,
          'ytick.labelsize' : 12,
          #'ytick.direction' : 'in',

          'lines.linewidth' : 1.5,
          'lines.markersize' : 6,
          #'lines.markeredgewidth' : 0,
          # 0 will make line-type markers, such as '+', 'x', invisible
         }

presentation = MPLdecorator(_params)

