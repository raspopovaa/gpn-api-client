import asyncio, json
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
    print("+++АВТОРИЗАЦИЯ+++")
    print(auth_response.data.contracts[1])

    # Получить региональные лимиты по договору
    response = await client.get_region_limits(contract_id=auth_response.data.contracts[1].id)
    print(response.data.result[0])
    print(f"Найдено: {response.data.total_count} региональных лимитов")
    print("-" * 80)
    for limit in response.data.result:
        print(f"ID:            {limit.id}")
        print(f"Договор:       {limit.contract_id}")
        print(f"Страна:        {limit.country}")
        print(f"Регион:        {limit.region or 'Не указан'}")
        print(f"Тип лимита:    {limit.limit_type}")
        print(f"Дата создания: {limit.date or 'Не указана'}")
        print("-" * 80)

    # # Установить региональный лимит на карту
    # await client.set_region_limit(
    #     region_limits=[
    #         {
    #             #"card_id": "2725116",
    #             #"contract_id": "1-2SY777F",
    #             "country": "RUS",
    #             #"region": "04",
    #             #"service_center": "2052059",
    #             "limit_type": 2,
    #         }
    #     ]
    # )

    # # Удалить региональный лимит
    rem_limits = await client.remove_region_limit(contract_id="1-2SY777F", regionlimit_id="65677796")
    print(rem_limits)

if __name__ == "__main__":
    asyncio.run(main())
