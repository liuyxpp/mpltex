mpltex
======

``mpltex`` is a python package for producing publication quality images using ``matplotlib``, which is inspired by `Olga Botvinnik <http://olgabotvinnik.com/>`_'s python package `prettyplotlib <https://github.com/olgabot/prettyplotlib>`_. Tutorial can be found at `www.yxliu.group <http://www.yxliu.group/2014/09/mpltex>`_.

The internal ``matplotlib`` color cycle is replaced by Tableau classic 10 color scheme which looks less saturated and more pleasing to eyes.
The colors of this scheme is reordered, which is different from current version of ``matplotlib`` v3.
Other available color schemes for multi-line plots are ColorBrewer Set 1 and Tableau classic 20.
For more information on these color schemes, see `documentation of palettable <https://jiffyclub.github.io/palettable>`_.

``mpltex`` also provide a way to generate highly configurable line styles with colors, line types, and line markers.
Hollow markers are supported.

``mpltex`` should work properly both in Python 2 and 3. If not, please file an issue at `Github <https://github.com/liuyxpp/mpltex>`_.

Quickstart
----------

1. Install
^^^^^^^^^^

::

    $ pip install mpltex

**Required Packages**

-  `matplotlib <http://matplotlib.org/>`_. Can be installed via
   ``pip install matplotlib``.
-  `palettable <https://github.com/jiffyclub/palettable>`_. Can be
   installed via ``pip install palettable``.

2. Usage
^^^^^^^^

Examples and sample plots can be found `here <http://www.yxliu.group/2014/09/mpltex>`_.

To use `mpltex`, just add one of ``mpltex`` decorators before your plot functions.

.. code:: python

    import mpltex

    @mpltex.acs_decorator
    def myplot():
        # plot images by matplotlib ...

        # Save the image. Give a file name without extension.
        # You can also save figure outside your_plot if you like.
        fig.save_fig('/path/to/save/fig/figname')

    # Then use your_plot in a normal way.
    myplot()

And it will create a plot ready for publishing in journals published by American Chemical Society (ACS).

**Available Decorators**

* ``mpltex.acs_decorator``: output EPS images for publishing in ACS (American Chemical Society).
* ``mpltex.aps_decorator``: output EPS images for publishing in APS (American Physical Society).
* ``mpltex.rsc_decorator``: output EPS images for publishing in RSC (Royal Society of Chemistry).
* ``mpltex.presentation_decorator``: output PDF images for presentation slides (Keynote).
* ``mpltex.web_decorator``: output PNG images for web pages.

``mpltex`` also provides several helper functions to facilitate production of specific type of images.
Following codes will produce a set of line arts with cycled line styles with the help of ``mpltex.linestyle_generator`` function.
Note that since version 0.5, ``linestyles`` is a shorthand for ``linestyle_generator``.

.. code:: python

    import matplotlib.pyplot as plt
    import mpltex

    @mpltex.acs_decorator
    def myplot():
        # ...   # generate data x and y
        fig, ax = plt.subplots(111)

        # The default line style is iterating over
        # color, line, and marker with hollow types.
        linestyles = mpltex.linestyles()
        # equivalently
        # linestyles = mpltex.linestyle_generator()

        for i in range(number_of_lines):
            ax.plot(x[i], y[i], label=str(i), **next(linestyles)

        ax.locator_params(nbins=5)  # limit the number of major ticks
        ax.legend(loc='best')  # show legend in a best location
        fig.tight_layout(pad=0.1)  # make layout as tight as possible
        fig.savefig('/path/to/save/fig/figname')

Contribute
----------

Fork the project at `github.com <https://github.com/liuyxpp/mpltex>`_ and file a pull request.

Links
-----

* `Yi-Xin Liu's personal academic website <http://www.yxliu.group>`_
* `Development version at github.com <https://github.com/liuyxpp/mpltex>`_
