class InvalidKeyError(ValueError):
    def __init__(self, message, errors):
        super(InvalidKeyError, self).__init__(message)
        self.errors = errors


class InvalidPrivateKeyError(InvalidKeyError):
    pass


class InvalidPublicKeyError(InvalidKeyError):
    def __init__(self):
        message = "Public key is not properly formatted"
        super(InvalidKeyError, self).__init__(message)