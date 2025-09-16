import pytest
from unittest.mock import AsyncMock
from src.api_client_opti24.services.auth import AuthMixin
from src.api_client_opti24.models.auth import AuthUserResponse


class DummyClient(AuthMixin):
    def __init__(self):
        self.login = "test_user"
        self.password = "secret"
        self.session_id = None
        self.contract_id = None

    # Заглушка для _headers
    def _headers(self, include_session: bool = False):
        headers = {"api_key": "FAKE_API_KEY"}
        if include_session and self.session_id:
            headers["session_id"] = self.session_id
        return headers

    # Заглушка для _request
    async def _request(self, method, endpoint, **kwargs):
        if endpoint == "authUser":
            return {
                "status": {"code": 200},
                "data": {
                    "session_id": "SESSION123",
                    "contracts": [
                        {"id": "1-AAA", "number": "NV0001"},
                        {"id": "1-BBB", "number": "NV0002"},
                    ],
                },
            }
        elif endpoint == "logoff":
            return {"status": {"code": 200}, "data": True}
        elif endpoint == "info":
            return {"status": {"code": 200}, "data": {"calls": 42}}
        else:
            raise ValueError(f"Unexpected endpoint: {endpoint}")


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "contract_id,contract_number,expected_id",
    [
        ("1-AAA", None, "1-AAA"),     # выбор по id
        (None, "NV0002", "1-BBB"),    # выбор по номеру
        (None, None, "1-BBB"),        # автоселект второго по списку
    ],
)
async def test_auth_user_sets_session_and_contract_id(contract_id, contract_number, expected_id):
    client = DummyClient()
    response = await client.auth_user(contract_id=contract_id, contract_number=contract_number)

    assert isinstance(response, AuthUserResponse)
    assert client.session_id == "SESSION123"
    assert client.contract_id == expected_id


@pytest.mark.asyncio
async def test_logoff_returns_true():
    client = DummyClient()
    client.session_id = "SESSION123"  # имитируем авторизацию

    result = await client.logoff()

    assert result["status"]["code"] == 200
    assert result["data"] is True


@pytest.mark.asyncio
async def test_get_info_returns_data():
    client = DummyClient()
    client.session_id = "SESSION123"  # имитируем авторизацию

    result = await client.get_info()

    assert result["status"]["code"] == 200
    assert "calls" in result["data"]
    assert result["data"]["calls"] == 42
