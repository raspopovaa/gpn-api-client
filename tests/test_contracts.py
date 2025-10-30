import pytest
from src.api_client_opti24.services.contract import ContractMixin
from src.api_client_opti24.models.contracts import ContractResponse


class MockContractClient(ContractMixin):
    """Мок для ContractMixin."""

    def __init__(self):
        self.session_id = "mock-session"

    def _headers(self, include_session: bool = False, content_type_json: bool = False):
        return {"X-Mock": "true"}

    async def _request(self, method, endpoint, api_version="v1", headers=None, **kwargs):
        if endpoint == "getPartContractData":
            return {
                "data": {
                    "mpc": True,
                    "template_id": "TEMPLATE1",
                    "status": "Active",
                    "status_crm": "CRM_OK",
                    "payment_term_id": "PT1",
                    "payment_scheme_id": "PS1",
                    "is_dealer": False,   # 👈 фикс: раньше было "Is_dealer"
                    "balanceData": {
                        "available_amount": "1000",
                        "own_balance": "500",
                        "balance": "1500",
                        "consumption_for_month": "200",
                        "consumption_for_month_volume": "100",
                        "consumption_for_prev_month_volume": "90",
                        "currency": "RUB",
                    },
                    "contractData": {
                        "contract_id": "1-1FLKAJQ",
                        "way_id": "WAY1",
                        "contract_number": "C12345",
                        "unique_payment_id": "U123",
                        "client": "CLIENT1",
                        "client_category": "VIP",
                        "contract_category": "Standard",
                        "country": "RU",
                        "region": "77",
                        "fin_institution": "Bank",
                        "invoice_scheme": "Monthly",
                        "contract_status": "Active",
                        "contract_status_name": "Активен",
                        "pay_scheme": "Prepaid",
                        "discount_scheme": "DS1",
                        "auto_pay": "true",
                        "auto_pay_type": "card",
                        "current_amount_limiter": "100000",
                        "date_open": "2020-01-01",
                        "effective_date": "2020-01-01",
                        "end_date": "2030-01-01",
                        "date_expire": "2031-01-01",
                        "product_type": True,
                        "type_code": "STD",
                        "supplier_name": "SupplierX",
                    },
                    "managerData": {
                        "email": "manager@test.ru",
                        "first_name": "Иван",
                        "last_name": "Иванов",
                    },
                    "cardsData": {
                        "cards_quantity_all": "100",
                        "cards_quantity_active": "90",
                    },
                }
            }
        elif endpoint == "getPayments":
            return {"total_count": 1, "result": [{"id": "PAY1", "sum": "1000"}]}
        elif endpoint == "documents":
            if method == "get":
                return {"total_count": 1, "result": [{"id": "DOC1", "sum": "500"}]}
            elif method == "post":
                return True   # 👈 фикс
        elif endpoint == "orderCards":
            payload = kwargs.get("data", {})
            return {"ordered": payload.get("count", 0)}

        elif endpoint == "invoice":
            payload = kwargs.get("data", {})
            return {"amount": str(payload.get("sum", 0))}
        return {}


# 🔹 фикстура
@pytest.fixture
def mock_contract_client():
    return MockContractClient()


# 🔹 Тесты
@pytest.mark.asyncio
async def test_get_contract_data(mock_contract_client):
    result = await mock_contract_client.get_contract_data("1-1FLKAJQ")
    assert isinstance(result, ContractResponse)
    assert result.mpc is True
    assert result.contractData.contract_id == "1-1FLKAJQ"


@pytest.mark.asyncio
async def test_get_payments(mock_contract_client):
    result = await mock_contract_client.get_payments("1-1FLKAJQ")
    assert result["total_count"] == 1
    assert result["result"][0]["id"] == "PAY1"


@pytest.mark.asyncio
async def test_get_documents(mock_contract_client):
    result = await mock_contract_client.get_documents("2025-01-01", "2025-09-01")
    assert result["total_count"] == 1
    assert result["result"][0]["id"] == "DOC1"


@pytest.mark.asyncio
async def test_order_documents_email(mock_contract_client):
    result = await mock_contract_client.order_documents_email(
        ids=["DOC1"], fmt="pdf", emails=["test@test.ru"]
    )
    assert result is True


@pytest.mark.asyncio
async def test_order_cards(mock_contract_client):
    result = await mock_contract_client.order_cards(count=10, office_id="OFFICE1")
    assert result["ordered"] == 10


@pytest.mark.asyncio
async def test_order_invoice(mock_contract_client):
    result = await mock_contract_client.order_invoice(amount=15000, email="test@test.ru")
    assert result["amount"] == "15000"


@pytest.mark.asyncio
async def test_get_invoices(mock_contract_client):
    result = await mock_contract_client.get_invoices()
    assert result["total_count"] == 1
    assert result["result"][0]["invoice_id"] == "INV1"
