# Log

> Auto-generated documentation for [pysrc.log](https://github.com/uuosio/UUOSKit/blob/master/pysrc/log.py) module.

- [Uuoskit](../README.md#uuoskit-index) / [Modules](../MODULES.md#uuoskit-modules) / [Pysrc](index.md#pysrc) / Log
    - [CustomFormatter](#customformatter)
        - [CustomFormatter().format](#customformatterformat)
    - [get_logger](#get_logger)

#### Attributes

- `formatter` - '%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s': `CustomFormatter()`

## CustomFormatter

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/log.py#L4)

```python
class CustomFormatter(logging.Formatter):
```

Logging Formatter to add colors and count warning / errors

#### Attributes

- `FORMATS` - "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)": `{logging.DEBUG: grey + fmt + reset, logging.INF...`

### CustomFormatter().format

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/log.py#L22)

```python
def format(record):
```

## get_logger

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/log.py#L35)

```python
def get_logger(name):
```
