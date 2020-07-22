# -*- coding: utf-8 -*-
"""
web.py
======

Context decorator for producing figures suitable for web pages.

PNG format for image file are used, because in web pages the pixel unit
and speed are most important.

NOTE:
DPI or PPI is not important for PNG images. but it is critical in
matplotlib. Matplotlib uses physical unit for its plot.
Therefore, for same number of pixels, higher DPI will require smaller
physical size in inch. But small physical size will cause plotting
problems.
It is obvious now we should choose a DPI that best matches the current working
screen, so that matplotlib will draw things nicely.

"""

from .general import MPLdecorator
from .layout import GOLDEN_RATIO, point2inch
from .colors import default_color_cycler
from .styles import latex_preamble

__all__ = ['web_decorator', ]

# Constants for web
_width_normal_px = 440
save_dpi = 150
width_normal = point2inch(_width_normal_px, save_dpi)
width_tiny = 0.5 * width_normal
width_small = 0.8 * width_normal
width_large = 1.2 * width_normal
width_large2 = 1.5 * width_normal
width_huge = 1.8 * width_normal

# Default ratio for a single plot figure
# I prefer a little higher than goden ratio, from 0.618 to 0.68
height_width_ratio = GOLDEN_RATIO * 1.1  # = height / width

_width = width_normal
_height = _width * height_width_ratio

_line_width = 0.8

_params = {'font.family': 'sans-serif',
           'font.serif': ['Bitstream Vera Serif', 'Computer Modern Roman'],
           'font.sans-serif': ['Helvetica', 'Arial', 'Lucida Grande'],
           'font.size': 7,
           'font.weight': 'normal',
           'text.usetex': True,
           # To force LaTeX use Helvetica fonts.
           'text.latex.preamble': latex_preamble,
           'axes.prop_cycle': default_color_cycler,
           'axes.labelsize': 'medium',
           'axes.labelweight': 'normal',
           'axes.linewidth': _line_width,

           'figure.figsize': (_width, _height),
           'figure.subplot.left': 0.125,
           'figure.subplot.right': 0.95,
           'figure.subplot.bottom': 0.1,
           'figure.subplot.top': 0.95,

           'savefig.dpi': save_dpi,
           'savefig.format': 'png',
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
           # pad between legend and legend content
           'legend.borderpad': 0.5,
           # pad between each legend column
           'legend.columnspacing': 1,

           # 'text.fontsize' : 'medium',
           'xtick.major.size': 3,
           # 'xtick.minor.size': 2,
           'xtick.major.width': _line_width,
           # 'xtick.minor.width': 0.5,
           'xtick.major.pad': 2,
           # 'xtick.minor.pad': 4,
           # 'xtick.color' : k,
           'xtick.labelsize': 'medium',
           'ytick.major.size': 3,
           # 'ytick.minor.size': 2,
           'ytick.major.width': _line_width,
           # 'ytick.minor.width': 0.5,
           'ytick.major.pad': 2,
           # 'ytick.minor.pad': 4,
           # 'ytick.color': k,
           'ytick.labelsize': 'medium',
           'lines.linewidth': _line_width,
           'lines.markersize': 3,
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

web_decorator = MPLdecorator(_params)
