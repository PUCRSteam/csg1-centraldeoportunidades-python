from errors.exceptions import Error

class ServerError(Error):
    code = 500
    msg = 'Unexpected error'
