import os
import sys
import time
import subprocess
import hashlib

version = sys.argv[1]
files = [
 f'pyeoskit-{version}-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl',
 f'pyeoskit-{version}-cp310-cp310-win_amd64.whl',
 f'pyeoskit-{version}-cp310-cp310-macosx_10_15_x86_64.whl',
 f'pyeoskit-{version}-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl',
 f'pyeoskit-{version}-cp39-cp39-win_amd64.whl',
 f'pyeoskit-{version}-cp39-cp39-macosx_10_15_x86_64.whl',
 f'pyeoskit-{version}-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl',
 f'pyeoskit-{version}-cp38-cp38-win_amd64.whl',
 f'pyeoskit-{version}-cp38-cp38-macosx_10_15_x86_64.whl',
 f'pyeoskit-{version}-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl',
 f'pyeoskit-{version}-cp37-cp37m-win_amd64.whl',
 f'pyeoskit-{version}-cp37-cp37m-macosx_10_15_x86_64.whl',
]

url = f'https://github.com/learnforpractice/pyeoskit/releases/download/v{version}/'
for f in files:
    count = 60*60/10
    while True:
        print('Downloading {}'.format(f))
        subprocess.call(['wget', url + f])
        if os.path.exists(f):
            break
        time.sleep(10)
        count -= 1
        if count <= 0:
            break

out = open('checksum.txt', 'w')
out.write('file\t SHA256 Checksum\n')
for file in files:
    with open(file, 'rb') as f:
        data = f.read()
        h = hashlib.sha256()
        h.update(data)
        out.write(file)
        out.write('\t')
        out.write(h.hexdigest())
        out.write('\n')
out.close()
