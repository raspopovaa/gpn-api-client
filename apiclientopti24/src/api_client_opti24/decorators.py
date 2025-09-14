import functools
import logging
from apiclientopti24.config import *
# log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
# logging.basicConfig(
#     level=log_level,
#     filename=LOGGER_FILE,
#     filemode="a",
#     format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
# )
# logger = logging.getLogger("decorators")
#
#
# def api_method(require_session: bool = False, default_version: str = "v1"):
#     def decorator(func):
#         @functools.wraps(func)
#         async def wrapper(self, *args, **kwargs):
#             if "api_version" not in kwargs:
#                 kwargs["api_version"] = default_version
#             if require_session and not self.session_id:
#                 logger.info("Нет session_id → авторизация...")
#                 await self.auth_user()
#             logger.info(f"Вызов метода {func.__name__}")
#             return await func(self, *args, **kwargs)
#         return wrapper
#     return decorator
# Настройка логирования через config
log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
logging.basicConfig(
    level=log_level,
    #filename=LOGGER_FILE,
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("api_client_opti24.decorators")


def api_method(require_session: bool = False, default_version: str = "v1"):
    """
    Декоратор для API-методов.
    - Добавляет api_version, если не указана
    - Выполняет авторизацию, если session_id отсутствует
    - Логирует вызовы, результаты и ошибки
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(self, *args, **kwargs):
            method_name = f"{self.__class__.__name__}.{func.__name__}"

            if "api_version" not in kwargs:
                kwargs["api_version"] = default_version

            if require_session and not getattr(self, "session_id", None):
                logger.info(f"[{method_name}] Нет session_id → выполняем авторизацию...")
                await self.auth_user()

            logger.info(f"➡ Вызов {method_name}, args={args}, kwargs={kwargs}")

            try:
                result = await func(self, *args, **kwargs)
                # Логируем только первые 500 символов ответа
                result_preview = str(result)[:300]
                logger.info(f"✅ {method_name} завершён. Результат: {result_preview}")
                return result
            except Exception as e:
                logger.error(f"❌ Ошибка в {method_name}: {e}", exc_info=True)
                raise
        return wrapper
    return decorator