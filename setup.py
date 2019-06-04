from skbuild import setup
from distutils.sysconfig import get_python_lib
import glob

setup(
    name="pyeoskit",
    version="0.6.0",
    description="toolkit for pyeos",
    author='The pyeos team',
    license="MIT",
    packages=['pyeoskit'],
    # The extra '/' was *only* added to check that scikit-build can handle it.
    package_dir={'pyeoskit': 'main/'},
    install_requires=[
        'urllib3>=1.21.1',
        'certifi',
        'toolz',
        'funcy',
        'prettytable',
        'requests_unixsocket'
    ],
)
