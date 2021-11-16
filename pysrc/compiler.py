import os
import sys
import shutil
import hashlib
import marshal
import subprocess
from pyeoskit import eosapi, wallet
from pyeoskit import config

def run_test_code(code, abi='', account_name='helloworld11'):
    publish_contract(account_name, code, abi)
    try:
        r = eosapi.push_action(account_name, 'sayhello', b'hello,world', {account_name:'active'})
        print(r['processed']['action_traces'][0]['console'])
    except Exception as e:
        print(e)

def set_code(account_name, code):
    m = hashlib.sha256()
    code = compile(code, "contract", 'exec')
    code = marshal.dumps(code)
    m.update(code)
    code_hash = m.hexdigest()
    r = eosapi.get_code(account_name)
    if code_hash == r['code_hash']:
        return

    setcode = {"account":account_name,
               "vmtype": 1,
               "vmversion":0,
               "code":code.hex()
               }
    eosapi.push_action(config.system_contract, 'setcode', setcode, {account_name:'active'})
    
    return True

def find_eosio_cdt_path():
    eosio_cpp = shutil.which('eosio-cpp')
    if not eosio_cpp:
        raise "eosio.cdt not installed, please refer to https://github.com/eosio/eosio.cdt for an installation guide"
    eosio_cpp = os.path.realpath(eosio_cpp)
    eosio_cpp = os.path.dirname(eosio_cpp)
    return os.path.dirname(eosio_cpp)

class cpp_compiler(object):

    def __init__(self, cpp_file, includes = [], entry='apply'):
        self.cpp_file = cpp_file
        self.includes = includes
        self.entry = entry
        if not cpp_file.endswith('.cpp'):
            raise 'Not a cpp file'

    def compile_cpp_file(self, opt='O3'):
        tmp_path = self.cpp_file[:-4]
        #%system rm test.obj test.wasm
        #%system eosio-cpp -I/usr/local/Cellar/eosio.cdt/1.6.1/opt/eosio.cdt/include/eosiolib/capi -I/usr/local/Cellar/eosio.cdt/1.6.1/opt/eosio.cdt/include/eosiolib/core -O3 -contract test -o test.obj -c test.cpp
        #%system eosio-ld test.obj -o test.wasm
        #%ls
        if sys.platform == 'darwin':
            dl_sufix = 'dylib'
        else:
            dl_sufix = 'so'
        eosio_cdt_path = find_eosio_cdt_path()
        clang_7_args = [f'{eosio_cdt_path}/bin/clang-7',
        '-o',
        f'{tmp_path}.obj',
        f'{tmp_path}.cpp',
        '--target=wasm32',
        '-ffreestanding',
        '-nostdlib',
        '-fno-builtin',
        '-fno-threadsafe-statics',
        '-fno-exceptions',
        '-fno-rtti',
        '-fmodules-ts',
        '-DBOOST_DISABLE_ASSERTS',
        '-DBOOST_EXCEPTION_DISABLE',
        '-Xclang',
        '-load',
        '-Xclang',
        f'{eosio_cdt_path}/bin/LLVMEosioApply.{dl_sufix}',
        f'-fplugin={eosio_cdt_path}/bin/eosio_plugin.{dl_sufix}',
        '-mllvm',
        '-use-cfl-aa-in-codegen=both',
        f'-I{eosio_cdt_path}/bin/../include/libcxx',
        f'-I{eosio_cdt_path}/bin/../include/libc',
        f'-I{eosio_cdt_path}/bin/../include',
        f'--sysroot={eosio_cdt_path}/bin/../',
        f'-I{eosio_cdt_path}/bin/../include/eosiolib/core',
        f'-I{eosio_cdt_path}/bin/../include/eosiolib/contracts',
        '-c',
        f'-I{eosio_cdt_path}/include/eosiolib/capi',
        f'-I{eosio_cdt_path}/include/eosiolib/core',
        f'-{opt}',
        '--std=c++17',
        ]
        for include in self.includes:
            clang_7_args.append(f"-I{include}")

        wasm_ld_args = [f'{eosio_cdt_path}/bin/wasm-ld',
        '--gc-sections',
        '--strip-all',
        '-zstack-size=8192',
        '--merge-data-segments',
        '-e', f'{self.entry}',
        '--only-export', f'{self.entry}:function',
        '-lc++',
        '-lc',
        '-leosio',
        '-leosio_dsm',
        '-mllvm',
        '-use-cfl-aa-in-codegen=both',
        f'{tmp_path}.obj',
        f'-L{eosio_cdt_path}/bin/../lib',
        '-stack-first',
        '--lto-O3',
        '-o',
        f'{tmp_path}.wasm',
        f'--allow-undefined-file={eosio_cdt_path}/bin/../eosio.imports']

        eosio_pp = [
            f'{eosio_cdt_path}/bin/eosio-pp',
            '-o',
            f'{tmp_path}.wasm',
            f'{tmp_path}.wasm',
        ]

        try:
            ret = subprocess.check_output(clang_7_args, stderr=subprocess.STDOUT)
            print(ret.decode('utf8'))
            ret = subprocess.check_output(wasm_ld_args, stderr=subprocess.STDOUT)
            print(ret.decode('utf8'))
            ret = subprocess.check_output(eosio_pp, stderr=subprocess.STDOUT)
            print(ret.decode('utf8'))
        except subprocess.CalledProcessError as e:
            print("error (code {}):".format(e.returncode))
            print(e.output.decode('utf8'))
            return None
        return open(f'{tmp_path}.wasm', 'rb').read()

