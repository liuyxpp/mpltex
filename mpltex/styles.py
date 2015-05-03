# -*- coding: utf-8 -*-
"""
styles.py
=========

Toolkits and constants for plotting styles.

"""

import itertools

from .colors import almost_black, brewer_set1

__all__ = ['lines', 'markers', 'nextlinestyle', 'linestyle_generator']

_colors = brewer_set1
colors = itertools.cycle(_colors)

_lines = ['-', '--', '-.', ':']
lines = itertools.cycle(_lines)

_markers = ['o', 's', 'v', '^', 'D', 'p', 'h', '<', '>']
markers = itertools.cycle(_markers)

# for making hollow markers, use it together with marker_types
_markersh = ['o', 'o', 's', 's', 'v', 'v', '^', '^', 'D', 'D']
markersh = itertools.cycle(_markersh)

_marker_types = [False, True]  # True for hollow markers
marker_types = itertools.cycle(_marker_types)


def linestyle_generator(colors=_colors, lines=_lines,
                        markers=_markers, hollow_styles=_marker_types):
    """
    Generate a dict for configuring plot line styles.

    The default line style is markers linked by lines, both styles are cycled,
    and hollow markers are included.

    Usage::

      linestyles = linestyle_generator()
      linestyle = linestyles.next()

    Note that all inputs should be iterable objects.
    To exclude one style, just pass empty list or ``None`` to the corresponding argument.
    To include one style but not cycle, just pass a single-element list.
    For example, pass ``lines=['-'] to apply solid line style to all line arts.
    Similarly, passing ``markers=['o']`` will apply filled circle only.

    :param colors: list of colors, (tuple of RGB or #FFFFFF
                or color name string)
    :type colors: list of tuple or list of string or ``None``
    :param lines: list of line styles within ('-', '--', '-.', ':')
    :type lines: list of string,  or ``None``
    :param markers: list of markers (see matplotlib for available markers)
    :type markers: list of charaters,  or ``None``
    :param hollow_styles: True for hollow markers, False for filled markers.
    :param hollow_styles: list of bool,  or ``None``
    :return: dict of parameters of linestyle
    :rtype: dict
    """

    # If both lines and markers are empty or None, do nothing
    is_nothing = False
    if not lines and not markers:
        is_nothing = True

    if colors:
        color_cycle = itertools.cycle(colors)
    else:  # default line color is almost_black
        color_cycle = itertools.cycle([almost_black])

    if lines:
        line_cycle = itertools.cycle(lines)
    else:  # empty list or None supplied, disable line connection
        line_cycle = itertools.cycle([''])

    if markers and hollow_styles:  # solid and hollow markers
        full_markers = itertools.product(markers, hollow_styles)
    elif markers and not hollow_styles:  # all solid markers
        full_markers = itertools.product(markers, [None])
    else:  # no markers
        full_markers = itertools.product(['None'], [None])
    marker_cycle = itertools.cycle(full_markers)

    while True:
        if not is_nothing:
            color = color_cycle.next()
            linestyle = line_cycle.next()
            marker, hollow = marker_cycle.next()
            if hollow is None:  # only filled markers
                mew = 1
                mec = color
                mfc = color
            elif hollow:  # make hollow markers
                mew = 1
                mec = color
                mfc = 'None'
            else:  # otherwise, make filled markers
                mew = 1
                mec = color
                mfc = color
            yield {'color': color, 'linestyle':linestyle,
                   'marker':marker, 'mew':mew, 'mec':mec, 'mfc':mfc}
        else:
            yield {}


def nextlinestyle(no_line=False, is_line=True, is_marker=True, is_hollow=True):
    """
    Generate a dict for configuring plot line style.

    NOTE: this function has a serious problem.
    As long as mpltex is imported,
    the beginning of the sequence cannot be configured later.
    This function is obsolete since version 0.2, please use linestyle_generator instead.

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
    color = colors.next()
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
