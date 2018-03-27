from distutils.core import setup
from bigbang import __version__ as version
setup(
    name='bigbang',
    packages=['bigbang'],
    version=version,
    description='Library to create development environment',
    author='Sergio Fabian Flores Mendoza',
    author_email='favian.flone92@gmail.com',
    url='https://github.com/Fabfm4/bigbang-python',
    download_url='https://github.com/Fabfm4/bigbang-python/archive/{0}.tar.gz'.format(version),
    keywords=['python', 'django', 'docker'],
    scripts=['bin/bigbang-py'],
    entry_points={'console_scripts': [
        'bigbang-py = bigbang.core.management:execute_from_command_line',
    ]},
    classifiers=[],
)
