import os
import sys
from setuptools import setup, find_packages

root_pkg_name = 'harmonia'

here = os.path.abspath(os.path.dirname(__file__))

version_path = os.path.join(here, root_pkg_name, '_version.py')
with open(version_path, 'r') as f:
    # puts __version__ in scope.
    exec(f.read())

install_requires = [ 'click' ]

setup(name=root_pkg_name,
    version=__version__,
    description="Find musical scales and modes from a given progression of chords.",
    long_description='',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Sound/Audio :: Analysis'
    ],
    keywords='music mode chord progression',
    author='Riley McDowell',
    author_email='riley.mcdowell.0@gmail.com',
    url='www.mcdowell.data',
    license='MIT',
    packages=find_packages('harmonia'),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['harmonia=harmonia.cli:cli']
    }
)
