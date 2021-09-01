pushd dist
python3 -m pip uninstall uuoskit -y;python3 -m pip install ./uuoskit-*.whl
popd
