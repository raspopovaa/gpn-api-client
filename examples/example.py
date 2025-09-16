import asyncio
from src.api_client_opti24.utils import print_json
from src.api_client_opti24 import APIClient
from src.api_client_opti24.config import *


async def main():
    client = APIClient(
        base_url=BASE_URL,   # твой URL API
        api_key=API_KEY,
        login=LOGIN,
        password=PASSWORD
    )

    # Авторизация
    auth_response = await client.auth_user(contract_id="1-2SY777F")
    print("=== Авторизация ===")
    for contract in auth_response.contracts:
        print(contract.id, contract.number)
    #print_json(auth_response)
    #auth_response = await client.auth_user()
    #Получение статистики
    # info_response = await client.get_info()
    # print("=== Cтатистика ===")
    # print_json(info_response)
    # # Получение списка карт
    # print("=== Список карт ===")
    # list_cards = await client.get_cards()
    # print_json(list_cards)
    # cards_info = [{'number': item['number'], 'status': item['status']} for item in list_cards['data']['result']]
    # print(cards_info)
    # print("=== CONTRACT ===")
    # contract_data = await client.get_contract_data(client.contract_id)
    # print_json(contract_data)
    # print("=== PAYMENTS ===")
    # print_json(await client.get_payments(client.contract_id))
    # print("=== DOCUMENTS ===")             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #   File "/Users/andrejraspopov/IdeaProjects/APIv2/apiclientopti24/src/api_client_opti24/services/auth.py", line 99, in auth_user
    #     return await data
    #            ^^^^^^^^^^
    # TypeError: object dict can't be used in 'await' expression

    # print(json.dumps(await client.getDocuments("2019-01-01", "2025-01-01", api_version="v2"), indent=2, ensure_ascii=False))
    # #Заказ документов на почту
    # print(json.dumps(await client.orderDocumentsEmail(
    #     ids=["6fffd550-b55f-11e9-8123-005056a969a3","27a19fb4-cdd0-11e9-8127-005056a969a3"],
    #     fmt="pdf",
    #     emails=["andrew.raspopov@yandex.ru"]
    # ), indent=2, ensure_ascii=False))
    # print("=== ORDER CARDS ===")
    # print(json.dumps(await client.orderCards(count=5, office_id="1-13HS"), indent=2, ensure_ascii=False))
    # print("=== ORDER INVOICE ===")
    # print(json.dumps(await client.orderInvoice(amount=50000, email="andrew.raspopov@yandex.ru"), indent=2, ensure_ascii=False))
    # #
    # print("=== INVOICES ===")
    # print(json.dumps(await client.getInvoices(), indent=2, ensure_ascii=False))
    #
    # print("=== search CARDS ===")
    # print(json.dumps(await client.get_contract_cards_v2(
    #     #contract_id=client.contract_id,
    #     #sort="-id",
    #     #q="7005830010286291",
    #     #status="Active",
    #     #carrier="Plastic",
    #     #platon=True,
    #     #avtodor=True,
    #     #users=True,
    #     #page=1,
    #     #on_page=10
    # ), indent=2, ensure_ascii=False))
    # #7005830010286293 79000003
    #
    # print("=== PROCESSING CARDS ===")
    # resp = await client.getProcessingCards(cache=False,)
    # print(json.dumps(resp, indent=2, ensure_ascii=False))

    # print("=== GROUP CARDS ===")
    # resp = await client.getGroupCards(contract_id=client.contract_id, group_id="1-2T6WC93")
    # print_json(resp)
    # print("=== SET GROUP CARDS ===")
    # resp_new = await client.set_card_group(
    #     name="groupcard-4"
    # )
    # print(resp_new)
    # print("=== CARD DRIVERS ===")
    # resp = await client.getCardDrivers(card_id="98000001")
    # print(json.dumps(resp, indent=2, ensure_ascii=False))

    # # Блокировка карт
    # resp_block = await client.block_card(
    #     card_ids=["98000001"],
    #     block=True
    # )
    # print("Заблокированы:", resp_block)
    #
    # # Разблокировка карт
    # resp_unblock = await client.block_card(
    #     card_ids=["98000001"],
    #     block=False
    # )
    # print("Разблокированы:", resp_unblock)
    # resp = await client.set_card_comment(
    #     card_id="98000001",
    #     comment="Карта закреплена за КамАЗом"
    # )
    # print(resp)


    # # 1. Запрос кода сброса PIN
    # await client.request_reset_pin(card_id="98000001")
    #
    # # 2. Подтверждение сброса с кодом из email
    # resp = await client.reset_pin(
    #     card_id="98000001",
    #     code="4K5KL5K4LKFGLK6YK6LKGH6LK4LF43F"
    # )
    # print(resp)

    #     # Изменить тип карты на электронный кошелёк
    # await client.set_card_product(card_ids=["98000001"], product="wallet")

    # # Перевести 5000 с договора на кошелёк
    # await client.move_to_card(card_id="98000001", amount=5000)
    #
    # # Вернуть 2000 обратно с кошелька на договор
    # await client.move_to_contract(card_id="98000001", amount=2000)





    # # Последние транзакции по договору
    # txs = await client.get_transactions(contract_id="1-2SY777F", count=5)

    # # Последние транзакции по карте
    # txs = await client.get_transactions(contract_id="1-2SY777F", card_id="98000001", count=5)

    # # Транзакции по договору за период (v2)
    # txs_v2 = await client.get_transactions_v2(
    #     contract_id="1-2SY777F",
    #     date_from="2020-08-01",
    #     date_to="2020-08-31"
    # )

    # # Транзакции по карте (v2)
    # txs_card = await client.get_card_transactions(
    #     card_id="98000001",
    #     contract_id="1-2SY777F",
    #     date_from="2025-08-01",
    #     date_to="2025-08-31"
    # )
    #
    # # # Детали транзакции
    # # details = await client.get_transaction_details(transaction_id="9281938437")
    #
    # Все транзакции по договору (v1), отсортированные по сумме убыванию
    # tx_list = await client.get_transactions(
    #     contract_id="1-2SY777F",
    #     sort_by="sum",
    #     reverse=True
    # )
    # print([tx.sum for tx in tx_list.result])
    #
    # # Фильтрация: только транзакции по продукту "Аи-95"
    # tx_list = await client.get_transactions_v2(
    #     contract_id="1-2SY777F",
    #     date_from="2025-08-01",
    #     date_to="2025-08-31",
    #     filter_fn=lambda tx: tx.product_name == "Аи-95"
    # )
    # print(f"Аи-95 транзакций: {tx_list.total_count}")
    #
    # # Фильтрация и сортировка по времени
    # tx_card_list = await client.get_card_transactions(
    #     card_id="2766953",
    #     contract_id="1-2SY777F",
    #     date_from="2025-08-01",
    #     date_to="2025-08-31",
    #     filter_fn=lambda tx: tx.sum and tx.sum > 1000,
    #     sort_by="timestamp"
    # )
    # for tx in tx_card_list.result:
    #     print(tx.timestamp, tx.sum)
    # # Получить лимиты по договору
    # limits = await client.get_limits(contract_id="1-2SY777F")
    # print("Найдено лимитов:", limits.total_count)
    # for limit in limits.result:
    #     print(limit.contract_id, limit.card_id, limit.amount)

    # # Установить лимит на карту (литры)
    # await client.set_limit(
    #     limits=[
    #         {
    #             "card_id": "98000001",
    #             "contract_id": "1-2SY777F",
    #             "productGroup": "1-CK235",
    #             "productType": "1-CK231",
    #             "amount": {"value": 123, "unit": "LIT"},
    #             "term": {"time": {"from": "03:00", "to": "08:00"}, "days": "1111100", "type": 1},
    #             "transactions": {"count": 40},
    #             "time": {"number": 4, "type": 7},
    #         }
    #     ]
    # )
    #
    # # Удалить лимит
    # await client.remove_limit(contract_id="1-2SY777F", limit_id="1-FKFLDK1")

    #
    # # Получить ограничения по договору
    # restrictions = await client.get_restrictions(contract_id="1-2SY777F")
    # print("Найдено ограничителей:", restrictions.total_count)
    # for r in restrictions.result:
    #     print(r.id, r.productTypeName, r.restriction_type)

    # # Установить ограничитель на карту
    # await client.set_restriction(
    #     restrictions=[
    #         {
    #             "card_id": "2748116",
    #             "contract_id": "1-1N3MWYG",
    #             "productGroup": "1-CK235",
    #             "productType": "1-CK231",
    #             "restriction_type": 1
    #         }
    #     ]
    # )
    #
    # # Удалить ограничитель
    # await client.remove_restriction(contract_id="1-B7C8D", restriction_id="15988463")



    # # Получить региональные лимиты по договору
    # limits = await client.get_region_limits(contract_id="1-2SY777F")
    # print("Региональных лимитов:", limits.total_count)
    # for rl in limits.result:
    #     print(rl.id, rl.country, rl.region, rl.limit_type)

    # # Установить региональный лимит на карту
    # await client.set_region_limit(
    #     region_limits=[
    #         {
    #             "card_id": "2725116",
    #             "contract_id": "1-1N3MWYG",
    #             "country": "RUS",
    #             "region": "04",
    #             "service_center": "2052059",
    #             "limit_type": 1,
    #         }
    #     ]
    # )
    #
    # # Удалить региональный лимит
    # await client.remove_region_limit(contract_id="1-B7C8D", regionlimit_id="6358201")


    # # Получение групп карт по договору
    # groups = await client.get_card_groups(contract_id="1-2SY777F")
    # for g in groups.result:
    #     print(g.id, g.name, g.cards_count)

    # # Создание новой группы
    # new_group = await client.set_card_group(contract_id="1-2SY777F", name="groupcard-4")

    # # Добавление карт в группу
    # await client.set_cards_to_group(
    #     contract_id="1-1N5MWYG",
    #     group_id=new_group["data"]["id"],
    #     cards_list=[{"id": "2728111", "type": "Attach"}, {"id": "2728112", "type": "Attach"}],
    # )
    #
    # # Удаление группы
    # await client.remove_card_group(contract_id="1-1N5MWYG", group_id=new_group["data"]["id"])




    # --- v2 ---
    # # Получить список доступных отчетов
    # reports = await client.get_reports()
    # for r in reports.result:
    #     print(r.id, r.name)

    # # Заказать отчет (по договору на email)
    # order = await client.order_report(
    #     report_id="tsc_transaction_protocol",
    #     format="xlsx",
    #     emails=["test@yandex.ru"],
    #     params={"start_date": "2022-11-02", "end_date": "2022-12-01", "id_agreement": ["1-2SY777F"]},
    # )
    #
    # # Список заказанных отчетов
    # jobs = await client.get_report_jobs()
    # for j in jobs.result:
    #     print(j.job_id, j.report_name)
    # #
    # ждём 5 минут после заказа отчёта
    #await asyncio.sleep(300)

    # content = await client.download_report_file(job_id="1-2FLFKAW")
    #
    # with open("report.xlsx", "wb") as f:
    #     f.write(content)
    #
    # # Скачиваем отчет (v1, в zip)
    # content = await client.download_report_file_v1(job_id="1-24H0D3I", archive=True)
    # with open("report.zip", "wb") as f:
    #     f.write(content)
    #
    #
    # # --- v1 (устаревшие) ---
    # await client.order_report_v1(
    #     contract_id="1-13WR9S2",
    #     start="2017-01-01",
    #     end="2017-01-31",
    #     report_format="xlsx",
    #     email="mail@mail.ru",
    # )
    #
    # jobs_v1 = await client.get_report_job_list_v1()
    # print(jobs_v1)

    # # список приглашений
    # await client.list(role="Driver", status="Active")

    # # создать с отправкой
    # await client.create({
    #     "role": "Driver",
    #     "mobile": "7999999999",
    #     "contracts": [{"id": "1-FFFFF", "template_id": "1-FKFKF"}]
    # })
    #
    # создать без отправки (только ссылка)
    # await client.create({
    #     "role": "Driver",
    #     "email": "test@test.yy",
    #     "cards": ["5554324", "4224443"]
    # }, with_send=False)
    # #
    # # удалить
    # await client.delete("5ddc1bd27f6e1101316dace6")
    #
    # # повторная отправка
    # await client.resend("5ddc1bd27f6e1101316dace6")
    #
    # # продление без отправки
    # await client.prolong("5e6fe829-ec61-4a18-8c4e-76df122979a5", with_send=False)

if __name__ == "__main__":
    asyncio.run(main())
