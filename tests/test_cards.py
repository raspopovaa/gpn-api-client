import pytest
import httpx
from types import SimpleNamespace

from src.api_client_opti24.services.cards import CardsMixin
from src.api_client_opti24.models.cards import (
    CardsV2Response,
    CardsV1Response,
    CardGroupResponse,
    CardDriversResponse,
    CardDetailResponse,
)


@pytest.fixture
def mock_client():
    """Создаём мок клиента с CardMixin и заглушками _request, _headers и auth_user."""

    class MockClient(CardsMixin):
        def __init__(self):
            self._called = []
            self.session_id = "fake-session"

        async def auth_user(self, *args, **kwargs):
            """Заглушка авторизации"""
            self.session_id = "fake-session"

        def _headers(self, include_session: bool = False, content_type_json: bool = False):
            """Фейковый генератор заголовков"""
            headers = {"api_key": "fake-api-key"}
            if include_session:
                headers["session_id"] = self.session_id
            if content_type_json:
                headers["Content-Type"] = "application/json"
            return headers

        async def _request(self, method, endpoint, api_version="v1", **kwargs):
            self._called.append((method, endpoint, api_version, kwargs))
            # Заглушки ответов для тестов ↓
            if endpoint == "cards" and api_version == "v2":
                return {
                    "data": {
                        "total_count": 1,
                        "result": [
                            {
                                "id": "19647206",
                                "group_id": "1-1F56KR",
                                "group_name": "Тестовая группа",
                                "contract_id": "1-1FLW4T7",
                                "contract_name": "СЗ01590002",
                                "number": "7005830900073164",
                                "status": "Active",
                                "status_name": "Активна",
                                "product": "limit",
                                "product_name": "Лимитная схема",
                                "carrier": "Virtual Card",
                                "carrier_name": "Виртуальная карта",
                                "platon": False,
                                "avtodor": True,
                                "sync_group_state": "Не синхронизирована",
                                "users": ["1-PBQRL0E"],
                                "mpc": True,
                            }
                        ],
                    }
                }
            elif endpoint == "cards" and api_version == "v1":
                return {
                    "data": {
                        "total_count": 1,
                        "result": [
                            {
                                "id": "382359",
                                "contract_id": "1-1FLKAJQ",
                                "number": "7005830001422138",
                                "status": "Active",
                                "can_work_offline": True,
                                "card_auth_type": "PIN",
                                "comment": "Комментарий",
                                "date_expired": "2034-09-30 23:59:59",
                                "date_last_usage": "2015-04-27 00:00:00",
                                "date_released": "2014-09-24 00:00:00",
                                "servicecenter_last_usage_name": "AZS103261",
                                "transaction_last_detail": "",
                                "transaction_timeout": {
                                    "type": "H",
                                    "value": "1",
                                },
                                "product": "limit",
                                "payment_of_tolls": "N",
                            }
                        ],
                    }
                }
            elif "drivers" in endpoint:
                return {
                    "data": {
                        "total_count": 1,
                        "result": [
                            {
                                "id": "1-3AKNC9S",
                                "login": "79111111111",
                                "first_name": "Роман",
                                "last_name": "Петров",
                                "middle_name": "",
                                "date": "01/01/1970",
                                "position": "Водитель",
                                "role": "Водитель",
                                "mobile_phone": "+79111111111",
                                "email": "test@test.test",
                            }
                        ],
                    }
                }
            elif endpoint == "blockCard":
                return {"data": ["517945", "517946"]}
            elif endpoint == "setCardComment":
                return {"data": True}
            elif "verifyPIN" in endpoint:
                return {"data": True}
            elif "resetPIN" in endpoint:
                return {"data": True}
            else:
                return {"data": {"total_count": 0, "result": []}}

    return MockClient()


@pytest.mark.asyncio
async def test_get_cards_v2(mock_client):
    result = await mock_client.get_cards_v2()
    assert isinstance(result, CardsV2Response)
    assert result.total_count == 1
    assert result.result[0].id == "19647206"


@pytest.mark.asyncio
async def test_get_cards_v1(mock_client):
    result = await mock_client.get_cards_v1(contract_id="1-1FLKAJQ")
    assert isinstance(result, CardsV1Response)
    assert result.total_count == 1
    assert result.result[0].status == "Active"


@pytest.mark.asyncio
async def test_get_card_drivers(mock_client):
    result = await mock_client.get_card_drivers(card_id="382359", contract_id="1-1FLKAJQ")
    assert isinstance(result, CardDriversResponse)
    assert result.total_count == 1
    assert result.result[0].first_name == "Роман"


@pytest.mark.asyncio
async def test_block_card(mock_client):
    result = await mock_client.block_card("1-B7C8D", ["517945", "517946"], block=True)
    assert result == ["517945", "517946"]


@pytest.mark.asyncio
async def test_set_card_comment(mock_client):
    result = await mock_client.set_card_comment("517945", "1-B7C8D", "COMMENT")
    assert result is True


@pytest.mark.asyncio
async def test_verify_and_reset_pin(mock_client):
    ok = await mock_client.verify_pin("382359", "1-B7C8D")
    assert ok is True

    reset = await mock_client.reset_pin("382359", "1-B7C8D", code="TESTCODE")
    assert reset is True
