from setuptools import setup, find_packages

setup(name='koota',
    version='0.0.1',
    description='beta library',
    author='Jenya',
    url='https://github.com/EvgenyIsmagilov/koota',
    packages=['koota'],
    # important
    license='MIT', 
    download_url = 'https://github.com/EvgenyIsmagilov/koota/archive/master.zip',
    keywords = ['EDA', 'DATA', 'CLEANING'],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Data Analysts',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
          ]
      #,install_requires=['unidecode']
     )
