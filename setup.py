from skbuild import setup
from distutils.sysconfig import get_python_lib
import glob

setup(
    name="uuoskit",
    version="1.0.1",
    description="Python Toolkit for EOSIO",
    author='The UUOSIO Team',
    license="MIT",
    url="https://github.com/uuosio/uuoskit",
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
        'certifi>=2021.10.8',
        'toolz>=0.11.1',
        'funcy>=1.16',
        'prettytable>=2.2.1',
        'requests_unixsocket>=0.2.0',
        'httpx>=0.19.0'
    ],
    include_package_data=True
)
