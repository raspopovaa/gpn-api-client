from typing import Optional, List, Dict
import json

from ..decorators import api_method
from api_client_opti24.models.card_group import (
    CardGroupListResponse,
    SetCardsToGroupResponse,
    RemoveCardGroupResponse,
    SetCardGroupResponse,
)


class CardGroupsMixin:
    """
    Методы для работы с группами карт (v1).
    """

    # -------------------------------
    # Получение списка групп карт
    # -------------------------------
    @api_method(require_session=True, default_version="v1")
    async def get_card_groups(
            self,
            *,
            contract_id: str,
            api_version: str = "v1",
    ) -> CardGroupListResponse:
        """
        Получить список групп карт по договору.
        """
        params = {"contract_id": contract_id}

        raw = await self._request(
            method="get",
            endpoint="cardGroups",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return CardGroupListResponse(**raw)

    # -------------------------------
    # Создание или изменение группы
    # -------------------------------
    @api_method(require_session=True, default_version="v1")
    async def set_card_group(
            self,
            *,
            contract_id: str,
            name: str,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> SetCardGroupResponse:
        """
        Создать новую или изменить существующую группу карт.

        Args:
            contract_id: Идентификатор договора.
            name: Название группы карт.
            group_id: (опционально) ID группы для изменения.
        """
        body = {"contract_id": contract_id, "name": name}
        if group_id:
            body["id"] = group_id

        raw = await self._request(
            method="post",
            endpoint="setCardGroup",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
        return SetCardGroupResponse(**raw)

    # -------------------------------
    # Добавление карт в группу
    # -------------------------------
    @api_method(require_session=True, default_version="v1")
    async def set_cards_to_group(
            self,
            *,
            contract_id: str,
            group_id: str,
            cards_list: List[Dict],
            api_version: str = "v1",
    ) -> SetCardsToGroupResponse:
        """
        Добавление карт в группу.

        Args:
            contract_id: Идентификатор договора.
            group_id: Идентификатор группы карт.
            cards_list: Список карт и действий, например:
                [{"id": "2728111", "type": "Attach"}, {"id": "2728112", "type": "Attach"}]
        """
        body = {
            "contract_id": contract_id,
            "group_id": group_id,
            "cards_list": json.dumps(cards_list),
        }

        raw = await self._request(
            method="post",
            endpoint="setCardsToGroup",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
        return SetCardsToGroupResponse(**raw)

    # -------------------------------
    # Удаление группы карт
    # -------------------------------
    @api_method(require_session=True, default_version="v1")
    async def remove_card_group(
            self,
            *,
            contract_id: str,
            group_id: str,
            api_version: str = "v1",
    ) -> RemoveCardGroupResponse:
        """
        Удалить группу карт по ID.

        Args:
            contract_id: Идентификатор договора.
            group_id: Идентификатор группы карт.
        """
        body = {"contract_id": contract_id, "group_id": group_id}

        raw = await self._request(
            method="post",
            endpoint="removeCardGroup",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
        return RemoveCardGroupResponse(**raw)