def compile_cpp_file(src_path, includes=[], entry='apply', opt='O3'):
    compiler = cpp_compiler(src_path, includes, entry)
    return compiler.compile_cpp_file(opt)

def compile_cpp_src(account_name, code, includes = [], entry='apply', opt='O3'):
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    src_path = os.path.join('tmp', account_name+'.cpp')
    if os.path.exists(src_path):
        old_code = open(src_path).read()
        if old_code == code:
            tmp_path = src_path[:-4]
            wasm_file = f'{tmp_path}.wasm'
            if os.path.exists(f'{tmp_path}.cpp') and os.path.exists(wasm_file):
                if os.path.getmtime(f'{tmp_path}.cpp') <= os.path.getmtime(wasm_file):
                    return open(wasm_file, 'rb').read()
    with open(src_path, 'w') as f:
        f.write(code)
    return compile_cpp_file(src_path, includes, entry, opt=opt)

def publish_cpp_contract_from_file(account_name, file_name, includes = [], entry='apply'):
    code = compile_cpp_file(file_name, includes, entry=entry)
    assert code
    m = hashlib.sha256()
    m.update(code)
    code_hash = m.hexdigest()

    r = eosapi.get_code(account_name)
    if code_hash != r['code_hash']:
        print('update contract')
        abi = open(f'{file_name}.abi', 'r').read()
        r = eosapi.set_contract(account_name, code, abi, 0)
    return True
#print(find_include_path())

def publish_cpp_contract(account_name, code, abi='', includes = [], entry='apply', opt='O3',vm_type=0):
    code = compile_cpp_src(account_name, code, includes, entry=entry, opt=opt)
    code = open(f'tmp/{account_name}.wasm', 'rb').read()
    m = hashlib.sha256()
    m.update(code)
    code_hash = m.hexdigest()
    r = eosapi.get_code(account_name)
    if code_hash != r['code_hash']:
        r = eosapi.set_contract(account_name, code, abi, vm_type)
    return True

def publish_py_contract(account_name, code, abi, vm_type=1, includes = [], entry='apply'):
    m = hashlib.sha256()
    code = compile(code, "contract", 'exec')
    code = marshal.dumps(code)
    m.update(code)
    code_hash = m.hexdigest()
    r = eosapi.get_code(account_name)
    if code_hash != r['code_hash']:
        eosapi.set_contract(account_name, code, abi, 1)
    return True

def publish_contract(account_name, code, abi, vm_type=1, includes = [], entry='apply'):
    if vm_type == 1:
        return publish_py_contract(account_name, code, abi, 1)
    else:
        return publish_cpp_contract(account_name, code, abi, includes, entry)

