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
    #auth_response = await client.auth_user()
    #Получение статистики
    info_response = await client.get_info()
    print("=== Cтатистика ===")
    print(info_response.data.client_info)
    print(info_response.data.methods)
    logoff_response = await client.logoff()
    print("=== LOGOFF ===")
    print(logoff_response)
if __name__ == "__main__":
        asyncio.run(main())