class DatabaseConnectionFailedException(Exception):
    def __str__(self):
        return """
Failed to connect to application database. Is 'A1A_DATABASE' environment variable set?"""
