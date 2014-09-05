# -*- coding: utf-8 -*-
"""
layout.py
=========

Toolkits and constants for plotting layout.

"""

__all__ = ['point2inch', 'inch2point', 'GOLDEN_RATIO', 'GOLDEN_RATIO2',]


GOLDEN_RATIO = 0.618
GOLDEN_RATIO2 = 1.618

def point2inch(npt, dpi=72.0):
     """
     Point to inch converter.

     :param npt: number of points
     :type npt: integer
     :return: number of inches corresponding to :param:`npt`
     :type: double
     """
     return 1.0 * npt / dpi


def inch2point(inch, dpi=72.0):
     """
     Inch to point converter.

     :param inch: the length in unit inch
     :type inch: double
     :return: number of points corresponding to :param:`inch`
     :rtype: integer
     """
     return int(dpi * inch)
