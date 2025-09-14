# APIClientOPTI24

Async API client for Газпромнефть топливные карты.

## Установка

```bash
poetry install
```

## Пример использования

```python
import asyncio
from api_client_opti24 import APIClient

async def main():
    client = APIClient(
        base_url="https://api.gpnbonus.ru/",
        api_key="your_api_key",
        login="your_login",
        password="your_password"
    )
    await client.auth_user()
    async for tx in client.iter_transactions("1-2Q45DA8", "2024-01-01", "2024-01-31"):
        print(tx)

asyncio.run(main())
```
