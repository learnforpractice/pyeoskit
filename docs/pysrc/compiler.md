# Compiler

> Auto-generated documentation for [pysrc.compiler](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / Compiler
    - [cpp_compiler](#cpp_compiler)
        - [cpp_compiler().compile_cpp_file](#cpp_compilercompile_cpp_file)
    - [compile_cpp_file](#compile_cpp_file)
    - [compile_cpp_src](#compile_cpp_src)
    - [find_eosio_cdt_path](#find_eosio_cdt_path)
    - [publish_contract](#publish_contract)
    - [publish_cpp_contract](#publish_cpp_contract)
    - [publish_cpp_contract_from_file](#publish_cpp_contract_from_file)
    - [publish_py_contract](#publish_py_contract)
    - [run_test_code](#run_test_code)
    - [set_code](#set_code)

## cpp_compiler

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L49)

```python
class cpp_compiler(object):
    def __init__(cpp_file, includes=[], entry='apply'):
```

### cpp_compiler().compile_cpp_file

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L58)

```python
def compile_cpp_file(opt='O3'):
```

## compile_cpp_file

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L146)

```python
def compile_cpp_file(src_path, includes=[], entry='apply', opt='O3'):
```

## compile_cpp_src

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L150)

```python
def compile_cpp_src(account_name, code, includes=[], entry='apply', opt='O3'):
```

## find_eosio_cdt_path

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L41)

```python
def find_eosio_cdt_path():
```

## publish_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L203)

```python
def publish_contract(
    account_name,
    code,
    abi,
    vm_type=1,
    includes=[],
    entry='apply',
):
```

## publish_cpp_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L181)

```python
def publish_cpp_contract(
    account_name,
    code,
    abi='',
    includes=[],
    entry='apply',
    opt='O3',
    vm_type=0,
):
```

## publish_cpp_contract_from_file

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L166)

```python
def publish_cpp_contract_from_file(
    account_name,
    file_name,
    includes=[],
    entry='apply',
):
```

## publish_py_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L192)

```python
def publish_py_contract(
    account_name,
    code,
    abi,
    vm_type=1,
    includes=[],
    entry='apply',
):
```

## run_test_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L14)

```python
def run_test_code(code, abi='', account_name='helloworld11'):
```

## set_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/compiler.py#L22)

```python
def set_code(account_name, code):
```
