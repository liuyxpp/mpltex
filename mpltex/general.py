# -*- coding: utf-8 -*-
"""
general.py
==========

A general class for producing context decorators for matplotlib.

"""

from functools import wraps
import itertools
import matplotlib as mpl

from .colors import almost_black, brewer_set1

__all__ = ['MPLdecorator', 'lines', 'markers', 'nextlinestyle']

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


class MPLdecorator:
     """
     An :class:`MPLdecorator` instance represents a specific context-decorator
     that makes it possible to configure matplotlib parameters
     without affecting matplotlib.pyplot.

     Parameters
     ----------
     :param rcp: matplotlib parameter settings
     :type rcp: dict

     Attributes
     ----------
     :param rcParams: matplotlib parameter settings
     :type rcParams: dict
     :param mpl_contexts: matplotlib rc contexts
     :type mpl_contexts: list of matplotlib.rc_context

     """
     mpl_contexts = []

     def __init__(self, rcp):
          self.rcParams = rcp

     def __call__(self, func):
          @wraps(func)
          def wrapper(*args, **kwargs):
               with self:
                    return func(*args, **kwargs)
          return wrapper

     def __enter__(self):
          context = mpl.rc_context(rc=self.rcParams)
          self.mpl_contexts.append(context)
          return context.__enter__()

     def __exit__(self, *args):
          return self.mpl_contexts.pop().__exit__(*args)

