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
    print(auth_response.data.contracts[0])
    contract_id = auth_response.data.contracts[0].id

        # Получить список ограничителей
    resp = await client.get_restrictions(contract_id=contract_id)
    print(resp.data.total_count)
    print(resp.data.result[0])

    # # Создать новый ограничитель
    # new_restriction = [{
    #     #"card_id": "98000001",
    #     "contract_id": contract_id,
    #     #"productGroup": "1-CK235",
    #     "productType": "1-CK231",
    #     "restriction_type": 1
    # }]
    # resp = await client.set_restriction(restrictions=new_restriction)
    # print(resp.data)  # ['18208262']
    #
    # Удалить ограничитель
    resp = await client.remove_restriction(
        contract_id=contract_id,
        restriction_id="54435568"
    )
    print(resp.data)  # True


if __name__ == "__main__":
    asyncio.run(main())