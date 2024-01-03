from flask import make_response, jsonify
from werkzeug.exceptions import HTTPException

class PGAPIException(HTTPException):
    def __init__(self, message, errors=None):
        self.message = message
        self.errors = errors
        super().__init__(description=message)

    def get_response(self):
        payload = {"message": self.message}
        if self.errors:
            payload["errors"] = self.errors
        return make_response(jsonify(payload), self.code)