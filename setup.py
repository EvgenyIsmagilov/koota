from setuptools import setup, find_packages

def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())
    return requirements_list

requirements = requirements()

setup(name='koota',
    version='0.0.2',
    description='Library for data analysis and EDA',
    long_description_content_type='text/markdown',
    # long_description=open('README.md').read(),
    author='Evgeny Ismagilov',
    author_email="evgenyismagilov@gmail.com",
    url='https://github.com/EvgenyIsmagilov/koota',
    packages=find_packages(exclude=['tests']),
    #long_description=read("README.md"),   # какая то проблема
    # important
    install_requires=requirements,
    license='MIT', 
    download_url = 'https://github.com/EvgenyIsmagilov/koota/archive/refs/tags/0.0.2.tar.gz',
    keywords = ['EDA', 'DATA', 'CLEANING', 'analysis', 'koota'],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        # 'Intended Audience :: Data Analysts',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
          ]
      #,install_requires=['unidecode']
     )
