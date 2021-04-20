# Toolchain Table

> Auto-generated documentation for [cmake.polly.bin.detail.toolchain_table](../../../../../cmake/polly/bin/detail/toolchain_table.py) module.

- [Uuoskit](../../../../README.md#uuoskit-index) / [Modules](../../../../MODULES.md#uuoskit-modules) / `Cmake` / `Polly` / `Bin` / [Detail](index.md#detail) / Toolchain Table
    - [Toolchain](#toolchain)
        - [Toolchain().verify](#toolchainverify)
    - [get_by_name](#get_by_name)

## Toolchain

[[find in source code]](../../../../../cmake/polly/bin/detail/toolchain_table.py#L10)

```python
class Toolchain():
    def __init__(
        name,
        generator,
        arch='',
        vs_version='',
        ios_version='',
        osx_version='',
        xp=False,
        nocodesign=False,
    ):
```

### Toolchain().verify

[[find in source code]](../../../../../cmake/polly/bin/detail/toolchain_table.py#L38)

```python
def verify():
```

## get_by_name

[[find in source code]](../../../../../cmake/polly/bin/detail/toolchain_table.py#L618)

```python
def get_by_name(name):
```
