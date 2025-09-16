import logging
from typing import Dict, Any, List, Optional
from ..decorators import api_method
from ..logger import logger


class ContractMixin:
    @api_method(require_session=False, default_version="v1")
    async def get_contract_data(self, contract_id: str, api_version: str = "v1") -> Dict[str, Any]:
        """Получение информации о контракте."""
        params = {"contract_id": contract_id}
        return await self._request("get", "getPartContractData", api_version=api_version, headers=self._headers(include_session=True), params=params)

    @api_method(require_session=False, default_version="v1")
    async def get_payments(self, contract_id: str, api_version: str = "v1") -> Dict[str, Any]:
        """Получение данных о платежах по контракту."""
        params = {"contract_id": contract_id}
        return await self._request("get", "getPayments", api_version=api_version, headers=self._headers(include_session=True), params=params)

    @api_method(require_session=False, default_version="v2")
    async def getDocuments(self, date_start: str, date_end: str, api_version: str = "v1", page: int = 1, on_page: int = 10) -> Dict[str, Any]:
        """Получение списка первичных документов (номер документа, дата, сумма, НДС, номер договора и пр.)."""
        params = {"date_start": date_start, "date_end": date_end, "page": page, "on_page": on_page}
        return await self._request("get", "documents", api_version=api_version, headers=self._headers(include_session=True), params=params)

    @api_method(require_session=False, default_version="v2")
    async def orderDocumentsEmail(self, ids: List[str], fmt: str, emails: List[str], api_version) -> Dict[str, Any]:
        """Заказ первичных документов по ID документа на указанные email – адреса (до 5 адресов)."""
        body = {"id": ids, "format": fmt, "emails": emails}
        return await self._request("post", "documents", api_version=api_version, headers=self._headers(include_session=True, content_type_json=True), json=body)

    @api_method(require_session=False, default_version="v2")
    async def orderCards(self, count: int, office_id: str, api_version) -> Dict[str, Any]:
        """Заказ необходимого количества топливных карт в определенном офисе продаж.."""
        data = {"count": count, "office_id": office_id}
        return await self._request("post", "orderCards", api_version=api_version, headers=self._headers(include_session=True), data=data)

    @api_method(require_session=False, default_version="v2")
    async def orderInvoice(self, amount: float, email: str, api_version) -> Dict[str, Any]:
        """Заказ счёта на оплату."""
        data = {"sum": amount, "email": email}
        return await self._request("post", "invoice", api_version=api_version, headers=self._headers(include_session=True), data=data)

    @api_method(require_session=False, default_version="v2")
    async def getInvoices(self, api_version) -> Dict[str, Any]:
        """Получение списка счетов на оплату."""
        return await self._request("get", "invoices", api_version=api_version, headers=self._headers(include_session=True))

