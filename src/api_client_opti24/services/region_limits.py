from typing import Optional, List, Dict
from ..decorators import api_method
from src.api_client_opti24.models.region_limits import RegionLimitList, RemoveRegionLimit, RegionLimitResponse


class RegionLimitsMixin:
    """
    Методы для работы с региональными лимитами (v1).
    """

    @api_method(require_session=True, default_version="v1")
    async def get_region_limits(
            self,
            *,
            contract_id: str,
            card_id: Optional[str] = None,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> RegionLimitList:
        """
        Получение списка региональных лимитов по договору, карте или группе карт.
        """
        params = {"contract_id": contract_id}
        if card_id:
            params["card_id"] = card_id
        if group_id:
            params["group_id"] = group_id

        raw = await self._request(
            "get",
            "regionLimit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return RegionLimitResponse(**raw)

    @api_method(require_session=True, default_version="v1")
    async def set_region_limit(
            self,
            *,
            region_limits: List[Dict],
            api_version: str = "v1",
    ) -> dict:
        """
        Установка/изменение регионального лимита по карте или группе карт.
        Для изменения лимита необходимо передавать его ID.
        """
        body = {"region_limit": str(region_limits).replace("'", '"')}

        return await self._request(
            "post",
            "setRegionLimit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v1")
    async def remove_region_limit(
            self,
            *,
            contract_id: str,
            regionlimit_id: str,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> dict:
        """
        Удаление регионального лимита по карте или группе карт.
        """
        body = {"regionlimit_id": regionlimit_id, "contract_id": contract_id}
        if group_id:
            body["group_id"] = group_id

        raw = await self._request(
            "post",
            "removeRegionLimit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
        return RemoveRegionLimit(**raw)
