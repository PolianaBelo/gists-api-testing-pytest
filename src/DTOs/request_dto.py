class RequestDTO:

    def __init__(self, body=None, parameters=None):
        self._body = body
        self._headers = {"Accept": "application/vnd.github.v3+json"}
        self._parameters = parameters

    def auth_token(self):
        return self._headers["Authorization"]

    def set_auth_header(self, auth_token):
        self._headers["Authorization"] = auth_token
