"""
setup.py
========

:copyright: (c) 2014 by Yi-Xin Liu
:license: BSD, see LICENSE.txt for more details.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import sys
cwd = os.path.dirname(os.path.abspath(__file__))

# Read __version__ from _version.py and add it into the current variable space.
exec(open('mpltex/_version.py').read())

setup(
    name='mpltex',
    version=__version__,
    license='BSD',
    description='mpltex is a python package for creating publication-quality plots using matplotlib.',
    author='Yi-Xin Liu',
    author_email='liuyxpp@gmail.com',
    url='https://github.com/liuyxpp/mpltex',
    packages=['mpltex'],
    include_package_data=True,
    zip_safe=False,
    long_description=open(os.path.join(cwd, 'README.rst')).read(),
    install_requires=[
        'matplotlib',
        'palettable',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Education', ],
)
