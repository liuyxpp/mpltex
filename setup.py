"""
mpltex
======

**mpltex** is a python package for producing publication quality images using matplotlib.
Inspired by `Olga Botvinnik <http://olgabotvinnik.com/>`_'s python package `prettyplot <https://github.com/olgabot/prettyplotlib>`_.

The internal matplotlib color cycle is replaced by ColorBrewer Set1 scale which looks less saturated and more pleasing to eyes.
For more information on ColorBrewer, see `a flash-based interactive map <http://colorbrewer2.org/>`_ and `a quick visual reference to all ColorBrewer scales <http://bl.ocks.org/mbostock/5577023>`_.

**mpltex** also enable cycle line styles and a selected set of line markers.
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

Just add one of **mpltex** decorators before your plot functions.

.. code:: python

    import mpltex

    @mpltex.acs_decorators
    def your_plot():
        # plot images by matplotlib ...

        # Save the image. Give a file name without extension.
        # You can also save figure outside your_plot if you like.
        fig.save_fig('/path/to/save/fig/figname')

    # Then use your_plot in a normal way.
    your_plot()

And it will produce images suitable for publishing in American Chemical Society (ACS).

**mpltex** also includes several helper functions to faciliate production of specific type of images.
Following code will produce a set of line arts with cycled line styles and line markers

.. code:: python

    @mpltex.acs_decorator
    def your_plot(x, y):
        fig, ax = plt.subplots(111)
        for i in range(x.size):
            # The default line style is iterating over
            # color, line, and marker with hollow types.
            linestyle = mpltex.nextlinestyle()
            ax.plot(x[i], y[i], label=str(i), **linestyle)

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

Please do not hesitate to submit your own configurations.
I will add them to the package.

Links
-----

* `Yi-Xin Liu's personal website <http://ngpy.org>`_
* `Development version <http://bitbucket.org/liuyxpp/mpltex/>`_
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mpltex',
    version='0.1',
    license='BSD',
    description='mpltex is a python package for producing publication quality images using matplotlib.',
    author='Yi-Xin Liu',
    author_email='liuyxpp@gmail.com',
    url='https://github.com/liuyxpp/mpltex',
    packages=['mpltex'],
    include_package_data=True,
    zip_safe=False,
    long_description=__doc__,
    platform='linux',
    install_requires=[
        'matplotlib',
        'brewer2mpl',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Education',
    ]
     )

