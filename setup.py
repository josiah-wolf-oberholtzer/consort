#!/usr/bin/env python

import sys
from distutils.core import setup
from distutils.version import StrictVersion

install_requires = [
    'abjad[development]',
    ]

version = '.'.join(str(x) for x in sys.version_info[:3])
if StrictVersion(version) < StrictVersion('3.3.0'):
    install_requires.append('funcsigs')


def main():
    setup(
        author='Josiah Wolf Oberholtzer',
        author_email='josiah.oberholtzer@gmail.com',
        install_requires=install_requires,
        name='consort',
        packages=('consort',),
        url='https://github.com/josiah-wolf-oberholtzer/consort',
        version='0.1',
        zip_safe=False,
        )


if __name__ == '__main__':
    main()