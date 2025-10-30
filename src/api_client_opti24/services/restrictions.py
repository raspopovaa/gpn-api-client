from typing import Optional, List, Dict
import json
from ..decorators import api_method
from src.api_client_opti24.models.restrictions import (
    RestrictionGetResponse,
    RestrictionSetResponse,
    RestrictionRemoveResponse,
)
from ..logger import logger


class RestrictionsMixin:
    """
    Методы для работы с товарными ограничителями (v1).
    """

    # ---------------- Запрос ----------------
    @api_method(require_session=True, default_version="v1")
    async def get_restrictions(
            self,
            *,
            contract_id: str,
            card_id: Optional[str] = None,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> RestrictionGetResponse:
        """
        Получение списка товарных ограничителей по договору, карте или группе карт.
        """
        params = {"contract_id": contract_id}
        if card_id:
            params["card_id"] = card_id
        if group_id:
            params["group_id"] = group_id

        raw = await self._request(
            "get",
            "restriction",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

        logger.debug(f"GET /restriction response: {raw}")
        return RestrictionGetResponse(**raw)

    # ---------------- Установка ----------------
    @api_method(require_session=True, default_version="v1")
    async def set_restriction(
            self,
            *,
            restrictions: List[Dict],
            api_version: str = "v1",
    ) -> RestrictionSetResponse:
        """
        Установка или изменение товарного ограничителя по карте или группе карт.
        Для изменения ограничителя необходимо передавать его ID.
        """
        if not restrictions:
            raise ValueError("Список restrictions не может быть пустым")

        body = {"restriction": json.dumps(restrictions, ensure_ascii=False)}

        raw = await self._request(
            "post",
            "setRestriction",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        logger.debug(f"POST /setRestriction response: {raw}")
        return RestrictionSetResponse(**raw)

    # ---------------- Удаление ----------------
    @api_method(require_session=True, default_version="v1")
    async def remove_restriction(
            self,
            *,
            contract_id: str,
            restriction_id: str,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> RestrictionRemoveResponse:
        """
        Удаление товарного ограничителя по карте или группе карт.
        """
        body = {
            "restriction_id": restriction_id,
            "contract_id": contract_id,
        }
        if group_id:
            body["group_id"] = group_id

        raw = await self._request(
            "post",
            "removeRestriction",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        logger.debug(f"POST /removeRestriction response: {raw}")
        return RestrictionRemoveResponse(**raw)
