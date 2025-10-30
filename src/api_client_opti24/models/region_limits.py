from typing import Optional, List
from pydantic import BaseModel, Field


class RegionLimit(BaseModel):
    """Региональный лимит по договору, карте или группе карт."""

    id: Optional[str] = Field(..., description="ID регионального лимита")
    contract_id: str = Field(..., description="ID договора, к которому относится лимит")
    card_id: Optional[str] = Field(None, description="ID карты, если лимит задан для карты")
    group_id: Optional[str] = Field(None, description="ID группы карт, если лимит задан для группы")
    country: str = Field(..., description="Код страны обслуживания, пример - RUS")
    region: Optional[str] = Field(None, description="Код регион обслуживания")
    service_center: Optional[str] = Field(None, description="ID АЗС")
    date: Optional[str] = Field(None, description="Дата последнего изменения")
    limit_type: int = Field(..., description="Тип лимита") # 1 – Разрешающий ограничитель, 2 – Запрещающий ограничитель

class RegionLimitList(BaseModel):
    """Коллекция региональных лимитов."""
    total_count: int = Field(..., description="Общее количество лимитов")
    result: List[RegionLimit] = Field(..., description="Данные с лимитами")

class RegionLimitResponse(BaseModel):
    """Коллекция региональных лимитов."""
    status: dict = Field(..., description="Статус ответа")
    data: RegionLimitList = Field(..., description="Данные с лимитами")
    timestamp: int = Field(..., description="Метка времени сервера")

class RemoveRegionLimit(BaseModel):
    """Удаление регионального лимита."""
    status: dict = Field(..., description="Статус выполнения запроса")
    data: bool = Field(..., description="Результат операции (True — успешно)")
    timestamp: int = Field(..., description="Временная метка ответа")
