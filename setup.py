import os
from setuptools import setup, find_packages
import sys
setup(
    name='snap-webkit-how',
    version='1.0.0',
    url='https://github.com/blah/snap-webkit-how',
    author='Blah',
    author_email='blah@gmail.com',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'gitm=main:run',
        ],
    },    
)