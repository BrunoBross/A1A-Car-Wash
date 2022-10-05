class DatabaseIntegrityException(Exception):
    """Failed transaction caused by integrity failure. Issuing database rollback."""

    pass
