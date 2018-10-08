class EosdNoResponse(BaseException):
    pass


class HttpAPIError(Exception):
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
        self.response = response
