import asyncio
from api_client_opti24 import APIClient
from api_client_opti24 import BASE_URL, API_KEY, LOGIN, PASSWORD


async def main():
    client = APIClient(
        base_url=BASE_URL,
        api_key=API_KEY,
        login=LOGIN,
        password=PASSWORD
    )

    # === Авторизация пользователя ===
    auth_response = await client.auth_user()
    print("\n=== Авторизация ===")
    print(f"Контракт: {auth_response.data.contracts[0].number}")
    contract_id = auth_response.data.contracts[0].id

    # # -----------------------------------------------------------
    # # 1️⃣ v1 — Список последних транзакций по договору или карте
    # # -----------------------------------------------------------
    # print("\n=== ТРАНЗАКЦИИ v1 ===")
    # tx_v1 = await client.get_transactions_v1(
    #     contract_id=contract_id,
    #     # card_id="79000001",  # можно указать для фильтра по карте
    #     count=5
    # )
    # print(f"Всего транзакций: {tx_v1.data.total_count}")
    # for t in tx_v1.data.result:
    #     print(f"- ID: {t.id}, Время: {t.time}, Сумма: {t.cost}, Карта: {t.card_number}")

    # -----------------------------------------------------------
    # 2️⃣ v2 — Список транзакций по договору
    # -----------------------------------------------------------
    # print("\n=== ТРАНЗАКЦИИ ПО ДОГОВОРУ (v2) ===")
    # tx_v2 = await client.get_transactions_v2(
    #     contract_id=contract_id,
    #     date_from="2020-09-01",
    #     date_to="2020-09-30",
    #     page_limit=1
    # )
    # print(f"Всего найдено: {tx_v2.data.total_count}")
    # for tx in tx_v2.data.result[:3]:
    #     print(f"- {tx.timestamp} | Карта {tx.card_number} | {tx.sum} {tx.currency}")

    # -----------------------------------------------------------
    # 3️⃣ v2 — Список транзакций по карте
    # -----------------------------------------------------------
    # print("\n=== ТРАНЗАКЦИИ ПО КАРТЕ (v2) ===")
    # card_id = "98000001"  # пример ID карты
    # tx_card = await client.get_card_transactions_v2(
    #     card_id=card_id,
    #     contract_id=contract_id,
    #     date_from="2021-09-01",
    #     date_to="2021-09-30",
    #     page_limit=10
    # )
    # print(f"По карте {card_id} найдено транзакций: {tx_card.data.total_count}")
    # for tx in tx_card.data.result[:3]:
    #     print(f"- ID: {tx.id} | Сумма: {tx.sum} | Продукт: {tx.product_name}")

    # # -----------------------------------------------------------
    # # 4️⃣ v2 — Детали конкретной транзакции
    # # -----------------------------------------------------------
    # print("\n=== ДЕТАЛИ ТРАНЗАКЦИИ (v2) ===")
    # transaction_id = "9281938437"  # пример ID транзакции
    # tx_detail = await client.get_transaction_detail(
    #     transaction_id=transaction_id,
    #     contract_id=contract_id
    # )
    # detail = tx_detail.data.result[0]
    #
    # print(f"ID: {detail.id}")
    # print(f"Дата: {detail.timestamp}")
    # print(f"Карта: {detail.card_number}")
    # print(f"Сумма: {detail.sum}")
    # print(f"Продукт: {detail.product_name}")
    # print(f"Тип: {detail.type}")
    # print(f"Сторнировано: {detail.is_storno}")
    #
    # print("\n=== Готово ===")
    #

if __name__ == "__main__":
    asyncio.run(main())
