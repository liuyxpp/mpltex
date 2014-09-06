# -*- coding: utf-8 -*-
"""
colors.py
=========

A set of colors and color maps.

"""

import numpy as np

import brewer2mpl
from matplotlib import cm

# ColorBrewer by Drs. Cynthia Brewer and Mark Harrower of Pennsylvania
# State University. For more information on ColorBrewer, see:
# - Flash-based interactive map:
# http://colorbrewer2.org/
# - A quick visual reference to every ColorBrewer scale:
# http://bl.ocks.org/mbostock/5577023

# ColorBrewer scale 'Qualitative.Set1'.
# This one has nice "traditional" colors like reds and blues
brewer_set1 = brewer2mpl.get_map('Set1', 'qualitative', 9).mpl_colors

# ColorBrewer scale 'Qualitative.Set2'.
# This one are lesssaturated than those colors in Set1.
brewer_set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# ColorBrewer scale 'Qualitative.Accent'.
brewer_accent = brewer2mpl.get_map('Accent', 'qualitative', 8).mpl_colors

# ColorBrewer scale 'Qualitative.Dark2'.
brewer_dark2 = brewer2mpl.get_map('Dark2', 'qualitative', 8).mpl_colors

# ColorBrewer scale 'Qualitative.Paired'.
brewer_paired = brewer2mpl.get_map('Paired', 'qualitative', 12).mpl_colors

# Set some commonly used colors
almost_black = '#262626'
light_grey = np.array([float(248) / float(255)] * 3)

# Color maps
reds = cm.Reds
reds.set_bad('white')
reds.set_under('white')

blues_r = cm.Blues_r
blues_r.set_bad('white')
blues_r.set_under('white')

# Need to 'reverse' red to blue so that blue=cold=small numbers,
# and red=hot=large numbers with '_r' suffix
brewer_blue_red = brewer2mpl.get_map('RdBu', 'Diverging', 11,
                                     reverse=True).mpl_colormap

