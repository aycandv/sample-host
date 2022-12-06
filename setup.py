# create a simple package setup script
# this is a simple example of a setup script for a package

from distutils.core import setup

setup(
    name='samplehost',
    version='1.0',
    description='A simple package',
    author='Sample Author',
    author_email='a',
    url='http://www.python.org/sigs/distutils-sig/',
    packages=['samplehost'],
)
