import pytest
from apiclientopti24.src.api_client_opti24 import APIClient

@pytest.mark.asyncio
async def test_auth(monkeypatch):
    client = APIClient("https://api.test/", "api_key", "login", "password")

    async def fake_request(method, endpoint, **kwargs):
        return {"data": {"session_id": "12345"}}

    client._request = fake_request
    resp = await client.auth_user()
    assert resp["data"]["session_id"] == "12345"
    assert client.session_id == "12345"
