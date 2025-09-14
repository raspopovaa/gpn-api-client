import logging
from datetime import datetime

from ..decorators import api_method
from ..utils import hash_password
from apiclientopti24.config import LOG_LEVEL, LOGGER_FILE
log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
logging.basicConfig(
    level=log_level,
    filename=LOGGER_FILE,
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("auth")


class AuthMixin:
    # @api_method(require_session=False, default_version="v1")
 #    async def auth_user(self, api_version: str = "v1") -> dict:
 #        '''Метод используется для авторизации в системе через API.
 # При выполнении запроса пользователь получает идентификатор активной сессии,
 # который используется во всех последующих запросах для возможности их выполнения.
 # Суть метода заключается в том же, что и авторизация в ЛК (т.е. получение прав на работу в интерфейсе).'''
 #        payload = {"login": self.login, "password": hash_password(self.password)}
 #        data = await self._request("post", "authUser", api_version=api_version, headers=self._headers(), data=payload)
 #        self.session_id = data["data"]["session_id"]
 #        self.contract_id = data["data"]["contracts"][1]["id"]
 #        return data

    @api_method(require_session=True, default_version="v1")
    async def logoff(self, api_version: str = "v1") -> dict:
        '''Метод делает ранее полученную сессию (на этапе авторизации) неактивной.
        Другими словами, пользователь "выходит" из профиля (аналогично кнопке выхода в ЛК). '''
        return await self._request("get", "logoff", api_version=api_version, headers=self._headers(include_session=True))

    async def get_info(self)->dict:
        '''Получение статистических данных по вызовам всех методов.'''
        return await self._request(
            "get",
            "info",
            api_version="v1",
            headers=self._headers(include_session=True),
            params={"period": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  # можно указать день "2018-10-20"
        )

    @api_method(require_session=False, default_version="v1")
    async def auth_user(
            self,
            *,
            api_version: str = "v1",
            contract_id: str | None = None,
            contract_number: str | None = None,
    ) -> dict:
        """
        Авторизация пользователя.
        - Всегда сохраняет session_id
        - contract_id выбирается автоматически (первый в списке), либо можно указать вручную:
          * contract_id="1-2SY777F"
          * contract_number="НВ01509999"
        """
        payload = {
            "login": self.login,
            "password": hash_password(self.password)
        }

        data = await self._request(
            "post",
            "authUser",
            api_version=api_version,
            headers=self._headers(),
            data=payload
        )

        self.session_id = data["data"]["session_id"]

        # Автовыбор контракта (оставляем только id и number)
        contracts = [
            {"id": item["id"], "number": item["number"]}
            for item in data["data"].get("contracts", [])
        ]

        selected = None
        if contract_id:
            selected = next((c for c in contracts if c["id"] == contract_id), None)
        elif contract_number:
            selected = next((c for c in contracts if c["number"] == contract_number), None)
        elif contracts:
            selected = contracts[1]

        if selected:
            self.contract_id = selected["id"]
            # Логирование выбранного контракта
            logger.info(
                f"Выбран контракт: id={selected['id']}, number={selected['number']}"
            )
        else:
            logger.warning("Контракт не найден — contract_id не установлен")

        return data