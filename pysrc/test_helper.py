load_code = None
run = None

test_account1 = 'ceyelqpjeeia'
test_account2 = 'ebvjmdibybgq'

def config_network():
    from pyeoskit import config

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
    from pyeoskit import wallet

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
    wallet.create('test')

def print_console(r):
    print('\n===================== CONSOLE OUTPUT BEGIN =====================\n')
    print(r['processed']['action_traces'][0]['console'])
    print('\n===================== CONSOLE OUTPUT END =====================\n')

def run_test():
    global test_account1
    global test_account2
    test_account1 = 'ceyelqpjeeia'
    test_account2 = 'ebvjmdibybgq'

    import os
    import sys
    import asyncio
    import argparse
    from pyeoskit import config
    config.setup_eos_test_network()
#    config.setup_uuos_test_network()

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--test-dir', type=str, default='tests/test_helloworld', help='test directory')
    args = parser.parse_args()
    os.chdir(args.test_dir)

    with open('test.py', 'r') as f:
        src = f.read()
        a = compile(src, "test.py", 'exec')
        m = type(sys)('test')
        print('Test is running, please wait...')
        exec(a, m.__dict__)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(m.run_test())
