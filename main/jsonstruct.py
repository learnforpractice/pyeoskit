import json
class JsonStruct(object):
    def __init__(self, js):
        if isinstance(js, bytes):
            js = js.decode('utf8')
            js = json.loads(js)
        if isinstance(js, str):
            js = json.loads(js)
        self._dict = js

    def __getattr__(self, attr):
        try:
            ret = self._dict[attr]
            if isinstance(ret, dict):
                ret = JsonStruct(ret)
            return ret
        except KeyError:
            raise AttributeError

    def __str__(self):
        return json.dumps(self, default=lambda x: x._dict, sort_keys=False, indent=4, separators=(',', ': '))

    def __repr__(self):
        return json.dumps(self, default=lambda x: x._dict, sort_keys=False, indent=4, separators=(',', ': '))

    def __getitem__(self, o):
        return self._dict[o]

    def __contains__(self, o):
        return o in self._dict
