mpltex
======

``mpltex`` is a python package for producing publication quality images using ``matplotlib``.
Inspired by `Olga Botvinnik <http://olgabotvinnik.com/>`_'s python package `prettyplotlib <https://github.com/olgabot/prettyplotlib>`_.

The internal ``matplotlib`` color cycle is replaced by ColorBrewer Set1 scale which looks less saturated and more pleasing to eyes.
For more information on ColorBrewer, see `a flash-based interactive map <http://colorbrewer2.org/>`_ and `a quick visual reference to all ColorBrewer scales <http://bl.ocks.org/mbostock/5577023>`_.

``mpltex`` also enable cycle line styles and a selected set of line markers.
Hollow markers are supported.

Quickstart
----------

1. Install
^^^^^^^^^^

::

    $ pip install mpltex

**Required Packages**

-  `matplotlib <http://matplotlib.org/>`_. Can be installed via
   ``pip install matplotlib``.
-  `brewer2mpl <https://github.com/jiffyclub/brewer2mpl>`_. Can be
   installed via ``pip install brewer2mpl``.

2. Usage
^^^^^^^^

Examples and sample plots can be found `here <http://ngpy.org/post/mpltex/>`_.

Following is a breif introduction. Just add one of ``mpltex`` decorators before your plot functions.

.. code:: python

    import mpltex

    @mpltex.acs_decorator
    def your_plot():
        # plot images by matplotlib ...

        # Save the image. Give a file name without extension.
        # You can also save figure outside your_plot if you like.
        fig.save_fig('/path/to/save/fig/figname')

    # Then use your_plot in a normal way.
    your_plot()

And it will create a plot ready for publishing in journals published by American Chemical Society (ACS).

``mpltex`` also contains several helper functions to faciliate production of specific type of images.
Following codes will produce a set of line arts with cycled line styles and line markers with the help of ``mpltex.linestyle_generator`` function.

.. code:: python

    import matplotlib.pyplot as plt
    import mpltex

    @mpltex.acs_decorator
    def your_plot():
        # ...   # generate data x and y
        fig, ax = plt.subplots(111)

        # The default line style is iterating over
        # color, line, and marker with hollow types.
        linestyles = mpltex.linestyle_generator()

        for i in range(number_of_lines):
            ax.plot(x[i], y[i], label=str(i), **linestyles.next())

        ax.locator_params(nbins=5)  # limit the number of major ticks
        ax.legend(loc='best')  # show legend in a best location
        fig.tight_layout(pad=0.1)  # make layout as tight as possible
        fig.savefig('/path/to/save/fig/figname')

**Available Decorators**

* ``mpltex.acs_decorator``: output EPS images for publishing in ACS.
* ``mpltex.presentation_decorator``: output PDF images for presentation slides (Keynote).
* ``mpltex.web_decorator``: output PNG images for web pages.

Contribute
----------

Let me know what you think and wish. I can be reached through `email <mailto:liuyxpp@gmail.com>`_ or `other ways <http://ngpy.org/about>`_. Or fork the project at `github.com <https://github.com/liuyxpp/mpltex>`_ and file a pull request.

Links
-----

* `Yi-Xin Liu's personal website <http://ngpy.org>`_
* `Development version at github.com <https://github.com/liuyxpp/mpltex>`_

