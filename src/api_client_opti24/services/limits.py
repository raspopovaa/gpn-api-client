from typing import Optional, List, Dict
from ..decorators import api_method
from src.api_client_opti24.models.limits import LimitList
from ..logger import logger
class LimitsMixin:
    """
    Методы для работы с продуктовыми лимитами (v1).
    """

    @api_method(require_session=True, default_version="v1")
    async def get_limits(
            self,
            *,
            contract_id: str,
            card_id: Optional[str] = None,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> LimitList:
        """
        Получение списка продуктовых лимитов по договору, карте или группе карт.
        """
        params = {"contract_id": contract_id}
        if card_id:
            params["card_id"] = card_id
        if group_id:
            params["group_id"] = group_id

        raw = await self._request(
            "get",
            "limit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return LimitList(**raw.get("data", {}))

    @api_method(require_session=True, default_version="v1")
    async def set_limit(
            self,
            *,
            limits: List[Dict],
            api_version: str = "v1",
    ) -> dict:
        """
        Установка/изменение продуктового лимита по карте или группе карт.
        Для изменения лимита необходимо передавать его ID.
        """
        body = {"limit": str(limits).replace("'", '"')}

        return await self._request(
            "post",
            "setLimit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v1")
    async def remove_limit(
            self,
            *,
            contract_id: str,
            limit_id: str,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> dict:
        """
        Удаление продуктового лимита по карте или группе карт.
        """
        body = {"limit_id": limit_id, "contract_id": contract_id}
        if group_id:
            body["group_id"] = group_id

        return await self._request(
            "post",
            "removeLimit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
