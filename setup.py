from distutils.core import setup
from setuptools import setup, find_packages

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list



requirements = requirements()

PACKAGE = ""
NAME = "koota"
DESCRIPTION = "Library for data analysis and EDA"
KEYWORDS = "python eda data analysis cleaning"
AUTHOR = "Evgeny Ismagilov"
AUTHOR_EMAIL = "evgenyismagilov@gmail.com"
URL = "https://github.com/EvgenyIsmagilov/koota"
VERSION = 0.0.1 #__import__(PACKAGE).__version__
 = ['mod1', 'pkg.mod2']
packages = ['koota'] #find_packages()

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      keywords=KEYWORDS,
      long_description=read("README.md"),
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      packages=packages,
      install_requires=requirements,
      py_modules = PY_MODULES
      #, download_url=''
      #, license=''
     )
