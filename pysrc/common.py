import json
def check_result(r):
    r = json.loads(r)
    if 'error' in r:
        raise Exception(r['error'])
    return r['data']
