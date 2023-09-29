
class Error(Exception):
    code: int
    msg: str

class ServerError(Error):
    code = 500
    msg = 'Unexpected error'

class ClientError(Error):
    code = 400

class BadRequest(ClientError):
    code = 400

class UnautorizedException(ClientError):
    code = 401

class NotFoundException(ClientError):
    code = 404
    msg = 'Not found.'
