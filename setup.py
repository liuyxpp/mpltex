'''
mpltex
======

**mpltex** is a python package for generating suitable Matplotlib configurations for publication at various publishers. 

Quickstart
----------

1. Install
^^^^^^^^^^

::

    $ easy_install mpltex

or

::

    $ tar -xvf mpltex-xxx.tar.gz
    $ cd mpltex-xxx
    $ python setup.py install

Required packages:

* `matplotlib`

2. Usage
^^^^^^^^

Add a line to your plotting script

::
   import mpltex.acs 

Current available publisher formats

* American Chemical Society

Ask for Help
------------

* You can directly contact me at liuyxpp@gmail.com.
* You can join the mailinglist by sending an email to mpltex@librelist.com 
  and replying to the confirmation mail. 
  To unsubscribe, send a mail to chebpy-unsubscribe@librelist.com 
  and reply to the confirmation mail.

Contribute
----------

Please do not hesitate to submit your own configurations.
I will add them to the package.

Links
-----

* `Documentation <http://pypi.python.org/pypi/mpltex>`_
* `Website <http://ngpy.org>`_
* `Development version <http://bitbucket.org/liuyxpp/mpltex/>`_

'''
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='mpltex',
    version='0.1',
    license='BSD',
    description='mpltex is a python package which providds an easy way to change matplotlib configurations for specific publications.',
    author='Yi-Xin Liu',
    author_email='liuyxpp@gmail.com',
    url='https://bitbucket.org/liuyxpp/mpltex',
    packages=['mpltex'],
    include_package_data=True,
    zip_safe=False,
    long_description=__doc__,
    platform='linux',
    install_requires=[
        'matplotlib',
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

