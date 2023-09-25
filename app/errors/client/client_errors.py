from errors.exceptions import Error

class ClientError(Error):
    code = 400

class BadRequest(ClientError):
    code = 400

class UnautorizedException(ClientError):
    code = 401

class NotFoundException(ClientError):
    code = 404
    msg = 'Not found.'
