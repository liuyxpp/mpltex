# -*- coding: utf-8 -*-
"""
styles.py
=========

Toolkits and constants for plotting styles.

"""

import itertools

from .colors import almost_black, brewer_set1

__all__ = ['lines', 'markers', 'nextlinestyle', 'linestyle_generator']


_colors = itertools.cycle(brewer_set1)

_line_styles = ['-', '--', '-.', ':']
lines = itertools.cycle(_line_styles)

_markers = ['o', 's', 'v', '^', 'D', 'p', 'h', '<', '>']
markers = itertools.cycle(_markers)

# for making hollow markers, use it together with marker_types
_markersh = ['o', 'o', 's', 's', 'v', 'v', '^', '^', 'D', 'D']
markersh = itertools.cycle(_markersh)

_marker_types = [False, True]  # True for hollow markers
marker_types = itertools.cycle(_marker_types)

def nextlinestyle(no_line=False, is_line=True, is_marker=True, is_hollow=True):
     """
     Generate a dict for configuring plot line style.

     NOTE: this function has a serious problem.
     As long as mpltex is imported,
     the beginning of the sequence cannot be configured later.
     This function is obsolete, please use linestyle_generator instead.

     The default line style is markers linked by lines, both styles are cycled,
     and hollow markers are included.
     Disable cycling one style by set the corresponding flag to False.

     :param no_line: if True, only markers, no line segments
     :type no_line: bool
     :param is_line: if True, cycle line styles. No effect when no_line=True.
     :type is_line: bool
     :param is_marker: if True, cycle markers.
     :type is_marker: bool
     :param is_hollow: if True, cycle markers including hollow styles.
     :param is_hollow: bool
     :return: dict of parameters of linestyle
     :rtype: dict
     """
     color = _colors.next()
     linestyle = lines.next()
     if(is_hollow):
          marker = markersh.next()
     else:
          marker = markers.next()
     marker_type = marker_types.next()
     if marker_type:  # hollow mark
          mew = 1
          mec = color
          mfc = 'None'
     else:
          mew = 1
          mec = color
          mfc = color

     linestyles = {}
     if (is_line):
          linestyles['linestyle'] = linestyle
     if (no_line):  # overwrite is_line if no_line is True
          linestyles['linestyle'] = ''
     if (is_marker):
          linestyles['marker'] = marker
          linestyles['mew'] = 0  # make the marker no edge
     if (is_hollow):
          linestyles['color'] = color
          linestyles['marker'] = marker
          linestyles['mew'] = mew
          linestyles['mec'] = mec
          linestyles['mfc'] = mfc
     return linestyles


def linestyle_generator(colors=brewer_set1, lines=_line_styles,
                        markers=_markers, hollow_styles=_marker_types):
     """
     Generate a dict for configuring plot line styles.

     The default line style is markers linked by lines, both styles are cycled,
     and hollow markers are included.

     Usage:
          linestyles = linestyle_generator()
          linestyle = linestyles.next()

     To exclude hollow markers, just let hollow_styles = [None].
     Note that all inputs should be iterable objects.

     :param colors: list of colors (tuple of RGB or #FFFFFF
                    or color name string)
     :type colors: list of tuple or list of string
     :param lines: list of line styles ('-', '--', '-.', ':')
     :type is_line: list of string
     :param markers: list of markers (see matplot for available markers)
     :type marker: list of charaters
     :param hollow_styles: True for hollow markers, False for filled markers.
     :param is_hollow: list of bool
     :return: dict of parameters of linestyle
     :rtype: dict
     """
     color_cycle = itertools.cycle(colors)
     line_cycle = itertools.cycle(lines)
     full_markers = itertools.product(markers, hollow_styles)
     marker_cycle = itertools.cycle(full_markers)
     while True:
        color = color_cycle.next()
        linestyle = line_cycle.next()
        marker, hollow = marker_cycle.next()
        if hollow is None:  # don't cycle hollow markers
            mew = 0
            mec = 'None'
            mfc = color
        elif hollow:  # make hollow markers
            mew = 1
            mec = color
            mfc = 'None'
        else:  # make filled markers
            mew = 1
            mec = color
            mfc = color
        yield {'linestyle':linestyle, 'marker':marker, 'mew':mew, 'mec':mec, 'mfc':mfc}
