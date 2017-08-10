#!/usr/bin/env python
import os
import setuptools


install_requires = [
    'abjad[accelerated,development]==2.21',
    ]


version_file_path = os.path.join(
    os.path.dirname(__file__),
    'consort',
    '_version.py'
    )
with open(version_file_path, 'r') as file_pointer:
    file_contents_string = file_pointer.read()
local_dict = {}
exec(file_contents_string, None, local_dict)
__version__ = local_dict['__version__']


def main():
    setuptools.setup(
        author='Josiah Wolf Oberholtzer',
        author_email='josiah.oberholtzer@gmail.com',
        description='High-level tools for formalized score control in Abjad.',
        include_package_data=True,
        install_requires=install_requires,
        name='consort',
        packages=('consort',),
        url='https://github.com/josiah-wolf-oberholtzer/consort',
        version=__version__,
        zip_safe=False,
        )


if __name__ == '__main__':
    main()
