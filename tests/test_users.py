# tests/test_users.py
import pytest
from src.api_client_opti24.services.users import UsersMixin
from src.api_client_opti24.models.users import UsersListResponse


class DummyClient(UsersMixin):
    def __init__(self):
        self._called = []
        self.session_id = "test-session"

    async def _request(self, method, endpoint, **kwargs):
        self._called.append((method, endpoint, kwargs))

        if endpoint == "users" and method == "get":
            return {
                "status": {"code": 200},
                "data": {
                    "total_count": 1,
                    "result": [
                        {
                            "id": "1-USER",
                            "login": "79999999999",
                            "first_name": "Иван",
                            "last_name": "Иванов",
                            "middle_name": "Иванович",
                            "date": "01/01/1990",
                            "position": "Водитель",
                            "role": {"id": "Driver", "name": "Водитель"},
                            "active": True,
                            "access": {"web": True, "api": False, "mobile": True},
                            "mobile_phone": "79999999999",
                            "email": "test@test.ru",
                            "contracts": [
                                {
                                    "sid": "1-AAA",
                                    "number": "NV0001",
                                    "available": True,
                                    "status": {"id": "Active", "name": "Активен"},
                                    "template_id": None,
                                    "cards_count": 1,
                                }
                            ],
                            "cards": [
                                {
                                    "id": "1-CARD",
                                    "sid": "123456",
                                    "number": "7005830001",
                                    "mpc": True,
                                    "product": "wallet",
                                    "comment": "Test card",
                                    "status": "Active",
                                    "contract_id": "1-AAA",
                                    "contract_name": "NV0001",
                                    "available": True,
                                }
                            ],
                        }
                    ],
                },
            }

        if endpoint == "users" and method == "post":
            return {"status": {"code": 200}, "data": "1-NEWUSER"}

        if endpoint.endswith("attachContracts"):
            return {"status": {"code": 200}, "data": True}

        if endpoint.endswith("detachContracts"):
            return {"status": {"code": 200}, "data": True}

        if endpoint.endswith("attachCard"):
            return {"status": {"code": 200}, "data": True}

        if endpoint.endswith("detachCard"):
            return {"status": {"code": 200}, "data": True}

        if endpoint.startswith("users/") and method == "delete":
            return {"status": {"code": 200}, "data": True}

        raise ValueError(f"Unexpected call: {method} {endpoint}")


@pytest.mark.asyncio
async def test_get_users_returns_model():
    client = DummyClient()
    response = await client.get_users()
    assert isinstance(response, UsersListResponse)
    assert response.total_count == 1
    assert response.result[0].first_name == "Иван"
    assert response.result[0].contracts[0].number == "NV0001"


@pytest.mark.asyncio
async def test_create_user_returns_id():
    client = DummyClient()
    user_id = await client.create_user(mobile="79999999999", uuid="test-uuid")
    assert user_id == "1-NEWUSER"


@pytest.mark.asyncio
async def test_attach_and_detach_contracts():
    client = DummyClient()
    result = await client.attach_contracts("1-USER", contracts=[{"sid": "1-AAA"}])
    assert result is True

    result = await client.detach_contracts("1-USER", contracts=["1-AAA"])
    assert result is True


@pytest.mark.asyncio
async def test_attach_and_detach_card():
    client = DummyClient()
    result = await client.attach_card("1-USER", card_id="12345")
    assert result is True

    result = await client.detach_card("1-USER", card_id="12345")
    assert result is True


@pytest.mark.asyncio
async def test_delete_user():
    client = DummyClient()
    result = await client.delete_user("1-USER")
    assert result is True
