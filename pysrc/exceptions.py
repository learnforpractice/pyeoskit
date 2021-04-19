import json

class NoResponse(BaseException):
    pass

class WalletException(BaseException):
    pass

class ChainException(Exception):
    def __init__(self, response, status_code=0):
        super().__init__(response)
        self.status_code = status_code
        self.response = response
        try:
            self.json = json.loads(response)
        except:
            self.json = None

    def __str__(self):
        if isinstance(self.json, dict):
            return json.dumps(self.json, indent=' ')
        return self.response
