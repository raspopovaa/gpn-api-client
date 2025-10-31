from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# ============================================================
# Общие структуры
# ============================================================

class TransactionItem(BaseModel):
    """Позиция (товар) внутри транзакции."""
    id: str = Field(..., description="ID позиции транзакции")
    rrn: str = Field(..., description="Уникальный номер RRN")
    product: str = Field(..., description="Наименование продукта (топлива)")
    amount: str = Field(..., description="Количество продукта")
    price: str = Field(..., description="Цена за единицу")
    base_cost: str = Field(..., description="Базовая стоимость")
    cost: str = Field(..., description="Итоговая стоимость с учетом скидки")
    discount: str = Field(..., description="Скидка по позиции")
    discount_cost: str = Field(..., description="Стоимость с учётом скидки")
    transaction: str = Field(..., description="ID транзакции")
    currency: str = Field(..., description="Валюта")
    unit: str = Field(..., description="Единица измерения")


class RequestInfo(BaseModel):
    """Информация о типе и названии запроса."""
    type: str = Field(..., description="Тип операции (например, Advice)")
    name: str = Field(..., description="Название операции (например, Покупка)")


class TransactionV1(BaseModel):
    """Транзакция для версии v1."""
    id: str = Field(..., description="ID транзакции")
    time: datetime = Field(..., description="Дата и время транзакции")
    host_date: datetime = Field(..., description="Дата и время на хосте")
    currency: str = Field(..., description="Код валюты (например, 810)")
    card_id: str = Field(..., description="ID карты")
    service_center: str = Field(..., description="ID сервисного центра (АЗС)")
    card_number: str = Field(..., description="Номер карты")
    base_cost: str = Field(..., description="Базовая стоимость транзакции")
    cost: str = Field(..., description="Фактическая стоимость с учётом скидок")
    discount: str = Field(..., description="Размер скидки")
    discount_cost: str = Field(..., description="Стоимость после применения скидки")
    incoming: bool = Field(..., description="Признак входящей транзакции")
    request: RequestInfo = Field(..., description="Информация о типе операции")
    transaction_items: List[TransactionItem] = Field(..., description="Список товаров в транзакции")


class TransactionItemV2(BaseModel):
    """Позиция в транзакции (v2)."""
    id: int = Field(..., description="ID транзакции")
    timestamp: datetime = Field(..., description="Время транзакции (локальное)")
    utc_time: datetime = Field(..., description="Время транзакции в UTC")
    card_id: str = Field(..., description="ID карты")
    poi_id: str = Field(..., description="ID точки продаж (АЗС)")
    terminal_id: str = Field(..., description="ID терминала")
    type: str = Field(..., description="Тип операции (P — покупка, R — возврат)")
    product_id: str = Field(..., description="ID продукта")
    product_name: str = Field(..., description="Наименование продукта")
    product_category_id: str = Field(..., description="Категория продукта (например, НП)")
    currency: str = Field(..., description="Код валюты (например, RUR)")
    check_id: int = Field(..., description="Номер чека")
    stor_transaction_id: int = Field(..., description="ID сторнируемой транзакции")
    is_storno: bool = Field(..., description="Признак сторно")
    is_manual_corrention: bool = Field(..., description="Признак ручной корректировки")
    qty: float = Field(..., description="Количество")
    price: float = Field(..., description="Цена за единицу")
    price_no_discount: float = Field(..., description="Цена без скидки")
    sum: float = Field(..., description="Сумма с учетом скидки")
    sum_no_discount: float = Field(..., description="Сумма без скидки")
    discount: float = Field(..., description="Размер скидки")
    exchange_rate: float = Field(..., description="Курс обмена")
    card_number: str = Field(..., description="Номер карты")
    payment_type: str = Field(..., description="Тип оплаты (например, Карта)")


# ============================================================
# Ответы API
# ============================================================

class TransactionsV1Data(BaseModel):
    total_count: int = Field(..., description="Общее количество транзакций")
    result: List[TransactionV1] = Field(..., description="Список транзакций")


class TransactionsV1Response(BaseModel):
    status: dict = Field(..., description="Статус ответа")
    data: TransactionsV1Data = Field(..., description="Данные ответа")
    timestamp: int = Field(..., description="Метка времени сервера")


class TransactionsV2Data(BaseModel):
    total_count: int = Field(..., description="Общее количество транзакций")
    result: List[TransactionItemV2] = Field(..., description="Список транзакций (v2)")


class TransactionsV2Response(BaseModel):
    status: dict = Field(..., description="Статус ответа")
    data: TransactionsV2Data = Field(..., description="Данные ответа")
    timestamp: int = Field(..., description="Метка времени сервера")


class TransactionDetailResponse(BaseModel):
    """Ответ метода получения детальной информации по транзакции (v2)."""
    status: dict = Field(..., description="Статус ответа")
    data: TransactionsV2Data = Field(..., description="Информация по одной транзакции")
    timestamp: int = Field(..., description="Метка времени сервера")
