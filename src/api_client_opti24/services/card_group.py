from typing import Optional, List, Dict
from ..decorators import api_method
from src.api_client_opti24.models.card_group import CardGroupList


class CardGroupsMixin:
    """
    Методы для работы с группами карт (v1).
    """

    @api_method(require_session=True, default_version="v1")
    async def get_card_groups(
            self,
            *,
            contract_id: str,
            api_version: str = "v1",
    ) -> CardGroupList:
        """
        Получить список групп карт по договору.
        """
        params = {"contract_id": contract_id}

        raw = await self._request(
            "get",
            "cardGroups",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return CardGroupList(**raw.get("data", {}))

    @api_method(require_session=True, default_version="v1")
    async def set_card_group(
            self,
            *,
            contract_id: str,
            name: str,
            group_id: Optional[str] = None,
            api_version: str = "v1",
    ) -> dict:
        """
        Создать или изменить группу карт.
        """
        body = {"contract_id": contract_id, "name": name}
        if group_id:
            body["id"] = group_id

        return await self._request(
            "post",
            "setCardGroup",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v1")
    async def set_cards_to_group(
            self,
            *,
            contract_id: str,
            group_id: str,
            cards_list: List[Dict],
            api_version: str = "v1",
    ) -> dict:
        """
        Добавление карт в группу.
        cards_list = [{"id": "2728111", "type": "Attach"}, {"id": "2728112", "type": "Attach"}]
        """
        body = {
            "contract_id": contract_id,
            "group_id": group_id,
            "cards_list": str(cards_list).replace("'", '"'),
        }

        return await self._request(
            "post",
            "setCardsToGroup",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v1")
    async def remove_card_group(
            self,
            *,
            contract_id: str,
            group_id: str,
            api_version: str = "v1",
    ) -> dict:
        """
        Удалить группу карт.
        """
        body = {"contract_id": contract_id, "group_id": group_id}

        return await self._request(
            "post",
            "removeCardGroup",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
