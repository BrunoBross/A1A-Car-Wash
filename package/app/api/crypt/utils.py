import bcrypt

from package.Config import Config


salt = bcrypt.gensalt()


def encrypt(string: str) -> bytes:
    return bcrypt.hashpw(bytes(string, Config.ENCODING), salt=salt)


def matchHash(string: str, hash: bytes) -> bool:
    return bcrypt.checkpw(bytes(string, Config.ENCODING), hash)


def toBytes(string: str) -> bytes:
    return bytes(string, Config.ENCODING)
