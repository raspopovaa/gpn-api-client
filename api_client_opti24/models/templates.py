from typing import Optional, List
from pydantic import BaseModel, Field


# ---------- Шаблоны ----------
class Template(BaseModel):
    """Модель шаблона ВК"""
    id: str = Field(..., description="ID шаблона")
    name: str = Field(..., description="Название шаблона")
    type: str = Field(..., description="Тип карты: Limit или Wallet")
    contract_id: str = Field(..., description="ID договора")


class TemplateListResponse(BaseModel):
    """Ответ со списком шаблонов ВК"""
    total_count: int = Field(..., description="Количество шаблонов")
    result: List[Template] = Field(..., description="Массив шаблонов")


class TemplateResponse(BaseModel):
    """Ответ при создании/обновлении шаблона"""
    id: str = Field(..., description="ID созданного или изменённого шаблона")


class DeleteTemplateResponse(BaseModel):
    """Ответ при удалении шаблона"""
    success: bool = Field(..., description="Флаг успешного удаления")


# ---------- Лимиты ----------
class TemplateLimit(BaseModel):
    id: str = Field(..., description="ID лимита")
    template_id: str = Field(..., description="ID шаблона")
    contract_id: str = Field(..., description="ID договора")
    productType: Optional[str] = Field(None, description="Тип продукта")
    productGroup: Optional[str] = Field(None, description="Группа продукта")
    productTypeName: Optional[str] = Field(None, description="Название продукта")
    productGroupName: Optional[str] = Field(None, description="Название группы")
    date: Optional[str] = Field(None, description="Дата создания")
    sum: Optional[dict] = Field(None, description="Суммовой лимит")
    amount: Optional[dict] = Field(None, description="Объемный лимит")
    time: Optional[dict] = Field(None, description="Интервал времени")
    term: Optional[dict] = Field(None, description="Условия применения")
    transactions: Optional[dict] = Field(None, description="Ограничение по кол-ву транзакций")


class TemplateLimitListResponse(BaseModel):
    total_count: int = Field(..., description="Количество лимитов")
    result: List[TemplateLimit] = Field(..., description="Массив лимитов")


# ---------- Ограничители ----------
class TemplateRestriction(BaseModel):
    id: str = Field(..., description="ID ограничителя")
    template_id: str = Field(..., description="ID шаблона")
    contract_id: str = Field(..., description="ID договора")
    date: Optional[str] = Field(None, description="Дата создания")
    productType: Optional[str] = Field(None, description="Тип продукта")
    productGroup: Optional[str] = Field(None, description="Группа продукта")
    productTypeName: Optional[str] = Field(None, description="Название продукта")
    productGroupName: Optional[str] = Field(None, description="Название группы")
    restriction_type: int = Field(..., description="Тип ограничителя (1 - разрешение, 2 - запрет)")


class TemplateRestrictionListResponse(BaseModel):
    total_count: int = Field(..., description="Количество ограничителей")
    result: List[TemplateRestriction] = Field(..., description="Массив ограничителей")


# ---------- Геоограничители ----------
class TemplateGeoRestriction(BaseModel):
    id: str = Field(..., description="ID геоограничителя")
    template_id: str = Field(..., description="ID шаблона")
    contract_id: str = Field(..., description="ID договора")
    date: Optional[str] = Field(None, description="Дата создания")
    country: Optional[str] = Field(None, description="Код страны")
    countryName: Optional[str] = Field(None, description="Название страны")
    region: Optional[str] = Field(None, description="Код региона")
    regionName: Optional[str] = Field(None, description="Название региона")
    partner: Optional[str] = Field(None, description="Код партнера")
    partnerName: Optional[str] = Field(None, description="Название партнера")
    service_center: Optional[str] = Field(None, description="Код сервисного центра")
    service_centerName: Optional[str] = Field(None, description="Название сервисного центра")
    restriction_type: int = Field(..., description="Тип геоограничителя (1 - разрешение, 2 - запрет)")


class TemplateGeoRestrictionListResponse(BaseModel):
    total_count: int = Field(..., description="Количество геоограничителей")
    result: List[TemplateGeoRestriction] = Field(..., description="Массив геоограничителей")
