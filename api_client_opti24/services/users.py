# src/api_client_opti24/services/users.py

from ..decorators import api_method
from ..logger import logger
from ..models.users import UsersListResponse, UserResponse


class UsersMixin:
    @api_method(require_session=True, default_version="v2")
    async def get_users(self, *, api_version: str = "v2", **params) -> UsersListResponse:
        """
        Список пользователей
        """
        logger.info("Вызов метода get_users с параметрами: %s", params)
        data = await self._request(
            "get",
            "users",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return UsersListResponse(**data["data"])

    @api_method(require_session=True, default_version="v2")
    async def create_user(self, *, api_version: str = "v2", **payload) -> str:
        """
        Создание водителя без персональных данных
        """
        logger.info("Создание пользователя: %s", payload)
        data = await self._request(
            "post",
            "users",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return data["data"]

    @api_method(require_session=True, default_version="v2")
    async def attach_contracts(self, user_id: str, *, api_version: str = "v2", contracts: list) -> bool:
        """
        Прикрепление договоров к пользователю
        """
        logger.info("Прикрепление договоров к пользователю %s: %s", user_id, contracts)
        data = await self._request(
            "post",
            f"users/{user_id}/attachContracts",
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=contracts,
        )
        return data["data"]

    @api_method(require_session=True, default_version="v2")
    async def detach_contracts(self, user_id: str, *, api_version: str = "v2", contracts: list) -> bool:
        """
        Открепление договоров от пользователя
        """
        logger.info("Открепление договоров от пользователя %s: %s", user_id, contracts)
        data = await self._request(
            "post",
            f"users/{user_id}/detachContracts",
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=contracts,
        )
        return data["data"]

    @api_method(require_session=True, default_version="v2")
    async def attach_card(self, user_id: str, card_id: str, *, api_version: str = "v2") -> bool:
        """
        Прикрепление карты к пользователю
        """
        logger.info("Прикрепление карты %s к пользователю %s", card_id, user_id)
        data = await self._request(
            "post",
            f"users/{user_id}/attachCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data={"card_id": card_id},
        )
        return data["data"]

    @api_method(require_session=True, default_version="v2")
    async def detach_card(self, user_id: str, card_id: str, *, api_version: str = "v2") -> bool:
        """
        Открепление карты от пользователя
        """
        logger.info("Открепление карты %s от пользователя %s", card_id, user_id)
        data = await self._request(
            "post",
            f"users/{user_id}/detachCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data={"card_id": card_id},
        )
        return data["data"]

    @api_method(require_session=True, default_version="v2")
    async def delete_user(self, user_id: str, *, api_version: str = "v2") -> bool:
        """
        Удаление пользователя
        """
        logger.info("Удаление пользователя %s", user_id)
        data = await self._request(
            "delete",
            f"users/{user_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return data["data"]
