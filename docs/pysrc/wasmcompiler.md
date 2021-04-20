# Wasmcompiler

> Auto-generated documentation for [pysrc.wasmcompiler](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wasmcompiler.py) module.

- [Uuoskit](../README.md#uuoskit-index) / [Modules](../MODULES.md#uuoskit-modules) / [Pysrc](index.md#pysrc) / Wasmcompiler
    - [cpp_compiler](#cpp_compiler)
        - [cpp_compiler().compile_cpp_file](#cpp_compilercompile_cpp_file)
    - [compile_cpp_file](#compile_cpp_file)
    - [compile_cpp_src](#compile_cpp_src)
    - [compile_with_eosio_cpp](#compile_with_eosio_cpp)
    - [find_eosio_cdt_path](#find_eosio_cdt_path)

## cpp_compiler

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wasmcompiler.py#L21)

```python
class cpp_compiler(object):
    def __init__(cpp_file, includes=[], entry='apply'):
```

### cpp_compiler().compile_cpp_file

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wasmcompiler.py#L30)

```python
def compile_cpp_file(opt='O3'):
```

## compile_cpp_file

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wasmcompiler.py#L120)

```python
def compile_cpp_file(src_path, includes=[], entry='apply', opt='O3'):
```

## compile_cpp_src

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wasmcompiler.py#L124)

```python
def compile_cpp_src(
    account_name,
    code,
    includes=[],
    entry='apply',
    opt='O3',
    force=False,
):
```

## compile_with_eosio_cpp

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wasmcompiler.py#L139)

```python
def compile_with_eosio_cpp(contract_name, code, options=''):
```

contract_name must match the class name in code, otherwise there will no abi generated

## find_eosio_cdt_path

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wasmcompiler.py#L13)

```python
def find_eosio_cdt_path():
```
