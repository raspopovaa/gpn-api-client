from pydantic import BaseModel, Field
from typing import List, Optional


class FinalPriceItem(BaseModel):
    """Товар с рассчитанной финальной ценой"""
    code: str = Field(..., description="Код товара")
    price: float = Field(..., description="Финальная цена за единицу товара")


class FinalPricesData(BaseModel):
    """Данные о финальных ценах"""
    total_count: int = Field(..., description="Количество товаров")
    goods: List[FinalPriceItem] = Field(..., description="Список товаров с ценами")


class FinalPricesResponse(BaseModel):
    """Ответ API при расчёте финальных цен"""
    data: FinalPricesData = Field(..., description="Информация о финальных ценах")


class CheckPurchaseRequestItem(BaseModel):
    """Элемент проверки покупки"""
    code: str = Field(..., description="Код товара")
    quantity: float = Field(..., description="Количество товара")
    price: float = Field(..., description="Цена за единицу товара")


class CheckPurchaseResponse(BaseModel):
    """Ответ API на проверку возможности транзакции"""
    data: bool = Field(..., description="Доступность транзакции (True/False)")
