from ..decorators import api_method
from ..models.virtual_cards import VirtualCardResponse


class VirtualCardsMixin:
    @api_method(require_session=True, default_version="v2")
    async def create_virtual_card(
            self,
            user_id: str,
            api_version: str = "v2",
    ) -> VirtualCardResponse:
        """Выпуск виртуальной карты (старый метод)"""
        payload = {"user_id": user_id}
        data = await self._request(
            "post",
            "cards",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return VirtualCardResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def release_virtual_card(
            self,
            *,
            type_: str | None = None,
            template_id: str | None = None,
            user_id: str | None = None,
            api_version: str = "v2",
    ) -> VirtualCardResponse:
        """Выпуск виртуальной карты (новый метод /release)"""
        payload = {}
        if type_:
            payload["type"] = type_
        if template_id:
            payload["template_id"] = template_id
        if user_id:
            payload["user_id"] = user_id

        data = await self._request(
            "post",
            "cards/release",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return VirtualCardResponse(**data)

    @api_method(require_session=True, default_version="v2")
    async def delete_mpc(
            self,
            card_id: str,
            api_version: str = "v2",
    ) -> bool:
        """Удаление МПК"""
        data = await self._request(
            "post",
            f"cards/{card_id}/deleteMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return data.get("data", False)

    @api_method(require_session=True, default_version="v2")
    async def reset_mpc(
            self,
            card_id: str,
            type_: str,
            api_version: str = "v2",
    ) -> bool:
        """Сброс счетчиков МПК"""
        payload = {"type": type_}
        data = await self._request(
            "post",
            f"cards/{card_id}/resetMPC",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return data.get("data", False)
