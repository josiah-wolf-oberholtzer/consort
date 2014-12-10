#!/usr/bin/env python

from distutils.core import setup

install_requires = (
    'abjad',
    'ide',
    'supriya',
    )


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