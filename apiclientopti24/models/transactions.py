from typing import List, Optional
from pydantic import BaseModel, Field


class TransactionItem(BaseModel):
    """Элемент транзакции (товар/услуга)."""

    id: str
    rrn: Optional[str] = None
    product: Optional[str] = None
    amount: Optional[float] = None
    price: Optional[float] = None
    base_cost: Optional[float] = None
    cost: Optional[float] = None
    discount: Optional[float] = None
    discount_cost: Optional[float] = None
    transaction: Optional[str] = None
    currency: Optional[str] = None
    unit: Optional[str] = None


class TransactionRequestInfo(BaseModel):
    """Информация о запросе, инициировавшем транзакцию."""

    type: Optional[str] = None
    name: Optional[str] = None


class Transaction(BaseModel):
    """Модель транзакции."""

    id: str
    time: Optional[str] = None  # v1
    host_date: Optional[str] = None  # v1
    timestamp: Optional[str] = None  # v2
    utc_time: Optional[str] = None  # v2
    currency: Optional[str] = None
    card_id: Optional[str] = None
    card_number: Optional[str] = None
    service_center: Optional[str] = None
    terminal_id: Optional[str] = None
    poi_id: Optional[str] = None
    base_cost: Optional[float] = None
    cost: Optional[float] = None
    discount: Optional[float] = None
    discount_cost: Optional[float] = None
    incoming: Optional[bool] = None
    request: Optional[TransactionRequestInfo] = None
    transaction_items: List[TransactionItem] = Field(default_factory=list)
    qty: Optional[float] = None  # v2
    price: Optional[float] = None  # v2
    price_no_discount: Optional[float] = None
    sum: Optional[float] = None
    sum_no_discount: Optional[float] = None
    is_storno: Optional[bool] = None
    is_manual_corrention: Optional[bool] = None
    payment_type: Optional[str] = None
    product_id: Optional[str] = None
    product_name: Optional[str] = None
    product_category_id: Optional[str] = None
    check_id: Optional[int] = None
    stor_transaction_id: Optional[int] = None
    exchange_rate: Optional[float] = None


class TransactionList(BaseModel):
    """
    Список транзакций по договору.

    Attributes:
        total_count (int): Общее количество транзакций.
        result (List[Transaction]): Список транзакций.

    """
    total_count: int
    result: List[Transaction] = Field(default_factory=list)
