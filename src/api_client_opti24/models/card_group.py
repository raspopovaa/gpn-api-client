from typing import Optional, List
from pydantic import BaseModel, Field


class CardGroup(BaseModel):
    """Группа карт."""

    id: Optional[str] = None
    name: Optional[str] = None
    cards_count: Optional[int] = None
    status: Optional[str] = None
    contract_id: Optional[str] = None


class CardGroupList(BaseModel):
    """Список групп карт."""

    total_count: int = Field(default=0)
    result: List[CardGroup] = Field(default_factory=list)
