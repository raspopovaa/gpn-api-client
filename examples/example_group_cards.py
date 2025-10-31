import asyncio
from api_client_opti24 import *
from api_client_opti24.config import BASE_URL, API_KEY, LOGIN, PASSWORD

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

    # # 1️⃣ Получение списка групп карт по договору
    # print("=== Получение списка групп карт ===")
    # groups = await client.get_card_groups(contract_id=auth_response.data.contracts[0].id)
    # print(groups)
    # # 👉 Возвращает CardGroupListResponse с total_count и result (список групп)

    # 2️⃣ Создание новой группы карт
    print("\n=== Создание новой группы карт ===")
    new_group = await client.set_card_group(
        contract_id=auth_response.data.contracts[0].id,
        name="test_group_01"
    )
    print(new_group)
    #👉 Возвращает SetCardGroupResponse, например:
    #{"status": {"code": 200}, "data": {"id": "1-2645PK1"}}

    # # 3️⃣ Добавление карт в группу
    # print("\n=== Добавление карт в группу ===")
    # cards_response = await client.set_cards_to_group(
    #     contract_id=auth_response.data.contracts[0].id,
    #     group_id="1-2645PK1",
    #     cards_list=[
    #         {"id": "2728111", "type": "Attach"},
    #         {"id": "2728112", "type": "Attach"},
    #         {"id": "2728113", "type": "Attach"},
    #     ],
    # )
    # print(cards_response)
    # # # 👉 Возвращает SetCardsToGroupResponse (data=True при успехе)
    #
    # # 4️⃣ Удаление группы карт
    # print("\n=== Удаление группы карт ===")
    # delete_response = await client.remove_card_group(
    #     contract_id=auth_response.data.contracts[0].id,
    #     group_id="1-2T6WC93"
    # )
    # print(delete_response)
    # # 👉 Возвращает RemoveCardGroupResponse (data=True при успешном удалении)



if __name__ == "__main__":
    asyncio.run(main())