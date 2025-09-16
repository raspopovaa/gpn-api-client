import logging

import httpx
from apiclientopti24.config import LOG_LEVEL, LOGGER_FILE
log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
logging.basicConfig(
    level=log_level,
    #filename=LOGGER_FILE,
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("transport")
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from .errors import (
    APIError, ValidationError, NotAuthenticatedError,
    AccessDeniedError, NotFoundError, DuplicateConflictError, ServerError
)


class AsyncTransport:
    def __init__(self, base_url: str, client: "APIClientOPTI24"):
        self.base_url = base_url.rstrip("/") + "/"
        self.client = httpx.AsyncClient(timeout=30)
        self._parent = client


    def _build_url(self, api_version: str, endpoint: str) -> str:
        return f"{self.base_url}{api_version}/{endpoint.lstrip('/')}"

    def _handle_response(self, resp: httpx.Response , endpoint: str) -> dict or list:
        if 200 <= resp.status_code < 300:
            try:
                return resp.json()
            except Exception:
                return resp.text
        elif resp.status_code == 400:
            raise ValidationError(resp.status_code, "Некорректные данные", resp.json(), endpoint = endpoint)
        elif resp.status_code == 401:
            raise NotAuthenticatedError(resp.status_code, "Необходима авторизация", resp.json(), endpoint = endpoint)
        elif resp.status_code == 403:
            raise AccessDeniedError(resp.status_code, "Доступ запрещен", resp.json(), endpoint = endpoint)
        elif resp.status_code == 404:
            raise NotFoundError(resp.status_code, "Ресурс не найден", resp.json(), endpoint = endpoint)
        elif resp.status_code == 409:
            raise DuplicateConflictError(resp.status_code, "Конфликт", resp.json(), endpoint = endpoint)
        elif 500 <= resp.status_code < 600:
            raise ServerError(resp.status_code,  "Ошибка сервера", resp.text, endpoint = endpoint)
        else:
            raise APIError(resp.status_code,  "Неизвестная ошибка", resp.text, endpoint = endpoint)

    @retry(
        reraise=True,
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=60),
        retry=retry_if_exception_type(httpx.RequestError),
    )
    async def request(self, method: str, endpoint: str, api_version: str = "v1", headers=None, retry_auth: bool = True, **kwargs):
        url = self._build_url(api_version, endpoint)
        resp = await self.client.request(method, url, headers=headers, **kwargs)
        logger.info(resp.status_code)

        if resp.status_code == 401 and retry_auth:
            await self._parent.auth_user()
            headers = self._parent._headers(include_session=True)
            return await self.request(method, endpoint, api_version, headers=headers, retry_auth=False, **kwargs)

        return self._handle_response(resp, endpoint)

    async def request_stream(self, method: str, url: str, headers=None, **kwargs) -> bytes:
        """Для скачивания бинарных файлов (PDF, XLSX, ZIP и т.д.)."""
        async with self.client.stream(method, url, headers=headers, **kwargs) as resp:
            resp.raise_for_status()
            return await resp.aread()
