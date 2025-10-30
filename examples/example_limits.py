import asyncio
from src.api_client_opti24 import APIClient
from src.api_client_opti24.config import *


async def main():
    client = APIClient(
        base_url=BASE_URL,   # твой URL API
        api_key=API_KEY,
        login=LOGIN,
        password=PASSWORD
    )

    # Авторизация пользователя
    auth_response = await client.auth_user()
    print("===АВТОРИЗАЦИЯ===")
    print(auth_response.data.contracts[1])

    # Получение лимитов по договору
    limits = await client.get_limits(contract_id=auth_response.data.contracts[1].id)
    print(limits.data.result[0])

    # # Установка лимита на карту
    # new_limit = [{
    #     "card_id": "2724116",
    #     "contract_id": auth_response.data.contracts[0].id,
    #     "productGroup": "1-CK235",
    #     "productType": "1-CK231",
    #     "amount": {"value": 123, "unit": "LIT"},
    #     "term": {"time": {"from": "03:00", "to": "08:00"}, "days": "1111100", "type": 1},
    #     "transactions": {"count": 40},
    #     "time": {"number": 4, "type": 7}
    # }]
    # resp = await client.set_limit(limits=new_limit)
    # print("Создан лимит:", resp.data)

    # # Удаление лимита
    # del_resp = await client.remove_limit(contract_id=auth_response.data.contracts[0].id, limit_id="1-FKFLDK1")
    # print("Удаление лимита:", del_resp.data)

if __name__ == "__main__":
    asyncio.run(main())