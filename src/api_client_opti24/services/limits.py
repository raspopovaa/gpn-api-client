import json
from typing import Optional, List, Dict
from ..decorators import api_method
from ..logger import logger
from src.api_client_opti24.models.limits import (
    LimitsResponse,
    SetLimitResponse,
    RemoveLimitResponse,
)


class LimitsMixin:
    """
    Методы для работы с продуктовыми лимитами (v1).

    Поддерживаются:
      • Получение списка лимитов (по договору, карте или группе)
      • Установка / изменение лимита
      • Удаление лимита
    """

    # ------------------- GET /limit -------------------

    @api_method(require_session=True, default_version="v1")
    async def get_limits(
            self,
            *,
            contract_id: str,
            card_id: Optional[str] = None,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> LimitsResponse:
        """
        Получить список продуктовых лимитов по договору, карте или группе карт.

        :param contract_id: ID договора
        :param card_id: ID карты (опционально)
        :param group_id: ID группы карт (опционально)
        :param api_version: версия API (по умолчанию v1)
        """
        if not contract_id:
            raise ValueError("contract_id обязателен для get_limits")

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

        logger.debug(f"GET /limit params={params} -> {raw}")
        return LimitsResponse(**raw)

    # ------------------- POST /setLimit -------------------

    @api_method(require_session=True, default_version="v1")
    async def set_limit(
            self,
            *,
            limits: List[Dict],
            api_version: str = "v1",
    ) -> SetLimitResponse:
        """
        Для изменения уже ранее созданного лимита, требуется передавать в запросе его ID.
        Для договора нельзя выставить продуктовый лимит, можно для карты или группы карт.
        :param limits: список лимитов в виде словарей (см. документацию API)
        """
        if not limits:
            raise ValueError("Не переданы данные лимита (limits)")

        body = {"limit": json.dumps(limits, ensure_ascii=False)}

        raw = await self._request(
            "post",
            "setLimit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        logger.info(f"POST /setLimit body={body} -> {raw}")
        return SetLimitResponse(**raw)

    # ------------------- POST /removeLimit -------------------

    @api_method(require_session=True, default_version="v1")
    async def remove_limit(
            self,
            *,
            contract_id: str,
            limit_id: str,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> RemoveLimitResponse:
        """
        Удалить продуктовый лимит по карте или группе карт.
        Если ID группы карты не передано, то будет удален лимит по карте.
         Если передан ID группы карт, то будет удален лимит по группе карт
        :param contract_id: ID договора
        :param limit_id: ID лимита
        :param group_id: ID группы карт (опционально)
        """
        if not contract_id:
            raise ValueError("contract_id обязателен для remove_limit")
        if not limit_id:
            raise ValueError("limit_id обязателен для remove_limit")

        body = {"limit_id": limit_id, "contract_id": contract_id}
        if group_id:
            body["group_id"] = group_id

        raw = await self._request(
            "post",
            "removeLimit",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        logger.info(f"POST /removeLimit body={body} -> {raw}")
        return RemoveLimitResponse(**raw)
