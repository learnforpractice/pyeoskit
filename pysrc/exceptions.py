import json

class NoResponse(Exception):
    pass

class WalletException(Exception):
    pass

class ChainException(Exception):
    def __init__(self, response, status_code=0):
        super().__init__(str(response))
        self.status_code = status_code
        self.response = str(response)
        if isinstance(response, dict):
            self.json = response
        else:
            try:
                self.json = json.loads(response)
            except:
                self.json = None

    def __str__(self):
        try:
            if isinstance(self.json, dict):
                return json.dumps(self.json, indent=' ')
            return self.response
        except Exception as e:
            print(e)

    def __repr__(self):
        if isinstance(self.json, dict):
            return json.dumps(self.json, indent=' ')
        return self.response
