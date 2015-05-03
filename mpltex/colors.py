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
# Remove the sixth color (yellow) which is too bright
brewer_set1.pop(5)

# ColorBrewer scale 'Qualitative.Set2'.
# This one are less saturated than those colors in Set1.
brewer_set2 = brewer2mpl.get_map('Set2', 'qualitative', 8).mpl_colors

# ColorBrewer scale 'Qualitative.Set3'.
# This one are even less saturated than those colors in Set1.
brewer_set3 = brewer2mpl.get_map('Set3', 'qualitative', 12).mpl_colors
# Remove the second color (yellow) which is too bright
brewer_set3.pop(1)

# ColorBrewer scale 'Qualitative.Accent'.
brewer_accent = brewer2mpl.get_map('Accent', 'qualitative', 8).mpl_colors
# Remove the fourth color (yellow) which is too bright
brewer_accent.pop(3)

# ColorBrewer scale 'Qualitative.Dark2'.
brewer_dark2 = brewer2mpl.get_map('Dark2', 'qualitative', 8).mpl_colors

# ColorBrewer scale 'Qualitative.Paired'.
brewer_paired = brewer2mpl.get_map('Paired', 'qualitative', 12).mpl_colors
# Remove the 11th and 12th colors (yellow and brown) which is too bright
brewer_paired.pop(11)
brewer_paired.pop(10)

# ColorBrewer scale 'Qualitative.Pastel1'.
brewer_pastel1 = brewer2mpl.get_map('Pastel1', 'qualitative', 9).mpl_colors

# ColorBrewer scale 'Qualitative.Pastel2'.
brewer_pastel2 = brewer2mpl.get_map('Pastel2', 'qualitative', 8).mpl_colors

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

