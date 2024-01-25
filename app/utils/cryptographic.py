from cryptography.fernet import Fernet
from settings import settings

cipher_suite = Fernet(settings.ENCRYPTION_KEY.encode())


def encrypt(value: str) -> str:
    v = cipher_suite.encrypt(value.encode())

    return v.decode()


def decrypt(value: str) -> str:
    v = cipher_suite.decrypt(value.encode())

    return v.decode()
