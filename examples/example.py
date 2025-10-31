import asyncio

from api_client_opti24 import *


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
    limits = await client.get_region_limits(contract_id="1-2SY777F")
    print("Региональных лимитов:", limits)
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


    # # 📌 Список пользователей
    # users = await client.get_users(
    #     sort="id,login",
    #     page=1,
    #     on_page=5,
    #     q="Кирилл",
    #     filter={"role": "Driver", "active": True}
    # )
    # print("Список пользователей:", users)
    #
    # # 📌 Создание водителя без персональных данных
    # new_user_id = await client.create_user(
    #     uuid="62f2e267-4398-4ea2-b02e-6e88b81b0958",
    #     mobile="7999999999"
    # )
    # print("Создан пользователь:", new_user_id)
    #
    # # 📌 Прикрепление договоров к пользователю
    # await client.attach_contracts(
    #     user_id=new_user_id,
    #     contracts=[
    #         {"sid": "1-380B94P", "template_id": "1-3BE470B", "use_mpc": True},
    #         {"sid": "1-37PYW2D", "template_id": None},
    #     ]
    # )
    # print("Договоры прикреплены")
    #
    # # 📌 Открепление договоров от пользователя
    # await client.detach_contracts(
    #     user_id=new_user_id,
    #     contract_ids=["1-380B94P", "1-37PYW2D"]
    # )
    # print("Договоры откреплены")
    #
    # # 📌 Прикрепление карты к пользователю
    # await client.attach_card(user_id=new_user_id, card_id="5050505")
    # print("Карта прикреплена")
    #
    # # 📌 Открепление карты от пользователя
    # await client.detach_card(user_id=new_user_id, card_id="5050505")
    # print("Карта откреплена")
    #
    # # 📌 Удаление пользователя
    # await client.delete_user(user_id=new_user_id)
    # print("Пользователь удалён")
    #
    # # 📌 Выход из системы
    # await client.logoff()
    # print("Сессия завершена")


    # # ---------- Шаблоны ----------
    # templates = await client.get_templates(contract_id="1-380B94P")
    # print("Шаблоны:", templates)
    #
    # new_template = await client.create_template("1-2SY777F", "Wallet", "Demo Template")
    # print("Создан:", new_template)
    #
    # updated_template = await client.update_template(new_template.id, "1-2SY777F", "Limit", "Updated Demo")
    # print("Обновлён:", updated_template)
    #
    # # ---------- Лимиты ----------
    # limits = await client.get_template_limits(new_template.id)
    # print("Лимиты:", limits)
    #
    # new_limit = await client.create_template_limit(new_template.id, {
    #     "contract_id": "1-2SY777F",
    #     "amount": {"unit": "LIT", "value": 100},
    #     "time": {"type": 3, "number": 1}
    # })
    # print("Создан лимит:", new_limit)
    #
    # #---------- Ограничители ----------
    # restrictions = await client.get_template_restrictions(new_template.id)
    # print("Ограничители:", restrictions)
    #
    # new_restriction = await client.create_template_restriction(new_template.id, {
    #     "contract_id": "1-2SY777F",
    #     "product_type": "1-276PF01",
    #     "restriction_type": 1
    # })
    # print("Создан ограничитель:", new_restriction)
    #
    # # ---------- Геоограничители ----------
    # geos = await client.get_template_georestrictions(new_template.id)
    # print("Геоограничители:", geos)
    #
    # new_geo = await client.create_template_georestriction(new_template.id, {
    #     "contract_id": "1-2SY777F",
    #     "country": "RUS",
    #     "region": "45",
    #     "restriction_type": 1
    # })
    # print("Создан геоограничитель:", new_geo)
    #
    # #---------- Удаление ----------
    # await client.delete_template_georestriction(new_template.id, new_geo.id)
    # await client.delete_template_restriction(new_template.id, new_restriction.id)
    # await client.delete_template_limit(new_template.id, new_limit.id)
    # await client.delete_template(new_template.id)
    # print("Все сущности удалены")

    # # 1. Выпуск ВК по user_id (старый метод)
    # card = await client.create_virtual_card(user_id="1-2Q468ZB")
    # print("Создана виртуальная карта:", card.data)
    #
    # # 2. Выпуск ВК с типом карты (новый метод)
    # card2 = await client.release_virtual_card(type_="wallet")
    # print("Выпущена ВК:", card2.data)
    #
    # # 3. Выпуск ВК с шаблоном и пользователем
    # card3 = await client.release_virtual_card(template_id="1-3BDZMRJ", user_id="1-2Q468ZB")
    # print("ВК по шаблону:", card3.data)
    #
    # # 4. Удаление МПК
    # result = await client.delete_mpc(card_id=card.data.id)
    # print("Удаление МПК:", result)
    #
    # # 5. Сброс счетчиков МПК
    # reset_result = await client.reset_mpc(card_id=card.data.id, type_="ResetCounterCode")
    # print("Сброс счетчиков:", reset_result)
    # 1. Получение финальных цен на товары
    # prices = await client.calculate_prices(
    #     card_id="989666",
    #     poi_id="366038",
    #     goods=["00000000000007", "00000000000009"]
    # )
    # print("Финальные цены:")
    # for item in prices.data.goods:
    #     print(f"- {item.code}: {item.price} руб.")
    #
    # # 2. Проверка возможности покупки
    # can_buy = await client.check_purchase(
    #     card_id="989666",
    #     poi_id="366038",
    #     goods=[
    #         {"code": "00000000000007", "quantity": 1, "price": 1.5},
    #         {"code": "00000000000009", "quantity": 1, "price": 1.5},
    #     ]
    # )
    # print("Можно ли совершить транзакцию:", can_buy.data)

    # # 1. Получение списка АЗС
    # azs = await client.get_azs(filter={"countries": ["RUS"]}, page=1, on_page=5)
    # print(f"Найдено АЗС: {azs.total_count}")
    # for station in azs.result:
    #     print(f"- {station.id}: {station.name} ({station.address})")
    #
    # # 2. Получение фильтров для АЗС
    # filters = await client.get_azs_filters()
    # print("Доступные фильтры для АЗС:", filters.filters.keys())
    #
    # # 3. Получение справочника единиц измерения
    # dictionary = await client.get_dictionary("Unit")
    # print(f"Элементов в справочнике: {dictionary.total_count}")
    # for item in dictionary.result:
    #     print(f"- {item.id}: {item.value}")

if __name__ == "__main__":
    asyncio.run(main())
