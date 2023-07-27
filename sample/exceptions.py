class InvalidCredentialsExcepton(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'The ClientID or the Client Secret provided are invalid'

class TokenAlreadyInUseException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return 'The token you provided is already being used'