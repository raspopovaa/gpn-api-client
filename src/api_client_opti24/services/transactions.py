from typing import Optional, Callable
from datetime import datetime

from ..logger import logger
from ..decorators import api_method
from .. import utils
from ..models.transactions import (
    TransactionsV1Response,
    TransactionsV2Response,
    TransactionDetailResponse,
    TransactionV1,
    TransactionItemV2,
)


class TransactionsMixin:
    """
    Методы для работы с транзакциями (v1 и v2).
    """

    # ---------------- Вспомогательный метод ---------------- #

    def _filter_and_sort(
            self,
            items: list,
            *,
            filter_fn: Optional[Callable] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> list:
        """
        Фильтрует и сортирует список транзакций.
        """
        result = items

        if filter_fn:
            result = list(filter(filter_fn, result))

        if sort_by:
            try:
                result.sort(key=lambda x: getattr(x, sort_by, None), reverse=reverse)
            except Exception as e:
                logger.warning(f"Ошибка сортировки по '{sort_by}': {e}")

        return result

    # ---------------- v1: Транзакции ---------------- #

    @api_method(require_session=True, default_version="v1")
    async def get_transactions_v1(
            self,
            *,
            contract_id: str,
            card_id: Optional[str] = None,
            count: int = 20,
            api_version: str = "v1",
            filter_fn: Optional[Callable[[TransactionV1], bool]] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> TransactionsV1Response:
        """
        Получение списка последних транзакций по договору или карте (v1).

        :param contract_id: Идентификатор договора
        :param card_id: Идентификатор карты (опционально)
        :param count: Количество транзакций (по умолчанию 20)
        :param filter_fn: Функция для фильтрации списка
        :param sort_by: Поле для сортировки
        :param reverse: Обратный порядок сортировки
        """
        params = {"contract_id": contract_id, "count": count}
        if card_id:
            params["card_id"] = card_id

        raw = await self._request(
            "get",
            "transactions",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        tx_response = TransactionsV1Response(**raw)
        tx_response.data.result = self._filter_and_sort(
            tx_response.data.result, filter_fn=filter_fn, sort_by=sort_by, reverse=reverse
        )

        return tx_response

    # ---------------- v2: Транзакции по договору ---------------- #

    @api_method(require_session=True, default_version="v2")
    async def get_transactions_v2(
            self,
            *,
            contract_id: str,
            date_from: str,
            date_to: str,
            page_limit: int = 100,
            page_offset: int = 0,
            api_version: str = "v2",
            filter_fn: Optional[Callable[[TransactionItemV2], bool]] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> TransactionsV2Response:
        """
        Получение списка транзакций по договору (v2).

        :param contract_id: Идентификатор договора
        :param date_from: Начало периода (YYYY-MM-DD)
        :param date_to: Конец периода (YYYY-MM-DD)
        :param page_limit: Количество записей на странице
        :param page_offset: Смещение страницы
        """
        utils.validate_month_span(date_from, date_to)

        params = {
            "contract_id": contract_id,
            "date_from": date_from,
            "date_to": date_to,
            "page_limit": page_limit,
            "page_offset": page_offset,
        }

        raw = await self._request(
            "get",
            "transactions",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        tx_response = TransactionsV2Response(**raw)
        tx_response.data.result = self._filter_and_sort(
            tx_response.data.result, filter_fn=filter_fn, sort_by=sort_by, reverse=reverse
        )

        return tx_response

    # ---------------- v2: Транзакции по карте ---------------- #

    @api_method(require_session=True, default_version="v2")
    async def get_card_transactions_v2(
            self,
            *,
            card_id: str,
            contract_id: Optional[str] = None,
            date_from: str,
            date_to: str,
            page_limit: int = 100,
            page_offset: int = 0,
            api_version: str = "v2",
            filter_fn: Optional[Callable[[TransactionItemV2], bool]] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> TransactionsV2Response:
        """
        Получение списка транзакций по карте (v2).

        :param card_id: Идентификатор карты
        :param contract_id: Идентификатор договора (если не указан, берётся из сессии)
        :param date_from: Начало периода (YYYY-MM-DD)
        :param date_to: Конец периода (YYYY-MM-DD)
        """
        utils.validate_month_span(date_from, date_to)

        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для get_card_transactions_v2")

        params = {
            "contract_id": cid,
            "date_from": date_from,
            "date_to": date_to,
            "page_limit": page_limit,
            "page_offset": page_offset,
        }

        raw = await self._request(
            "get",
            f"cards/{card_id}/transactions",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        tx_response = TransactionsV2Response(**raw)
        tx_response.data.result = self._filter_and_sort(
            tx_response.data.result, filter_fn=filter_fn, sort_by=sort_by, reverse=reverse
        )

        return tx_response

    # ---------------- v2: Детали транзакции ---------------- #

    @api_method(require_session=True, default_version="v2")
    async def get_transaction_detail(
            self,
            *,
            transaction_id: str,
            contract_id: Optional[str] = None,
            api_version: str = "v2",
    ) -> TransactionDetailResponse:
        """
        Получение детальной информации по транзакции (v2).

        :param transaction_id: ID транзакции
        :param contract_id: Идентификатор договора
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для get_transaction_detail")

        raw = await self._request(
            "get",
            f"transactions/{transaction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"contract_id": cid},
        )

        return TransactionDetailResponse(**raw)
