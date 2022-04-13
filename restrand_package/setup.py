from setuptools import setup

setup(name='restrand',
      version='0.0.2',
      description='randomly choose restaurants utilities',
      maintainer='Chuhan Feng',
      maintainer_email='chuhanfe@andrew.cmu.edu',
      license='GPL',
      packages=['restrand'],
      scripts=['restrand/bin/randrest.py'],
      setup_requires=[],
      data_files=['LICENSE'],
      include_package_data=True,
      install_requires=['importlib_resources'],
      long_description='''\
restrand utilities
==============
Handy scripts for the restrand project.
      ''')
