# -*- coding: utf-8 -*-
"""
colors.py
=========

A set of colors and color maps as provided by python package `palettable` (https://jiffyclub.github.io/palettable).

"""

import numpy as np

from palettable.colorbrewer.qualitative import Set1_9
from palettable.tableau import Tableau_10, Tableau_20
from cycler import cycler

# Set some commonly used colors
almost_black = '#262626'
light_grey = np.array([float(248) / float(255)] * 3)

# ColorBrewer
# by Drs. Cynthia Brewer and Mark Harrower of Pennsylvania
# State University. For more information on ColorBrewer, see:
# - Flash-based interactive map:
# http://colorbrewer2.org/
# - A quick visual reference to every ColorBrewer scale:
# http://bl.ocks.org/mbostock/5577023
# https://jiffyclub.github.io/palettable/colorbrewer
#
# ColorBrewer scale 'Qualitative.Set1'.
# This one has nice "traditional" colors like reds and blues
# It is suitable for multi-line plots and category items.
brewer_set1 = Set1_9.mpl_colors
# Remove the sixth color (yellow) which is too bright
brewer_set1.pop(5)
# Swap the red and blue to let blue come first
brewer_set1[0], brewer_set1[1] = brewer_set1[1], brewer_set1[0]
# Add a decent black color to this list
brewer_set1.append(almost_black)

# Tableau 10 & 20 Classic
# See: https://jiffyclub.github.io/palettable/tableau/
# Another great qualitative set of colors suitable for multi-line plots.
# 10 and 20 are number of colors in the list.
tableau_10 = Tableau_10.mpl_colors
# Add a decent black color
tableau_10.append(almost_black)
# Swap orange and red
tableau_10[1], tableau_10[3] = tableau_10[3], tableau_10[1]
# swap orange and purple
# now table_au has similar sequence to brewer_set1
tableau_10[3], tableau_10[4] = tableau_10[4], tableau_10[3]
# This is 20-color Tableau which contains light version of tableau_10
tableau_20 = Tableau_20.mpl_colors

default_color_cycler = cycler('color', tableau_10)
