import asyncio, json
from http.client import responses

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


    #     # Изменить тип карты на электронный кошелёк
    # await client.set_card_product(card_ids=["98000001"], product="wallet")

    # Перевести 5000 с договора на кошелёк
    respons = await client.move_to_card(card_id="98000001", amount=5000)
    print(respons.data)

    # # Вернуть 2000 обратно с кошелька на договор
    # respons1 = await client.move_to_contract(card_id="98000001", amount=2000)
    # print(respons1.data)

if __name__ == "__main__":
    asyncio.run(main())