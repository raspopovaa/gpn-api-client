from .logger import logger


class APIError(Exception):
    """
Базовое исключение для ошибок API клиента.

Attributes:
    status_code (int): HTTP-статус ошибки.
    message (str): Текстовое описание ошибки.
    body (dict): Ответ сервера в формате JSON (если доступен).
"""
    def __init__(self, status_code: int, message: str = "", body: dict | None = None, endpoint: str | None = None):
        super().__init__(f"{status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.body = body or {}
        self.endpoint = endpoint

    def __str__(self):
        if self.endpoint:
            logger.info(f"{self.__class__.__name__}: [{self.status_code}] {self.message} при вызове метода {self.endpoint}")
            return f"{self.__class__.__name__}: [{self.status_code}] {self.message} при вызове метода {self.endpoint}"
        else:
            logger.info(f"{self.__class__.__name__}: [{self.status_code}] {self.message}")
            return f"{self.__class__.__name__}: [{self.status_code}] {self.message}"

class ValidationError(APIError): pass
class NotAuthenticatedError(APIError): pass
class AccessDeniedError(APIError): pass
class NotFoundError(APIError): pass
class DuplicateConflictError(APIError): pass
class ServerError(APIError): pass


