# Wasmcompiler

> Auto-generated documentation for [pysrc.wasmcompiler](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / Wasmcompiler
    - [cpp_compiler](#cpp_compiler)
        - [cpp_compiler().compile_cpp_file](#cpp_compilercompile_cpp_file)
    - [go_compiler](#go_compiler)
        - [go_compiler().compile_go_file](#go_compilercompile_go_file)
    - [compile_cpp_file](#compile_cpp_file)
    - [compile_cpp_src](#compile_cpp_src)
    - [compile_go_file](#compile_go_file)
    - [compile_go_src](#compile_go_src)
    - [compile_with_eosio_cpp](#compile_with_eosio_cpp)
    - [find_eosio_cdt_path](#find_eosio_cdt_path)

## cpp_compiler

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L20)

```python
class cpp_compiler(object):
    def __init__(cpp_file, includes=[], entry='apply'):
```

### cpp_compiler().compile_cpp_file

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L29)

```python
def compile_cpp_file(opt='O3'):
```

## go_compiler

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L179)

```python
class go_compiler(object):
    def __init__(go_file, includes=[], entry='apply'):
```

### go_compiler().compile_go_file

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L188)

```python
def compile_go_file(opt='O3', replace=''):
```

## compile_cpp_file

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L130)

```python
def compile_cpp_file(src_path, includes=[], entry='apply', opt='O3'):
```

## compile_cpp_src

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L134)

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

## compile_go_file

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L233)

```python
def compile_go_file(
    src_path,
    includes=[],
    entry='apply',
    opt='O3',
    replace='',
):
```

## compile_go_src

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L237)

```python
def compile_go_src(
    account_name,
    code,
    includes=[],
    entry='apply',
    opt='O3',
    force=False,
    replace='',
):
```

## compile_with_eosio_cpp

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L145)

```python
def compile_with_eosio_cpp(contract_name, code, options=''):
```

contract_name must match the class name in code, otherwise there will no abi generated

## find_eosio_cdt_path

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wasmcompiler.py#L12)

```python
def find_eosio_cdt_path():
```
