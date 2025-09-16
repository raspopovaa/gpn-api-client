from typing import Optional, List
from pydantic import BaseModel, Field


class Restriction(BaseModel):
    """Товарный ограничитель."""

    id: Optional[str] = None
    contract_id: str
    card_id: Optional[str] = None
    group_id: Optional[str] = None
    productType: Optional[str] = None
    productGroup: Optional[str] = None
    productTypeName: Optional[str] = None
    productGroupName: Optional[str] = None
    restriction_type: Optional[int] = None  # 1, 2, 3 ...
    date: Optional[str] = None


class RestrictionList(BaseModel):
    """Коллекция товарных ограничителей."""

    total_count: int = Field(default=0)
    result: List[Restriction] = Field(default_factory=list)
