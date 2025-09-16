import pytest
from src.api_client_opti24 import APIClient
from src.api_client_opti24.models.auth import AuthUserResponse
from src.api_client_opti24.config import BASE_URL, API_KEY, LOGIN, PASSWORD


@pytest.mark.asyncio
async def test_auth(monkeypatch):
    client = APIClient(
        base_url=BASE_URL,
        api_key=API_KEY,
        login=LOGIN,
        password=PASSWORD
    )

    async def fake_request(method, endpoint, **kwargs):
        return {"data": {"session_id": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9"}}

    monkeypatch.setattr(client, "_request", fake_request)

    resp = await client.auth_user()

    assert isinstance(resp, AuthUserResponse)
    assert resp.session_id == "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiYWE3NmY5YjFkMGQxZWEwYmJjZTczNDA4YzVjODY4ZmUyNWRhYTY0N2RhYzMzMGI1Njc1NTc2ZjZkODRiNjBjMzc3NTE0MmIyNGZlY2VmYzIiLCJpYXQiOjE3NTgwNTQwNzAuMzkyMTY1LCJuYmYiOjE3NTgwNTQwNzAuMzkyMTY3LCJleHAiOjE3NjA2NDYwNzAuMzg4NzU3LCJzdWIiOiIxLTVTS0s1NUE"
    assert client.session_id == "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiYWE3NmY5YjFkMGQxZWEwYmJjZTczNDA4YzVjODY4ZmUyNWRhYTY0N2RhYzMzMGI1Njc1NTc2ZjZkODRiNjBjMzc3NTE0MmIyNGZlY2VmYzIiLCJpYXQiOjE3NTgwNTQwNzAuMzkyMTY1LCJuYmYiOjE3NTgwNTQwNzAuMzkyMTY3LCJleHAiOjE3NjA2NDYwNzAuMzg4NzU3LCJzdWIiOiIxLTVTS0s1NUE"