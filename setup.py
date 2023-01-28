from skbuild import setup
from distutils.sysconfig import get_python_lib
import platform

data = [
        'data/*',
        'contracts/eosio.bios/*',
        'contracts/eosio.msig/*',
        'contracts/eosio.system/*',
        'contracts/eosio.token/*',
        'contracts/eosio.wrap/*',
        'contracts/micropython/*',
        'test_template.py',
]

if platform.system() == 'Windows':
    data.append("pyeoskit.dll")

setup(
    name="pyeoskit",
    version="1.1.10",
    description="Python Toolkit for EOS",
    author='learnforpractice',
    license="MIT",
    url="https://github.com/learnforpractice/pyeoskit",
    packages=['pyeoskit'],
    # The extra '/' was *only* added to check that scikit-build can handle it.
    package_dir={'pyeoskit': 'pysrc'},
    package_data={'pyeoskit': data
    },
    install_requires=[
        'requests_unixsocket>=0.2.0',
        'httpx>=0.19.0',
        'base58>=2.1.1',
        'asn1>=2.4.2',
        'ledgerblue>=0.1.41'
    ],
    include_package_data=True
)