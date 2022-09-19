class DatabaseConnectionFailedException(Exception):
    """Failed to connect to application database. Is 'A1A_DATABASE' environment variable set?"""
    pass
