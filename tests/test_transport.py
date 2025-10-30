import pytest
from httpx import Response, Request
from src.api_client_opti24.transport import AsyncTransport
from src.api_client_opti24.errors import AccessDeniedError, NotFoundError, ServerError, APIError


class DummyResp(Response):
    """Простейший заглушка для имитации ответов httpx.Response"""
    def __init__(self, status_code, text=None, json_data=None):
        self._text = text
        self._json_data = json_data
        self._request = Request(method="GET", url="http://example.com/endpoint")
        super().__init__(status_code=status_code, content=text.encode() if text else b"")

    def json(self):
        if self._json_data is not None:
            return self._json_data
        return self.text  # Возвращаем текст вместо исключения

    @property
    def text(self):
        return self._text or ""


def test_handle_response_success_json():
    t = AsyncTransport(base_url="http://example.com", client=None)
    resp = DummyResp(200, json_data={"ok": True})
    result = t._handle_response(resp, "test")
    assert result == {"ok": True}


def test_handle_response_success_text_fallback():
    t = AsyncTransport(base_url="http://example.com", client=None)
    resp = DummyResp(200, text="plain text")
    result = t._handle_response(resp, "test")
    assert result == "plain text"


@pytest.mark.parametrize(
    "status,exc_type",
    [
        (403, AccessDeniedError),
        (404, NotFoundError),
        (500, ServerError),
        (418, APIError),  # I'm a teapot :)
    ],
)
def test_handle_response_errors(status, exc_type):
    t = AsyncTransport(base_url="http://example.com", client=None)
    resp = DummyResp(status, text="error response")
    with pytest.raises(exc_type):
        t._handle_response(resp, "endpoint")