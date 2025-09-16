import logging
from typing import Any, Dict, Optional
from ..logger import logger

class InviteMixin:

    async def list(
            self,
            role: Optional[str] = None,
            user_id: Optional[str] = None,
            sort: Optional[str] = None,
            status: Optional[str] = None,
            q: Optional[str] = None,
            page: Optional[int] = None,
            on_page: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Список приглашений (GET /vip/v2/invites)"""
        params = {
            "role": role,
            "user_id": user_id,
            "sort": sort,
            "status": status,
            "q": q,
            "page": page,
            "on_page": on_page,
        }
        params = {k: v for k, v in params.items() if v is not None}

        #self.logger.info(f"Invites.list params={params}")
        return await self._request(
            "GET",
            "/vip/v2/invites",
            headers=self._headers(include_session=True),
            params=params,
        )

    async def create(self, data: Dict[str, Any], with_send: bool = True) -> Dict[str, Any]:
        """
        Создание приглашения.
        with_send=True → POST /vip/v2/invites
        with_send=False → POST /vip/v2/invites_free
        """
        url = "/vip/v2/invites" if with_send else "/vip/v2/invites_free"
        #self.logger.info(f"Invites.create with_send={with_send}, data={data}")
        return await self._request(
            "POST",
            url,
            headers=self._headers(include_session=True),
            json=data,
        )

    async def delete(self, invite_id: str) -> Dict[str, Any]:
        """Удалить приглашение (DELETE /vip/v2/invites/{invite_id})"""
        #self.logger.info(f"Invites.delete invite_id={invite_id}")
        return await self._request(
            "DELETE",
            f"/vip/v2/invites/{invite_id}",
            headers=self._headers(include_session=True),
        )

    async def resend(self, invite_id: str) -> Dict[str, Any]:
        """Повторная отправка приглашения (GET /vip/v2/invites/{invite_id}/send)"""
        #self.logger.info(f"Invites.resend invite_id={invite_id}")
        return await self._request(
            "GET",
            f"/vip/v2/invites/{invite_id}/send",
            headers=self._headers(include_session=True),
        )

    async def prolong(self, invite_id: str, with_send: bool = True) -> Dict[str, Any]:
        """
        Продлить приглашение.
        with_send=True → POST /vip/v2/invites/{invite_id}/prolong
        with_send=False → POST /vip/v2/invites/{invite_id}/prolong_free
        """
        path = "prolong" if with_send else "prolong_free"
        #self.logger.info(f"Invites.prolong invite_id={invite_id}, with_send={with_send}")
        return await self._request(
            "POST",
            f"/vip/v2/invites/{invite_id}/{path}",
            headers=self._headers(include_session=True),
        )

