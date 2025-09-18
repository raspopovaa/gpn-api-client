from ..decorators import api_method
from ..models.dictionaries import AZSResponse, AZSFiltersResponse, DictionaryResponse


class DictionariesMixin:
    @api_method(require_session=True, default_version="v1")
    async def get_azs(
            self,
            *,
            filter: dict | None = None,
            page: int | None = None,
            on_page: int | None = None,
            api_version: str = "v2"
    ) -> AZSResponse:
        """Получение списка торговых точек (АЗС)"""
        params = {}
        if filter:
            params["filter"] = filter
        if page:
            params["page"] = page
        if on_page:
            params["on_page"] = on_page

        data = await self._request(
            "get",
            "azs",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )
        return AZSResponse(**data["data"])

    @api_method(require_session=True, default_version="v2")
    async def get_azs_filters(self, api_version: str = "v2") -> AZSFiltersResponse:
        """Получение доступных фильтров для поиска АЗС"""
        data = await self._request(
            "get",
            "azs/filters",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return AZSFiltersResponse(**data["data"])

    @api_method(require_session=True, default_version="v1")
    async def get_dictionary(self, name: str, api_version: str = "v1") -> DictionaryResponse:
        """Получение общего справочника"""
        data = await self._request(
            "get",
            "getDictionary",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params={"name": name},
        )
        return DictionaryResponse(**data["data"])
