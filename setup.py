from skbuild import setup
from distutils.sysconfig import get_python_lib
import glob

setup(
    name="uuoskit",
    version="0.8.3",
    description="Python Toolkit for EOSIO",
    author='The UUOSIO Team',
    license="MIT",
    packages=['uuoskit'],
    # The extra '/' was *only* added to check that scikit-build can handle it.
    package_dir={'uuoskit': 'main/'},
    install_requires=[
        'urllib3>=1.21.1',
        'certifi',
        'toolz',
        'funcy',
        'prettytable',
        'requests_unixsocket'
    ],
)
