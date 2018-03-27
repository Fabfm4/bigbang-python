from setuptools import find_packages, setup
from bigbang import __version__ as version
setup(
    name='bigbang',
    packages=find_packages(),
    version=version,
    description='Library to create development environment',
    author='Sergio Fabian Flores Mendoza',
    author_email='favian.flone92@gmail.com',
    url='https://github.com/Fabfm4/bigbang-python',
    download_url='https://github.com/Fabfm4/bigbang-python/archive/{0}.tar.gz'.format(version),
    keywords=['python', 'django', 'docker'],
    scripts=['bigbang/bin/bigbang-py'],
    entry_points={
        'console_scripts': [
            'bigbang-py=bigbang.commands:main',
        ]
    },
    classifiers=[],
)
