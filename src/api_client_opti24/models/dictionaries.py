from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class AZSItem(BaseModel):
    """Торговая точка (АЗС)"""
    id: str = Field(..., description="ID торговой точки")
    name: Optional[str] = Field(None, description="Название АЗС")
    address: Optional[str] = Field(None, description="Адрес")
    region: Optional[str] = Field(None, description="Регион")
    country: Optional[str] = Field(None, description="Страна")
    services: Optional[List[str]] = Field(None, description="Список доступных услуг")
    goods: Optional[List[str]] = Field(None, description="Коды доступных товаров")
    status: Optional[str] = Field(None, description="Статус АЗС")


class AZSResponse(BaseModel):
    """Ответ API со списком АЗС"""
    total_count: int = Field(..., description="Количество АЗС")
    result: List[AZSItem] = Field(..., description="Список торговых точек")


class AZSFiltersResponse(BaseModel):
    """Ответ API со списком фильтров для АЗС"""
    filters: Dict[str, List[str]] = Field(..., description="Список доступных фильтров")


class DictionaryItem(BaseModel):
    """Элемент справочника"""
    id: str = Field(..., description="ID элемента справочника")
    value: str = Field(..., description="Значение")
    last_update: str = Field(..., description="Дата обновления")
    deleted: int = Field(..., description="Признак удаления (0/1)")


class DictionaryResponse(BaseModel):
    """Ответ API со справочником"""
    total_count: int = Field(..., description="Количество элементов")
    result: List[DictionaryItem] = Field(..., description="Список элементов справочника")
