from ..decorators import api_method
from ..models.final_prices import FinalPricesResponse, CheckPurchaseResponse
from typing import List


class FinalPricesMixin:
    @api_method(require_session=True, default_version="v2")
    async def calculate_prices(
            self,
            card_id: str,
            poi_id: str,
            goods: List[str],
            api_version: str = "v2",
    ) -> FinalPricesResponse:
        """Получение финальных цен на АЗС по карте"""
        payload = {
            "poi_id": poi_id,
            "goods": goods,
        }
        data = await self._request(
            "post",
            f"cards/{card_id}/calculatePrices",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return FinalPricesResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def check_purchase(
            self,
            card_id: str,
            poi_id: str,
            goods: List[dict],
            api_version: str = "v2",
    ) -> CheckPurchaseResponse:
        """Проверка возможности проведения транзакции"""
        payload = {
            "poi_id": poi_id,
            "goods": goods,
        }
        data = await self._request(
            "post",
            f"cards/{card_id}/checkPurchase",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return CheckPurchaseResponse(**data)
