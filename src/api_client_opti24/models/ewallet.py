from pydantic import BaseModel, Field
from typing import List, Any


class Status(BaseModel):
    """Модель для статуса ответа API."""
    code: int = Field(..., description="Код HTTP-статуса ответа (например, 200).")


# ============================================================
# 1️⃣ Изменить тип продукта карты
# ============================================================

class SetCardProductResponse(BaseModel):
    """
    Ответ на запрос изменения типа продукта карты (setCardProduct).
    Пример ответа:
    {
        "status": {"code": 200},
        "data": ["11148025"],
        "timestamp": 1596024392
    }
    """
    status: Status = Field(..., description="Статус выполнения операции.")
    data: List[str] = Field(..., description="Список идентификаторов карт, у которых изменён продукт.")
    timestamp: int = Field(..., description="Метка времени ответа (UNIX timestamp).")


# ============================================================
# 2️⃣ Перевести деньги с договора на кошелёк
# ============================================================

class MoveToCardResponse(BaseModel):
    """
    Ответ на запрос перевода денег с договора на карту-кошелёк (moveToCard).
    Пример ответа:
    {
        "status": {"code": 200},
        "data": true,
        "timestamp": 1596024392
    }
    """
    status: Status = Field(..., description="Статус выполнения операции.")
    data: bool = Field(..., description="Результат выполнения операции (true — успешно).")
    timestamp: int = Field(..., description="Метка времени ответа (UNIX timestamp).")


# ============================================================
# 3️⃣ Перевести деньги с кошелька на договор
# ============================================================

class MoveToContractResponse(BaseModel):
    """
    Ответ на запрос перевода денег с кошелька на договор (moveToContract).
    Пример ответа:
    {
        "status": {"code": 200},
        "data": true,
        "timestamp": 1596024392
    }
    """
    status: Status = Field(..., description="Статус выполнения операции.")
    data: bool = Field(..., description="Результат выполнения операции (true — успешно).")
    timestamp: int = Field(..., description="Метка времени ответа (UNIX timestamp).")
