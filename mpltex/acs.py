# -*- coding: utf-8 -*-
"""
acs.py
======

Context decorator for producing figures which is ready to publish
in American Chemical Society.

"""
from .general import MPLdecorator
from .colors import brewer_set1

__all__ = ['acs', ]

params = {'font.family' : 'serif',
          'font.serif' : ['Times', 'Computer Modern Roman'],
          'font.sans-serif' : ['Helvetica', 'Computer Modern Sans serif'],
          'text.usetex' : True,

          'axes.color_cycle': brewer_set1,
          'axes.labelsize' : 9,
          'axes.linewidth' : 1,

          'figure.figsize' : (3.25, 2.45),
          'figure.subplot.left' : 0.125,
          'figure.subplot.right' : 0.95,
          'figure.subplot.bottom' : 0.1,
          'figure.subplot.top' : 0.95,
          'figure.dpi' : 300,

          'savefig.dpi' : 300,
          'savefig.format': 'eps',
          'savefig.bbox': 'tight',

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

