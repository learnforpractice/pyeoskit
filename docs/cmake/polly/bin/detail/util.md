# Util

> Auto-generated documentation for [cmake.polly.bin.detail.util](../../../../../cmake/polly/bin/detail/util.py) module.

- [Uuoskit](../../../../README.md#uuoskit-index) / [Modules](../../../../MODULES.md#uuoskit-modules) / `Cmake` / `Polly` / `Bin` / [Detail](index.md#detail) / Util
    - [get_environment_from_batch_command](#get_environment_from_batch_command)

## get_environment_from_batch_command

[[find in source code]](../../../../../cmake/polly/bin/detail/util.py#L4)

```python
def get_environment_from_batch_command(env_cmd, initial=None):
```

Take a command (either a single command or list of arguments)
and return the environment created after running that command.
Note that if the command must be a batch file or .cmd file, or the
changes to the environment will not be captured.

If initial is supplied, it is used as the initial environment passed
to the child process.
