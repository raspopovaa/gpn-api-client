import pytest
from src.api_client_opti24.services.users import UsersMixin
from src.api_client_opti24.models.users import UsersListResponse


class DummyClient(UsersMixin):
    """Мок-клиент для UsersMixin."""

    def __init__(self):
        self.session_id = "mock-session"

    def _headers(self, include_session: bool = False, content_type_json: bool = False):
        return {"X-Mock": "true"}

    async def _request(self, method, endpoint, api_version="v2", headers=None, **kwargs):
    # Эмуляция API для users
        if endpoint == "users" and method == "get":
            return {
                "data": {
                    "total_count": 1,
                    "result": [
                        {
                            "id": "1-USER",
                            "mobile": "79999999999",
                            "login": "79999999999",
                            "first_name": "Иван",
                            "last_name": "Иванов",
                            "date": "2020-01-01",
                            "role": {"id": "driver", "name": "Водитель"},
                            "access": {
                                "web": True,
                                "api": True,
                                "mobile": True
                            }
                        }
                    ],
                }
            }
        if endpoint == "users" and method == "post":
            return {"data": "1-USER"}   # ✅ теперь строка, а не dict
        if endpoint.endswith("/attachContracts"):
            return {"data": True}
        if endpoint.endswith("/attachCard"):
            return {"data": True}
        if method == "delete" and endpoint.startswith("users/"):
            return {"data": True}
        return {"data": {}}


@pytest.mark.asyncio
async def test_get_users_returns_model():
    client = DummyClient()
    response = await client.get_users()
    assert isinstance(response, UsersListResponse)
    assert response.total_count == 1
    assert response.result[0].id == "1-USER"
    assert response.result[0].first_name == "Иван"


@pytest.mark.asyncio
async def test_create_user_returns_id():
    client = DummyClient()
    user_id = await client.create_user(mobile="79999999999", uuid="test-uuid")
    # метод create_user внутри UsersMixin вернет data["id"], а не весь dict
    assert user_id == "1-USER"


@pytest.mark.asyncio
async def test_attach_and_detach_contracts():
    client = DummyClient()
    result = await client.attach_contracts("1-USER", contracts=[{"sid": "1-AAA"}])
    assert result is True


@pytest.mark.asyncio
async def test_attach_and_detach_card():
    client = DummyClient()
    result = await client.attach_card("1-USER", card_id="12345")
    assert result is True


@pytest.mark.asyncio
async def test_delete_user():
    client = DummyClient()
    result = await client.delete_user("1-USER")
    assert result is True
