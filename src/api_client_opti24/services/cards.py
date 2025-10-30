from typing import List, Optional
from ..decorators import api_method
from ..models.cards import (
    CardsListResponse,
    CardGroupResponse,
    CardDriversResponse,
    CardDetailResponse,
    IDListResponse,
    BoolResponse,CardsV2Response
)
from ..logger import logger


class CardsMixin:
    """Методы работы с топливными картами."""

    # --- Список карт (v1) ---
    @api_method(require_session=True, default_version="v1")
    async def get_cards_v1(
            self, contract_id: str, cache: bool = True, api_version: str = "v1"
    ) -> CardsListResponse:
        """Список топливных карт (Процессинг).
        :param contract_id: Идентификатор договора
        :param cache: Кеш карт. false или не задан - данные берутся по прямому запросу из процессинга.
        :return: Объект CardsListResponse с данными о картах

    """
        params = {"contract_id": contract_id, "cache": str(cache).lower()}
        logger.info("Запрос списка карт (v1) с параметрами: %s", params)
        data = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        return CardsListResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def get_cards_v2(
            self,
            contract_id: str,
            sort: str = "-id",
            q: str | None = None,
            status: str | None = None,
            carrier: str | None = None,
            platon: bool | None = None,
            avtodor: bool | None = None,
            users: bool | None = None,
            group_id: str | None = None,
            page: int = None,
            onpage: int = None,
            api_version: str = "v2",
    ) -> CardsV2Response:
        """
        Получение списка карт договора (v2).
        :param contract_id: Идентификатор договора
        :param sort: Поле сортировки (по умолчанию '-id')
        :param q: Поисковый запрос (например, часть номера карты)
        :param status: Фильтр по статусу карты (Active, Locked и т.д.)
        :param carrier: Тип носителя карты ('Plastic', 'Virtual Card')
        :param platon: Фильтр по поддержке Платон
        :param avtodor: Фильтр по поддержке Автодор
        :param users: Фильтр по наличию пользователей
        :param group_id: Идентификатор группы карт (опционально)
        :param page: Номер страницы (по умолчанию 1)
        :param onpage: Количество элементов на странице (по умолчанию 10)
        :return: Объект CardsV2Response с данными о картах
        """
        params = {
            "contract_id": contract_id,
            "sort": sort,
            "q": q,
            "status": status,
            "carrier": carrier,
            "platon": platon,
            "avtodor": avtodor,
            "users": users,
            "group_id": group_id,
            "page": page,
            "onpage": onpage,
        }

        # Исключаем None, чтобы не отправлять пустые параметры
        filtered_params = {k: v for k, v in params.items() if v is not None}

        response = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=filtered_params,
        )

        # Возвращаем корректно типизированный объект
        return CardsV2Response(**response["data"])


    # --- Список карт по группе ---
    @api_method(require_session=True, default_version="v1")
    async def get_cards_by_group(
            self, contract_id: str, group_id: str, api_version: str = "v1"
    ) -> CardGroupResponse:
        """Получение списка топливных карт по группе карт."""
        params = {"contract_id": contract_id, "group_id": group_id}
        logger.info("Запрос списка карт по группе: %s", params)
        data = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return CardGroupResponse(**data)

    # --- Водители по карте ---
    @api_method(require_session=True, default_version="v2")
    async def get_card_drivers(
            self, card_id: str, contract_id: str, api_version: str = "v2"
    ) -> CardDriversResponse:
        """Получение списка водителей по карте."""
        logger.info("Запрос водителей по карте %s для договора %s", card_id, contract_id)
        data = await self._request(
            "get",
            f"cards/{card_id}/drivers",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"contract_id": contract_id},
        )
        return CardDriversResponse(**data)

    # --- Детальная информация по карте ---
    @api_method(require_session=True, default_version="v1")
    async def get_card_detail(
            self, contract_id: str, card_id: str, api_version: str = "v1"
    ) -> CardDetailResponse:
        """Получение детальной информации по карте."""
        params = {"contract_id": contract_id, "card_id": card_id}
        logger.info("Запрос детальной информации по карте: %s", params)
        data = await self._request(
            "get",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return CardDetailResponse(**data)

    # --- Блокировка / разблокировка карты ---
    @api_method(require_session=True, default_version="v1")
    async def block_card(
            self, contract_id: str, card_ids: List[str], block: bool = True, api_version: str = "v1"
    ) -> IDListResponse:
        """Блокировка или разблокировка топливных карт.
        :param contract_id: Идентификатор договора
        :param card_ids: Список идентификаторов карт
        :param block: True для блокировки, False для разблокировки
        return: Объект IDListResponse с результатом операции"""

        payload = {"contract_id": contract_id, "card_id": card_ids, "block": str(block).lower()}
        if block == True:
            logger.info("Блокировка карт: %s", payload)
        else:
            logger.info("Разблокировка карт: %s", payload)

        data = await self._request(
            "post",
            "blockCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return IDListResponse(**data)

    # --- Установка комментария ---
    @api_method(require_session=True, default_version="v1")
    async def set_card_comment(
            self, card_id: str, contract_id: str, comment: str, api_version: str = "v1"
    ) -> BoolResponse:
        """Установить комментарий на топливную карту."""
        payload = {"card_id": card_id, "contract_id": contract_id, "comment": comment}
        logger.info("Установка комментария на карту: %s", payload)
        data = await self._request(
            "post",
            "setCardComment",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return BoolResponse(**data)

    # --- Запрос одноразового кода для сброса PIN ---
    @api_method(require_session=True, default_version="v2")
    async def verify_pin(self, card_id: str, contract_id: str, api_version: str = "v2") -> BoolResponse:
        """ Запрос одноразового кода для сброса PIN карты.
        Данный метод позволяет инициировать запрос на сброс попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
        Вам будет отправлено письмо с кодом подтверждения на почту, которая привязана к вашей учетной записи.
        Данный код нужно ввести в метод resetPIN для завершения операции сброса попыток.
        """
        logger.info("Запрос(verifyPIN) одноразового кода для сброса PIN карты %s", card_id)
        data = await self._request(
            "post",
            f"cards/{card_id}/verifyPIN",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"contract_id": contract_id},
        )
        return BoolResponse(**data)

    # --- Подтверждение сброса PIN ---
    @api_method(require_session=True, default_version="v2")
    async def reset_pin(
            self, card_id: str, contract_id: str, code: str, api_version: str = "v2"
    ) -> BoolResponse:
        """ Подтверждение сброса PIN карты.
        Данный метод позволяет завершить операцию со сбросом попыток некорректного ввода PIN – кода пластиковой топливной карты на АЗС.
        Код подтверждения будет отправлен на почту, которая привязана к вашей учетной записи.
        """
        payload = {"contract_id": contract_id, "code": code}
        logger.info("Запрос resetPIN для карты %s", card_id)
        data = await self._request(
            "post",
            f"cards/{card_id}/resetPIN",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return BoolResponse(**data)
