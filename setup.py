from skbuild import setup
from distutils.sysconfig import get_python_lib
import glob

setup(
    name="uuoskit",
    version="1.0.0",
    description="Python Toolkit for EOSIO",
    author='The UUOSIO Team',
    license="MIT",
    packages=['uuoskit'],
    # The extra '/' was *only* added to check that scikit-build can handle it.
    package_dir={'uuoskit': 'pysrc'},
    package_data={'uuoskit': [
        'data/*',
        'contracts/eosio.bios/*',
        'contracts/eosio.msig/*',
        'contracts/eosio.system/*',
        'contracts/eosio.token/*',
        'contracts/eosio.wrap/*',
        'contracts/micropython/*',
        'test_template.py',
        ]
    },

    install_requires=[
        'urllib3>=1.21.1',
        'certifi',
        'toolz',
        'funcy',
        'prettytable',
        'requests_unixsocket',
        'httpx'
    ],
    include_package_data=True
)
