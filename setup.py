from distutils.core import setup

import pandas as pd # а оно тут надо?
import numpy as np # а оно тут надо?
import sys # а оно тут надо?

setup(name='koota',
      version='0.1',
      description='Library for data analysis and EDA',
      author='Evgeny Ismagilov',
      author_email='evgenyismagilov@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command'],
     )
