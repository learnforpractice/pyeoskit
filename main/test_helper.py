load_code = None
run = None

def config_network():
    from uuoskit import config
    config.main_token = 'UUOS'
    config.system_contract = 'uuos'
    config.main_token_contract = 'uuos.token'

try:
    from browser import window, aio
    editor = window.ace.edit("editor")
    editor_abi = window.ace.edit("editor_abi")

    def _load_code():
        abi = editor_abi.getValue()
        src = editor.getValue()
        return src, abi

    def _run(task):
        aio.run(task)

    load_code = _load_code
    run = _run

except Exception as e:
    import os
    import sys
    import asyncio

    def _load_code():
        with open('code.py', 'r') as f:
            code = f.read()
        with open('abi.py', 'r') as f:
            abi = f.read()
        return code, abi

    def _run(future):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(future)

    load_code = _load_code
    run = _run

    sys.path.append('..')

    if os.path.exists('test.wallet'):
        os.remove('test.wallet')

