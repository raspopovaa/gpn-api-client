from typing import Optional, List
from pydantic import BaseModel, Field


class RegionLimit(BaseModel):
    """Региональный лимит по договору, карте или группе карт."""

    id: Optional[str] = None
    contract_id: Optional[str] = None
    card_id: Optional[str] = None
    group_id: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None
    service_center: Optional[str] = None
    limit_type: Optional[int] = None  # 1, 2, ...
    date: Optional[str] = None


class RegionLimitList(BaseModel):
    """Коллекция региональных лимитов."""

    total_count: int = Field(default=0)
    result: List[RegionLimit] = Field(default_factory=list)
