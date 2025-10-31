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
    print("=== CONTRACT ===")
    contract_data = await client.get_contract_data(client.contract_id)
    print(contract_data.managerData.first_name)
    print("=== PAYMENTS ===")
    payments = await client.get_payments(client.contract_id)
    print(payments.data.result[0].id)
    # print("=== DOCUMENTS ===")
    # list_documents = await client.get_documents("2019-01-01", "2025-01-01")
    # print(list_documents.status)
    # #Заказ документов на почту
    # print(json.dumps(await client.order_documents_email(
    #     ids=["6fffd550-b55f-11e9-8123-005056a969a3","27a19fb4-cdd0-11e9-8127-005056a969a3"],
    #     fmt="pdf",
    #     emails=["andrew.raspopov@yandex.ru"]
    # ), indent=2, ensure_ascii=False))
    print("=== ORDER CARDS ===")
    order_cards = await client.order_cards(count=5, office_id="1-13HS")
    print(order_cards.data)
    # print("=== ORDER INVOICE ===")
    # invoice = await client.order_invoice(amount=50000, email="andrew.raspopov@yandex.ru")
    # print(invoice)

    print("=== INVOICES ===")
    list_invoices = await client.get_invoices()
    print(list_invoices.data.result[0].id,)
if __name__ == "__main__":
    asyncio.run(main())