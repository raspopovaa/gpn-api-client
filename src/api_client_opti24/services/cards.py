import json
import logging
from typing import Optional

from ..decorators import api_method
from ..logger import logger

class CardsMixin:
    @api_method(require_session=True, default_version="v2")
    async def get_contract_cards_v2(
            self,
            sort: str = "-id",
            q: str | None = None,
            status: str | None = None,
            carrier: str | None = None,
            platon: bool | None = None,
            avtodor: bool | None = None,
            users: bool | None = None,
            page: int = 1,
            onpage: int = 10,
            api_version: str = "v2",
    ) -> dict:
        """
        Новый метод получения списка карт с данными
        (например: название группы карт, статус, комментарий, существует ли МПК).
        """
        params: dict[str, str] = {
            "sort": sort,
            "page": str(page),
            "onpage": str(onpage),
        }

        if q:
            params["q"] = q
        if status:
            params["status"] = status
        if carrier:
            params["carrier"] = carrier
        if platon is not None:
            params["platon"] = str(platon).lower()
        if avtodor is not None:
            params["avtodor"] = str(avtodor).lower()
        if users is not None:
            params["users"] = str(users).lower()

        return await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params
        )

    @api_method(require_session=True, default_version="v1")
    async def getProcessingCards(self, cache: Optional[bool] = None, api_version: str = "v1") -> dict:
        """Получение списка карт с данными
        (например: комментарий, дата последнего использования,
        минимальное время меду транзакциями, тип продукта - лимитная или ЭК)."""
        params = {}
        if cache is not None:
            params["cache"] = str(cache).lower()

        return await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params
        )

    @api_method(require_session=True, default_version="v1")
    async def getGroupCards(self, contract_id: str, group_id: str, api_version: str = "v1") -> dict:
        """Получение списка по группе карт."""
        body = {
            "contract_id": contract_id or self.contract_id,
            "group_id": group_id
        }

        return await self._request(
            "GET",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body
        )

    @api_method(require_session=True, default_version="v1")
    async def set_card_group(
            self,
            *,
            name: str,
            contract_id: str | None = None,
            group_id: str | None = None,
            api_version: str = "v1",
    ) -> dict:
        """
        Создание или изменение группы карт.
        - Если group_id не указан → создаётся новая группа
        - Если group_id указан → обновляется существующая
        """
        body = {"name": name, "contract_id": contract_id or self.contract_id}
        if not body["contract_id"]:
            raise ValueError("contract_id обязателен для set_card_group")

        if group_id:
            body["id"] = group_id

        return await self._request(
            "post",
            "setCardGroup",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v2")
    async def getCardDrivers(self, card_id: str, api_version: str = "v2") -> dict:
        """Получение списка водителей."""
        return await self._request(
            "GET",
            f"cards/{card_id}/drivers",
            api_version=api_version,
            headers=self._headers(include_session=True)
        )
    @api_method(require_session=True, default_version="v1")
    async def getCardDetails(self, card_id: str, api_version: str = "v1") -> dict:
        """Получение детальной информации по карте (дата выпуска, тип продукта, тип карты и пр.)."""
        params = {"contract_id": self.contract_id,
                  "card_id": card_id}
        return await self._request(
            "GET",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params
        )
    @api_method(require_session=True, default_version="v1")
    async def block_card(
            self,
            *,
            card_ids: list[str],
            block: bool = True,
            contract_id: str | None = None,
            api_version: str = "v1",
    ) -> dict:
        """
        Блокировка или разблокировка карт.
        - card_ids: список ID карт
        - block: True = блокировка, False = разблокировка
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для block_card")

        body = {
            "contract_id": cid,
            # В API card_id передаётся как строка JSON-массива
            "card_id": json.dumps(card_ids, ensure_ascii=False),
            "block": str(block).lower(),
        }

        return await self._request(
            "post",
            "blockCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v1")
    async def set_card_comment(
            self,
            *,
            card_id: str,
            comment: str,
            contract_id: str | None = None,
            api_version: str = "v1",
    ) -> dict:
        """
        Установить комментарий на карту (v1).
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для set_card_comment")

        body = {
            "card_id": card_id,
            "contract_id": cid,
            "comment": comment,
        }

        return await self._request(
            "post",
            "setCardComment",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v2")
    async def request_reset_pin(
            self,
            *,
            card_id: str,
            contract_id: str | None = None,
            api_version: str = "v2",
    ) -> dict:
        """
        Запрос одноразового кода для сброса попыток ввода PIN карты (v2).
        После вызова на email пользователя придёт код, который нужно
        подтвердить методом resetPIN.
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для request_reset_pin")

        body = {"contract_id": cid}

        return await self._request(
            "post",
            f"cards/{card_id}/verifyPIN",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
    @api_method(require_session=True, default_version="v2")
    async def reset_pin(
            self,
            *,
            card_id: str,
            code: str,
            contract_id: str | None = None,
            api_version: str = "v2",
    ) -> dict:
        """
        Подтверждение сброса PIN карты (v2).
        Завершает операцию сброса после вызова request_reset_pin().
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для reset_pin")

        body = {"contract_id": cid, "code": code}

        return await self._request(
            "post",
            f"cards/{card_id}/resetPIN",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )