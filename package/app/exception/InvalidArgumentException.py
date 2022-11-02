class InvalidArgumentException(Exception):
    def __str__(self):
        return """
Invalid command line arguments"""
