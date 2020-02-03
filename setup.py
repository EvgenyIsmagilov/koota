from distutils.core import setup
from setuptools import setup, find_packages

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


packages = find_packages(exclude=['tests*'])
requirements = requirements()


import pandas as pd # а оно тут надо?
import numpy as np # а оно тут надо?
import sys # а оно тут надо?

setup(name='koota',
      version='0.1',
      description='Library for data analysis and EDA',
      keywords='python eda data analysis cleaning',
      author='Evgeny Ismagilov',
      author_email='evgenyismagilov@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=packages,
      install_requires=requirements
     )
