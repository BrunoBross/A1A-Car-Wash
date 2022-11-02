class DatabaseIntegrityException(Exception):
    def __str__(self):
        return """
Failed transaction caused by integrity failure. Issuing database rollback."""
