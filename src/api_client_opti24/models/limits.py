from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class LimitAmount(BaseModel):
    value: float
    used: Optional[float] = 0
    unit: str


class LimitTerm(BaseModel):
    days: Optional[str]
    type: Optional[int]
    time: Optional[Dict[str, str]]  # {"from": "07:00", "to": "18:00"}


class LimitTransactions(BaseModel):
    count: Optional[int]
    occured: Optional[int]


class LimitTime(BaseModel):
    number: Optional[int]
    type: Optional[int]


class Limit(BaseModel):
    id: Optional[str] = None
    contract_id: str
    card_id: Optional[str] = None
    group_id: Optional[str] = None
    amount: Optional[LimitAmount] = None
    sum: Optional[Dict] = None  # {"currency": "810", "value": 2000}
    productGroup: Optional[str] = None
    productType: Optional[str] = None
    term: Optional[LimitTerm] = None
    transactions: Optional[LimitTransactions] = None
    time: Optional[LimitTime] = None
    date: Optional[str] = None


class LimitList(BaseModel):
    """Коллекция лимитов с total_count."""

    total_count: int = Field(default=0)
    result: List[Limit] = Field(default_factory=list)
