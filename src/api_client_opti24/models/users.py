# src/api_client_opti24/models/users.py
from typing import Optional, List
from pydantic import BaseModel, Field


class ContractStatus(BaseModel):
    id: str = Field(..., description="ID статуса договора")
    name: str = Field(..., description="Название статуса договора")


class UserContract(BaseModel):
    sid: str = Field(..., description="ID договора")
    number: str = Field(..., description="Номер договора")
    available: bool = Field(..., description="Доступность пользователю")
    status: ContractStatus = Field(..., description="Статус договора")
    template_id: Optional[str] = Field(None, description="ID шаблона виртуальной карты")
    cards_count: int = Field(..., description="Количество карт на договоре")


class UserCard(BaseModel):
    id: str = Field(..., description="ID записи карты")
    sid: str = Field(..., description="ID карты")
    number: str = Field(..., description="Номер карты")
    mpc: bool = Field(..., description="Выпущен ли мобильный профиль карты")
    product: str = Field(..., description="Тип продукта (wallet или limit)")
    comment: Optional[str] = Field(None, description="Комментарий на карте")
    status: str = Field(..., description="ID статуса карты")
    contract_id: str = Field(..., description="ID договора")
    contract_name: str = Field(..., description="Номер договора")
    available: bool = Field(..., description="Доступность пользователю")


class UserRole(BaseModel):
    id: str = Field(..., description="ID роли пользователя")
    name: str = Field(..., description="Название роли пользователя")


class UserAccess(BaseModel):
    web: bool = Field(..., description="Доступ в ЛК")
    api: bool = Field(..., description="Доступ в API")
    mobile: bool = Field(..., description="Доступ в МП")


class UserResponse(BaseModel):
    id: str = Field(..., description="ID пользователя")
    login: str = Field(..., description="Логин пользователя")
    first_name: str = Field(..., description="Имя")
    last_name: str = Field(..., description="Фамилия")
    middle_name: Optional[str] = Field(None, description="Отчество")
    date: str = Field(..., description="Дата рождения")
    position: Optional[str] = Field(None, description="Должность")
    role: UserRole = Field(..., description="Роль пользователя")
    active: Optional[bool] = Field(None, description="Активность пользователя")
    access: UserAccess = Field(..., description="Доступ пользователя (ЛК, МП, API)")
    mobile_phone: Optional[str] = Field(None, description="Телефон")
    email: Optional[str] = Field(None, description="Email")
    contracts: List[UserContract] = Field(default_factory=list, description="Список договоров пользователя")
    cards: List[UserCard] = Field(default_factory=list, description="Список карт пользователя (для водителей)")


class UsersListResponse(BaseModel):
    total_count: int = Field(..., description="Количество пользователей")
    result: List[UserResponse] = Field(..., description="Массив пользователей")
