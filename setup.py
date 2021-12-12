from skbuild import setup
from distutils.sysconfig import get_python_lib
import glob

setup(
    name="pyeoskit",
    version="1.0.6",
    description="Python Toolkit for EOS",
    author='learnforpractice',
    license="MIT",
    url="https://github.com/learnforpractice/pyeoskit",
    packages=['pyeoskit'],
    # The extra '/' was *only* added to check that scikit-build can handle it.
    package_dir={'pyeoskit': 'pysrc'},
    package_data={'pyeoskit': [
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
        'httpx>=0.19.0',
        'asn1',
        'ledgerblue>=0.1.41'
    ],
    include_package_data=True
)
