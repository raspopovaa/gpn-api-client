from pydantic import BaseModel, Field
from typing import List, Optional


class CardGroupItem(BaseModel):
    """Информация о группе карт."""
    id: str = Field(..., description="Идентификатор группы карт")
    name: str = Field(..., description="Название группы карт")
    cards_count: int = Field(..., description="Количество карт в группе")
    status: str = Field(..., description="Статус группы (например, Synchronize)")
    contract_id: str = Field(..., description="Идентификатор договора")


class CardGroupListData(BaseModel):
    """Контейнер данных со списком групп карт."""
    total_count: int = Field(..., description="Общее количество групп")
    result: List[CardGroupItem] = Field(..., description="Список групп карт")


class CardGroupListResponse(BaseModel):
    """Ответ метода получения списка групп карт."""
    status: dict = Field(..., description="Информация о статусе запроса (код и описание)")
    data: CardGroupListData = Field(..., description="Основные данные ответа")
    timestamp: int = Field(..., description="Временная метка ответа (UNIX timestamp)")


class SetCardsToGroupResponse(BaseModel):
    """Ответ метода добавления карт в группу."""
    status: dict = Field(..., description="Информация о статусе запроса (код и описание)")
    data: bool = Field(..., description="Флаг успешного выполнения операции")
    timestamp: int = Field(..., description="Временная метка ответа (UNIX timestamp)")


class RemoveCardGroupResponse(BaseModel):
    """Ответ метода удаления группы карт."""
    status: dict = Field(..., description="Информация о статусе запроса (код и описание)")
    data: bool = Field(..., description="Флаг успешного выполнения операции")
    timestamp: int = Field(..., description="Временная метка ответа (UNIX timestamp)")


class SetCardGroupData(BaseModel):
    """Информация о созданной или изменённой группе."""
    id: str = Field(..., description="Идентификатор созданной или изменённой группы")


class SetCardGroupResponse(BaseModel):
    """Ответ метода установки/изменения группы карт."""
    status: dict = Field(..., description="Информация о статусе запроса (код и описание)")
    data: SetCardGroupData = Field(..., description="Информация о созданной/обновлённой группе")
    timestamp: int = Field(..., description="Временная метка ответа (UNIX timestamp)")
