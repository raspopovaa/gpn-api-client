import asyncio
from src.api_client_opti24 import APIClient
from src.api_client_opti24.config import BASE_URL, API_KEY, LOGIN, PASSWORD


async def main():
    """
    Пример использования API-клиента раздела 'cards'.
    Показывает авторизацию, получение информации о картах и операции с ними.
    """
    client = APIClient(
        base_url=BASE_URL,
        api_key=API_KEY,
        login=LOGIN,
        password=PASSWORD,
    )

    # === АВТОРИЗАЦИЯ ===
    auth_response = await client.auth_user()
    print("+++ АВТОРИЗАЦИЯ +++")
    print("Текущий договор:", auth_response.data.contracts[0].id)

    # print("=== СПИСОК КАРТ ДОГОВОРА (v2) ===")
    # cards_v2 = await client.get_cards_v2(
    #     contract_id=client.contract_id,
    #     # sort="-id",
    #     # q="700582009",
    #     # status="Active",
    #     # carrier="Plastic",
    #     # platon=True,
    #     # avtodor=True,
    #     # users=True,
    #     # page=1,
    #     # onpage=10,
    # )
    # print("Всего карт:", cards_v2.data.total_count)
    # print("Первая карта:", cards_v2.data.result[0].number)

    # === СПИСОК КАРТ (v1, процессинг) ===
    # cards_v1 = await client.get_cards_v1(contract_id=client.contract_id)
    # print("=== CARDS v1 ===")
    # print("Всего карт:", cards_v1.data.total_count)

    # === КАРТЫ ПО ГРУППЕ ===
    # group_cards = await client.get_cards_by_group(
    #     contract_id=client.contract_id,
    #     group_id="1-2T6WC93",
    # )
    # print("=== GROUP CARDS ===")
    # print("Количество карт в группе:", group_cards.data.total_count)

    # === СОЗДАНИЕ НОВОЙ ГРУППЫ КАРТ ===
    new_group = await client.set_card_group(
        contract_id=client.contract_id,
        name="groupcard-4",
    )
    print("=== SET GROUP CARD ===")
    print("Создана новая группа:", new_group)

    # === СПИСОК ВОДИТЕЛЕЙ ПО КАРТЕ ===
    print("=== CARD DRIVERS ===")
    card_drivers = await client.get_card_drivers(
        contract_id=client.contract_id,
        card_id="98000001",
    )
    print(card_drivers)

    # === ДЕТАЛЬНАЯ ИНФОРМАЦИЯ ПО КАРТЕ ===
    print("=== CARD DETAIL ===")
    card_detail = await client.get_card_detail(
        contract_id=client.contract_id,
        card_id="98000002",
    )
    print(card_detail)

    # === УСТАНОВКА КОММЕНТАРИЯ ДЛЯ КАРТЫ ===
    print("=== SET CARD COMMENT ===")
    comment_result = await client.set_card_comment(
        contract_id=client.contract_id,
        card_id="98000001",
        comment="Карта закреплена за КамАЗом",
    )
    print("Комментарий установлен:", comment_result)

    # === БЛОКИРОВКА КАРТ ===
    # print("=== BLOCK CARD ===")
    # block_result = await client.block_card(
    #     contract_id=client.contract_id,
    #     card_ids=["98000002"],
    #     block=True,
    # )
    # print("Заблокированы:", block_result)

    # === РАЗБЛОКИРОВКА КАРТ ===
    # print("=== UNBLOCK CARD ===")
    # unblock_result = await client.block_card(
    #     contract_id=client.contract_id,
    #     card_ids=["98000001"],
    #     block=False,
    # )
    # print("Разблокированы:", unblock_result)

    # === ЗАПРОС КОДА ДЛЯ СБРОСА PIN ===
    print("=== VERIFY PIN ===")
    verify_pin = await client.verify_pin(
        contract_id=client.contract_id,
        card_id="98000001",
    )
    print("Код подтверждения отправлен:", verify_pin.data)

    # === ПОДТВЕРЖДЕНИЕ СБРОСА PIN ===
    # print("=== RESET PIN ===")
    # reset_pin = await client.reset_pin(
    #     contract_id=client.contract_id,
    #     card_id="98000001",
    #     code="1265445",  # код из письма
    # )
    # print("PIN сброшен:", reset_pin)


if __name__ == "__main__":
    asyncio.run(main())
