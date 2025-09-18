from pydantic import BaseModel, Field


class VirtualCardData(BaseModel):
    """Данные виртуальной карты"""
    id: str = Field(..., description="ID карты")
    number: str = Field(..., description="Номер карты")
    carrier: str = Field(..., description="Тип носителя (например, Virtual Card)")
    product: str = Field(..., description="Тип продукта (wallet, limit)")
    status: str = Field(..., description="Статус карты (Active, Blocked и т.д.)")


class VirtualCardResponse(BaseModel):
    """Ответ API при выпуске или получении ВК"""
    data: VirtualCardData = Field(..., description="Информация о виртуальной карте")
