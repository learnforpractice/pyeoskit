pushd dist
python3 -m pip uninstall pyeoskit -y;python3 -m pip install ./pyeoskit-*.whl
popd
