# -*- coding: utf-8 -*-
"""
general.py
==========

General toolkits.

"""

from functools import wraps
import matplotlib as mpl

__all__ = ['MPLdecorator',]


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
