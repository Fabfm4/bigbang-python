from setuptools import setup
from bigbang import __version__ as version


setup(
    name='bigbang',
    version=version,
    description='Library to create development environment',
    author='Sergio Fabian Flores Mendoza',
    author_email='favian.flone92@gmail.com',
    url='https://github.com/Fabfm4/bigbang-python',
    license='MIT',
    packages=["bigbang"],
    install_requires=[
        'markdown',
    ],
    entry_points={
        'console_scripts': ['bigbang=bigbang.commands:main'],
    },
    include_package_data=True,
    zip_safe=False,
)
