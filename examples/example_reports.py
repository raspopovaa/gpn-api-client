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
    print("===АВТОРИЗАЦИЯ===")
    print(auth_response.data.contracts[0])

    print("=== СПИСОК ДОСТУПНЫХ ОТЧЁТОВ (v2) ===")
    reports = await client.get_reports()

    print(f"Всего доступно: {reports.total_count}")
    for report in reports.result:
        print(f"{report.id} - {report.name}")

    # print("=== ЗАКАЗ ОТЧЁТА НА EMAIL (v2) ===")
    # response = await client.order_report(
    #     report_id="tsc_transaction_protocol",
    #     format="xlsx",
    #     emails="test@test.com",
    #     params={
    #         "start_date": "2025-10-01",
    #         "end_date": "2025-11-01",
    #         "id_agreement": "1-2SY666F"
    #     }
    # )
    # print(response)

    # print("\n=== ЗАКАЗ ОТЧЁТА ПО ССЫЛКЕ (v2) ===")
    # response_link = await client.order_report(
    #     report_id="tsc_total_transaction_protocol",
    #     format="xlsx",
    #     params={
    #         "start_date": "2022-11-01",
    #         "end_date": "2022-12-01",
    #         "id_agreement": "1-2SY666F"
    #     }
    # )
    # print(response_link)



    print("=== СПИСОК ЗАКАЗАННЫХ ОТЧЁТОВ (v2) ===")
    jobs = await client.get_report_jobs()

    print(f"Всего заказано: {jobs.total_count}")
    for job in jobs.result:
        print(f"{job.date} | {job.report_name} | {job.job_id} | готов через: {job.available_after} сек")

    # print("=== СКАЧИВАНИЕ ФАЙЛА ОТЧЁТА (v2) ===")
    # job_id = "1-2FLFKAW"  # подставь актуальный ID
    # content = await client.download_report_file(job_id=job_id)
    #
    # with open("report_v2.xlsx", "wb") as f:
    #     f.write(content)
    #
    # print(f"Отчёт {job_id} успешно сохранён: report_v2.xlsx")
    #

    print("=== ЗАКАЗ ОТЧЁТА (v1) ===")
    response = await client.order_report_v1(
        contract_id="1-2SY666F",
        start="2022-11-01",
        end="2022-11-30",
        report_format="xlsx",
        email="mail@mail.ru"
    )
    print(response)

    # print("\n=== ЗАКАЗ ОТЧЁТА ПО СПИСКУ КАРТ (v1) ===")
    # response_cards = await client.order_report_v1(
    #     contract_id="1-2SY666F",
    #     start="2022-11-01",
    #     end="2022-11-30",
    #     report_format="pdf",
    #     cards_list=["7005830003470036", "7005830003470028"]
    # )
    # print(response_cards)

    print("=== СПИСОК ЗАКАЗАННЫХ ОТЧЁТОВ (v1) ===")
    jobs = await client.get_report_job_list_v1()
    print(f"Всего заказано отчётов: {len(jobs.jobs)}")
    print("Дата | Название отчёта | ID | Формат")
    print("-" * 50)
    for job in jobs.jobs:
        print(f"{job.date} | {job.report_name} | {job.job_id} | {job.report_format}")

#     print("=== СКАЧИВАНИЕ ФАЙЛА ОТЧЁТА (v1) ===")
#     job_id = "1-2FLFKAW"  # подставь свой ID
#     content = await client.download_report_file_v1(job_id=job_id)
#
#     with open("report_v1.xlsx", "wb") as f:
#         f.write(content)
#
#     print(f"Отчёт {job_id} сохранён: report_v1.xlsx")
#
#     print("\n=== СКАЧИВАНИЕ ZIP-ФАЙЛА (v1) ===")
#     zip_content = await client.download_report_file_v1(job_id=job_id, archive=True)
#
#     with open("report_v1.zip", "wb") as f:
#         f.write(zip_content)
#
# print("ZIP-архив отчёта успешно сохранён")


if __name__ == "__main__":
    asyncio.run(main())