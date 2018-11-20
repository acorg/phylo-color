#!/usr/bin/env python

from setuptools import setup


# Modified from http://stackoverflow.com/questions/2058802/
# how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package
def version():
    import os
    import re

    init = os.path.join('py3seq', '__init__.py')
    with open(init) as fp:
        initData = fp.read()
    match = re.search(r"^__version__ = ['\"]([^'\"]+)['\"]",
                      initData, re.M)
    if match:
        return match.group(1)
    else:
        raise RuntimeError('Unable to find version string in %r.' % init)


setup(name='phylo-color',
      version=version(),
      include_package_data=False,
      url='https://github.com/acorg/phylo-color',
      download_url='https://github.com/acorg/phylo-color',
      author='Terry Jones',
      author_email='tcj25@cam.ac.uk',
      keywords=['phylogenetic tree color nexml nexus newick'],
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='MIT',
      scripts=['phylo-color.py'],
      description=('Color the nodes of a phylogenetic tree using regular '
                   'expressions to match taxa names.'),
      install_requires=[
          'dendropy',
      ],
      extras_require={
        'dev': [
            'flake8',
            'pytest',
        ]
      })
