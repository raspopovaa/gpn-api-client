from ..logger import logger

from typing import Optional, Callable
from ..decorators import api_method
from .. import utils
from src.api_client_opti24.models.transactions import TransactionList, Transaction


class TransactionsMixin:
    """
    Методы для работы с транзакциями (v1/v2).
    """

    # ---------------- helpers ----------------

    def _filter_and_sort(
            self,
            tx_list: TransactionList,
            *,
            filter_fn: Optional[Callable[[Transaction], bool]] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> TransactionList:
        """Применяет фильтрацию и сортировку к результатам."""
        result = tx_list.result

        # фильтрация
        if filter_fn:
            result = list(filter(filter_fn, result))

        # сортировка
        if sort_by:
            try:
                result.sort(key=lambda tx: getattr(tx, sort_by, None), reverse=reverse)
            except Exception:
                # если поле не найдено или некорректно
                pass

        return TransactionList(total_count=len(result), result=result)

    # ---------------- v1 ----------------

    @api_method(require_session=True, default_version="v1")
    async def get_transactions(
            self,
            *,
            contract_id: str,
            card_id: Optional[str] = None,
            count: int = 20,
            api_version: str = "v1",
            filter_fn: Optional[Callable[[Transaction], bool]] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> TransactionList:
        """Список последних транзакций по договору или карте (v1)."""
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
        tx_list = TransactionList(**raw.get("data", {}))
        return self._filter_and_sort(tx_list, filter_fn=filter_fn, sort_by=sort_by, reverse=reverse)

    # ---------------- v2 ----------------

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
            filter_fn: Optional[Callable[[Transaction], bool]] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> TransactionList:
        """Список транзакций по договору (v2)."""
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
        tx_list = TransactionList(**raw.get("data", {}))
        return self._filter_and_sort(tx_list, filter_fn=filter_fn, sort_by=sort_by, reverse=reverse)

    @api_method(require_session=True, default_version="v2")
    async def get_card_transactions(
            self,
            *,
            card_id: str,
            contract_id: Optional[str] = None,
            date_from: str,
            date_to: str,
            page_limit: int = 100,
            page_offset: int = 0,
            api_version: str = "v2",
            filter_fn: Optional[Callable[[Transaction], bool]] = None,
            sort_by: Optional[str] = None,
            reverse: bool = False,
    ) -> TransactionList:
        """Список транзакций по карте (v2)."""
        utils.validate_month_span(date_from, date_to)

        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для get_card_transactions")

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
        tx_list = TransactionList(**raw.get("data", {}))
        return self._filter_and_sort(tx_list, filter_fn=filter_fn, sort_by=sort_by, reverse=reverse)
