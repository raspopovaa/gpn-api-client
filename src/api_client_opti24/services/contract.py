from typing import List
from ..decorators import api_method
from ..logger import logger
from ..models.contracts import (ContractResponse, PaymentsResponse,
                                DocumentsResponse, DocumentsOrderResponse,
                                OrderCardsResponse, InvoiceOrderResponse, InvoicesResponse
                                )


class ContractMixin:
    @api_method(require_session=True, default_version="v1")
    async def get_contract_data(self, contract_id: str, api_version: str = "v1") -> ContractResponse:
        """Получение информации о контракте."""
        params = {"contract_id": contract_id}
        data = await self._request(
            "get",
            "getPartContractData",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return ContractResponse(**data["data"])

    @api_method(require_session=True, default_version="v1")
    async def get_payments(self, contract_id: str, api_version: str = "v1") -> dict:
        """Получение данных о платежах по контракту."""
        params = {"contract_id": contract_id}
        data = await self._request(
            "get",
            "getPayments",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return PaymentsResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def get_documents(
            self, date_start: str, date_end: str, api_version: str = "v2", page: int = 1, on_page: int = 10
    ) -> dict:
        """Получение списка первичных документов (номер документа, дата, сумма, НДС, номер договора и пр.)."""
        params = {"date_start": date_start, "date_end": date_end, "page": page, "on_page": on_page}
        data =  await self._request(
            "get",
            "documents",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return DocumentsResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def order_documents_email(
            self, ids: List[str], fmt: str, emails: List[str], api_version: str = "v2"
    ) -> dict:
        """Заказ первичных документов по ID документа на указанные email – адреса (до 5 адресов)."""
        payload = {"id": ids, "format": fmt, "emails": emails}
        logger.debug(f"Заказ документов: {payload}")
        data = await self._request(
            "post",
            "documents",
            api_version=api_version,
            headers=self._headers(include_session=True, content_type_json=True),
            json=payload,
        )
        return DocumentsOrderResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def order_cards(self, count: int, office_id: str, api_version: str = "v2") -> dict:
        """Заказ необходимого количества топливных карт в определенном офисе продаж."""
        payload = {"count": count, "office_id": office_id}
        logger.debug(f"Заказ карт: {payload}")
        data =  await self._request(
            "post",
            "orderCards",
            api_version=api_version,
            headers=self._headers(include_session=True, content_type_json=True),
            json=payload,
        )
        return OrderCardsResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def order_invoice(self, amount: float, email: str, api_version: str = "v2") -> dict:
        """Заказ счёта на оплату."""
        payload = {"sum": amount, "email": email}
        logger.debug(f"Заказ счёта: {payload}")
        data =  await self._request(
            "post",
            "invoice",
            api_version=api_version,
            headers=self._headers(include_session=True, content_type_json=True),
            json=payload,
        )
        return InvoiceOrderResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def get_invoices(self, api_version: str = "v2") -> dict:
        """Получение списка счетов на оплату."""
        data =  await self._request(
            "get",
            "invoices",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return InvoicesResponse(**data)
