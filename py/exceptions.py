import json

class NoResponse(BaseException):
    pass

class ChainException(Exception):
    def __init__(self, status_code, response):
        if not status_code in [200, 202]:
            msg = 'API returned status code: {0} {1}'.format(status_code, response)
        elif not response:
            msg = 'API returned without response body.'
        else:
            msg = 'Invalid API response (%s): %s' % (
                status_code, response)
        super().__init__(msg)
        self.status_code = status_code
        try:
            self.json = json.loads(response)
        except:
            self.json = response

    def __str__(self):
        if isinstance(self.json, dict):
            return json.dumps(self.json, indent=' ')
        return str(self.json)
