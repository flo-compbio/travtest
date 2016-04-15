from __future__ import print_function

import sys
import os
import io

from setuptools import setup, find_packages, Extension
from os import path

root = 'travtest'
description = 'Travis CI test package'
version = '0.1.0'

install_requires = [
    'future >= 0.15.2, < 1',
    'six >= 1.10.0, < 2',
]

# do not require installation if built by ReadTheDocs
# (we mock these modules in docs/source/conf.py)
if 'READTHEDOCS' not in os.environ or \
        os.environ['READTHEDOCS'] != 'True':
    try:
        from Cython.Distutils import build_ext # Cython is required
    except ImportError:
        print ('You must installCython before installing XL-mHG! '
               'Try `pip install cython`.')
        sys.exit(1)

    install_requires.extend([
        'cython >= 0.23.4, < 1',
    ])

ext_modules = []

ext_modules.append(
    Extension(
        root + '.' + 'test_cython',
        sources=[root + os.sep + 'test_cython.pyx'],
        include_dirs=[]
    )
)

here = path.abspath(path.dirname(__file__))

long_description = ''
with io.open(path.join(here, 'README.rst'), encoding='UTF-8') as fh:
    long_description = fh.read()

# extensions
setup(
    name='travtest',

    version=version,

    description=description,
    long_description=long_description,

    url='https://github.com/flo-compbio/travtest',

    author='Florian Wagner',
    author_email='florian.wagner@duke.edu',

    license='GPLv3',

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Cython',
    ],

    keywords=('test'),

    #packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    packages=find_packages(exclude=['docs', 'tests*']),

    # extensions
    ext_modules=ext_modules,
    cmdclass={
        'build_ext': build_ext,
    },

    #libraries = [],

    install_requires=install_requires,

    tests_require=[
        'pytest >= 2.8.5, < 3',
    ],

    # development dependencies
    #extras_require={},

    # data
    #package_data={}

    # data outside package
    #data_files=[],

    # executable scripts
    entry_points={
        #'console_scripts': []
    },
)
