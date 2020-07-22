# -*- coding: utf-8 -*-
"""
presentation.py
===============

Context decorator for producing figures suitable in presentation for
Mac OS Keynote or Microsoft PowerPoint.

PDF format for image file are used, because it correctly uses sans-serif fonts.

"""

from .general import MPLdecorator
from .layout import point2inch, GOLDEN_RATIO
from .colors import default_color_cycler
from .styles import latex_preamble

__all__ = ['presentation_decorator', ]

# Constants for presentation
_width_full_pt = 1024  # Units in number of points (or dots)
_width_normal_pt = int(_width_full_pt / 3.0)
width_normal = point2inch(_width_normal_pt)
width_tiny = 0.5 * width_normal
width_small = 0.8 * width_normal
width_large = 1.2 * width_normal
width_large2 = 1.5 * width_normal
width_huge = 1.8 * width_normal
width_full = 0.9 * point2inch(_width_full_pt)  # use 90% of presentation page.

# Default ratio for a single plot figure
# I prefer a little higher than goden ratio, from 0.618 to 0.68
height_width_ratio = GOLDEN_RATIO * 1.1  # = height / width

_width = width_normal
_height = _width * height_width_ratio

_params = {'font.family': 'sans-serif',
           'font.serif': ['Times', 'Computer Modern Roman'],
           'font.sans-serif': ['Helvetica', 'Arial', 'Lucida Grande'],
           'font.size': 12,
           'font.weight': 'normal',
           'text.usetex': True,
           # To force LaTeX use Helvetica fonts.
           'text.latex.preamble': latex_preamble,
           'axes.prop_cycle': default_color_cycler,
           'axes.labelsize': 'medium',
           'axes.labelweight': 'normal',
           'axes.linewidth': 1.5,

           'figure.figsize': (_width, _height),
           'figure.subplot.left': 0.125,
           'figure.subplot.right': 0.95,
           'figure.subplot.bottom': 0.1,
           'figure.subplot.top': 0.95,

           'savefig.dpi': 300,
           'savefig.format': 'pdf',
           # 'savefig.bbox': 'tight',
           # this will crop white spaces around images that will make
           # width/height no longer the same as the specified one.

           'legend.fontsize': 'small',
           'legend.frameon': False,
           'legend.numpoints': 1,
           'legend.handlelength': 2,
           'legend.scatterpoints': 1,
           'legend.labelspacing': 0.5,
           'legend.markerscale': 0.9,
           'legend.handletextpad': 0.5,  # pad between handle and text
           'legend.borderaxespad': 0.5,  # pad between legend and axes
           'legend.borderpad': 0.5,  # pad between legend and legend content
           'legend.columnspacing': 1,  # pad between each legend column

           # 'text.fontsize': 'medium',

           'xtick.major.size': 6,
           # 'xtick.minor.size' : 2,
           'xtick.major.width': 1.5,
           # 'xtick.minor.width' : 0.5,
           # 'xtick.major.pad' : 4,
           # 'xtick.minor.pad' : 4,
           # 'xtick.color' : k,
           'xtick.labelsize': 'medium',

           'ytick.major.size': 6,
           # 'ytick.minor.size' : 2,
           'ytick.major.width': 1.5,
           # 'ytick.minor.width' : 0.5,
           # 'ytick.major.pad' : 4,
           # 'ytick.minor.pad' : 4,
           # 'ytick.color' : k,
           'ytick.labelsize': 'medium',

           'lines.linewidth': 1.5,
           'lines.markersize': 6,
           # 'lines.markeredgewidth' : 0,
           # 0 will make line-type markers, such as '+', 'x', invisible

           # Revert some properties to mpl v1 which is more suitable for publishing
           'axes.autolimit_mode': 'round_numbers',
           'axes.xmargin': 0,
           'axes.ymargin': 0,
           'xtick.direction': 'in',
           'xtick.top': True,
           'ytick.direction' : 'in',
           'ytick.right': True,
           }

presentation_decorator = MPLdecorator(_params)
