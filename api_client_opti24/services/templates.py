from ..decorators import api_method
from ..logger import logger
from ..models.templates import (
    TemplateListResponse, TemplateResponse, DeleteTemplateResponse,
    TemplateLimitListResponse, TemplateRestrictionListResponse, TemplateGeoRestrictionListResponse
)


class TemplatesMixin:
    # ---------- CRUD шаблонов ----------
    @api_method(require_session=True, default_version="v2")
    async def get_templates(self, contract_id: str, api_version: str = "v2",) -> TemplateListResponse:
        """Получить список шаблонов ВК"""
        data = await self._request(
            "get", "vc/templates",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"contract_id": contract_id},
        )
        return TemplateListResponse(**data["data"])

    @api_method(require_session=True, default_version="v2")
    async def create_template(
        self,
    contract_id: str,
    type_: str,
    name: str,
    api_version: str = "v2",   # ← обязателен
) -> TemplateResponse:
        """Создать новый шаблон ВК"""
        payload = {"contract_id": contract_id, "type": type_, "name": name}
        data = await self._request(
            "post", "vc/templates",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def update_template(self, template_id: str, contract_id: str, type_: str, name: str, api_version: str = "v2",) -> TemplateResponse:
        """Изменить шаблон ВК"""
        payload = {"contract_id": contract_id, "type": type_, "name": name}
        data = await self._request(
            "post", f"vc/templates/{template_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def delete_template(self, template_id: str, api_version: str = "v2") -> DeleteTemplateResponse:
        """Удалить шаблон ВК"""
        data = await self._request(
            "delete", f"vc/templates/{template_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return DeleteTemplateResponse(success=data["data"])

    # ---------- Лимиты ----------
    @api_method(require_session=True, default_version="v2")
    async def get_template_limits(self, template_id: str, api_version: str = "v2") -> TemplateLimitListResponse:
        """Получить список лимитов шаблона ВК"""
        data = await self._request(
            "get", f"vc/templates/{template_id}/limits",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateLimitListResponse(**data["data"])

    @api_method(require_session=True, default_version="v2")
    async def create_template_limit(self, template_id: str, payload: dict, api_version: str = "v2") -> TemplateResponse:
        """Создать лимит для шаблона ВК"""
        data = await self._request(
            "post", f"vc/templates/{template_id}/limits",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def update_template_limit(self, template_id: str, limit_id: str, payload: dict, api_version: str = "v2") -> TemplateResponse:
        """Изменить лимит шаблона ВК"""
        data = await self._request(
            "post", f"vc/templates/{template_id}/limits/{limit_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def delete_template_limit(self, template_id: str, limit_id: str, api_version: str = "v2") -> DeleteTemplateResponse:
        """Удалить лимит шаблона ВК"""
        data = await self._request(
            "delete", f"vc/templates/{template_id}/limits/{limit_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return DeleteTemplateResponse(success=data["data"])

    # ---------- Ограничители ----------
    @api_method(require_session=True, default_version="v2")
    async def get_template_restrictions(self, template_id: str, api_version: str = "v2") -> TemplateRestrictionListResponse:
        """Получить список ограничителей шаблона ВК"""
        data = await self._request(
            "get", f"vc/templates/{template_id}/restrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateRestrictionListResponse(**data["data"])

    @api_method(require_session=True, default_version="v2")
    async def create_template_restriction(self, template_id: str, payload: dict, api_version: str = "v2") -> TemplateResponse:
        """Создать ограничитель для шаблона ВК"""
        data = await self._request(
            "post", f"vc/templates/{template_id}/restrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def update_template_restriction(self, template_id: str, restriction_id: str, payload: dict, api_version: str = "v2") -> TemplateResponse:
        """Изменить ограничитель шаблона ВК"""
        data = await self._request(
            "post", f"vc/templates/{template_id}/restrictions/{restriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def delete_template_restriction(self, template_id: str, restriction_id: str, api_version: str = "v2") -> DeleteTemplateResponse:
        """Удалить ограничитель шаблона ВК"""
        data = await self._request(
            "delete", f"vc/templates/{template_id}/restrictions/{restriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return DeleteTemplateResponse(success=data["data"])

    # ---------- Геоограничители ----------
    @api_method(require_session=True, default_version="v2")
    async def get_template_georestrictions(self, template_id: str, api_version: str = "v2") -> TemplateGeoRestrictionListResponse:
        """Получить список геоограничителей шаблона ВК"""
        data = await self._request(
            "get", f"vc/templates/{template_id}/georestrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return TemplateGeoRestrictionListResponse(**data["data"])

    @api_method(require_session=True, default_version="v2")
    async def create_template_georestriction(self, template_id: str, payload: dict, api_version: str = "v2") -> TemplateResponse:
        """Создать геоограничитель для шаблона ВК"""
        data = await self._request(
            "post", f"vc/templates/{template_id}/georestrictions",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def update_template_georestriction(self, template_id: str, georestriction_id: str, payload: dict, api_version: str = "v2") -> TemplateResponse:
        """Изменить геоограничитель шаблона ВК"""
        data = await self._request(
            "post", f"vc/templates/{template_id}/georestrictions/{georestriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=payload,
        )
        return TemplateResponse(id=data["data"])

    @api_method(require_session=True, default_version="v2")
    async def delete_template_georestriction(self, template_id: str, georestriction_id: str, api_version: str = "v2") -> DeleteTemplateResponse:
        """Удалить геоограничитель шаблона ВК"""
        data = await self._request(
            "delete", f"vc/templates/{template_id}/georestrictions/{georestriction_id}",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return DeleteTemplateResponse(success=data["data"])
