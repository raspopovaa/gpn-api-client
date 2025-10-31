# src/api_client_opti24/models/cards.py
from __future__ import annotations
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Union
from datetime import datetime


# ==========================
#ИНФОРМАЦИЯ О КАРТАХ v1
# ==========================

class TransactionTimeout(BaseModel):
    type: Union[str, int] = Field(..., description="Тип таймаута ('H', 'N' или числовое значение)")
    value: Union[str, int] = Field(..., description="Значение таймаута")

class CardInfo(BaseModel):
    id: str = Field(..., description="Уникальный идентификатор карты")
    contract_id: str = Field(..., description="Идентификатор договора")
    number: str = Field(..., description="Номер топливной карты")
    status: str = Field(..., description="Статус карты (например, Active, Locked(Client))")
    can_work_offline: Optional[bool] = Field(None, description="Может ли карта работать офлайн")
    card_auth_type: Optional[str] = Field(None, description="Тип авторизации карты (например, PIN)")
    comment: Optional[str] = Field(None, description="Комментарий к карте")
    date_expired: Optional[datetime] = Field(None, description="Дата истечения срока действия карты")
    date_last_usage: Optional[datetime] = Field(None, description="Дата последнего использования карты")
    date_released: Optional[datetime] = Field(None, description="Дата выпуска карты")
    servicecenter_last_usage_name: Optional[str] = Field(
        None, description="Название последней АЗС, где использовалась карта"
    )
    transaction_last_detail: Optional[str] = Field(None, description="Информация о последней транзакции")
    transaction_timeout: Optional[TransactionTimeout] = Field(
        None, description="Таймаут последней транзакции"
    )
    product: Optional[str] = Field(None, description="Тип продукта (limit/wallet)")
    payment_of_tolls: Optional[str] = Field(None, description="Оплата платных дорог ('Y' или 'N')")


class CardsListData(BaseModel):
    total_count: int = Field(..., description="Общее количество найденных карт")
    result: List[CardInfo] = Field(..., description="Список найденных карт")


class CardsListResponse(BaseModel):
    status: dict = Field(..., description="Объект со статусом ответа (например, {'code': 200})")
    data: CardsListData = Field(..., description="Основные данные ответа")
    timestamp: int = Field(..., description="Временная метка сервера (UNIX-timestamp)")


# ==========================
#Информация о группе карт
# ==========================
class CardGroupInfo(BaseModel):
    id: str = Field(..., description="ID карты")
    group: str = Field(..., description="ID группы карт")
    contract_id: str = Field(..., description="ID договора")
    number: str = Field(..., description="Номер карты")
    status: str = Field(..., description="Статус карты")
    comment: Optional[str] = Field(None, description="Комментарий")
    product: Optional[str] = Field(None, description="Тип продукта")
    payment_of_tolls: Optional[str] = Field(None, description="Оплата платных дорог ('Y' или 'N')")
    sync_group_state: Optional[str] = Field(None, description="Статус синхронизации группы")


class CardGroupData(BaseModel):
    total_count: int = Field(..., description="Количество карт в группе")
    result: List[CardGroupInfo] = Field(..., description="Список карт в группе")


class CardGroupResponse(BaseModel):
    status: dict = Field(..., description="Статус ответа")
    data: CardGroupData = Field(..., description="Основные данные")
    timestamp: int = Field(..., description="Метка времени сервера")


# ==========================
#водители, связанные с картой
# ==========================
class CardDriverInfo(BaseModel):
    id: str = Field(..., description="ID пользователя/водителя")
    login: str = Field(..., description="Логин (обычно телефон)")
    first_name: str = Field(..., description="Имя водителя")
    last_name: str = Field(..., description="Фамилия водителя")
    middle_name: Optional[str] = Field(None, description="Отчество водителя")
    date: Optional[str] = Field(None, description="Дата рождения или дата регистрации")
    position: Optional[str] = Field(None, description="Должность водителя")
    role: Optional[str] = Field(None, description="Роль пользователя")
    mobile_phone: str = Field(..., description="Номер телефона")
    email: Optional[str] = Field(None, description="Email водителя")


class CardDriversData(BaseModel):
    total_count: int = Field(..., description="Количество водителей, связанных с картой")
    result: List[CardDriverInfo] = Field(..., description="Список водителей")


class CardDriversResponse(BaseModel):
    status: dict = Field(..., description="Статус запроса")
    data: CardDriversData = Field(..., description="Основные данные")
    timestamp: int = Field(..., description="Метка времени сервера")


# ==========================
#детальные данные по карте
# ==========================
class CardDetail(BaseModel):
    id: str = Field(..., description="Идентификатор карты")
    contract_id: str = Field(..., description="ID договора")
    number: str = Field(..., description="Номер карты")
    status: str = Field(..., description="Статус карты")
    can_work_offline: Optional[bool] = Field(None, description="Может работать офлайн")
    card_auth_type: Optional[str] = Field(None, description="Тип аутентификации карты")
    comment: Optional[str] = Field(None, description="Комментарий к карте")
    date_last_usage: Optional[Union[datetime, str, None]] = Field(
        None, description="Дата последнего использования (может быть пустой строкой)"
    )
    date_released: Optional[Union[datetime, str, None]] = Field(None, description="Дата выпуска карты")
    servicecenter_last_usage_name: Optional[str] = Field(None, description="Название АЗС последнего использования")
    transaction_timeout: Optional[TransactionTimeout] = Field(None, description="Таймаут транзакции")
    product: Optional[str] = Field(None, description="Тип продукта (limit/wallet)")
    carrier: Optional[str] = Field(None, description="Тип карты (Plastic/Virtual)")
    available: Optional[str] = Field(None, description="Доступный лимит или баланс")
    currency: Optional[str] = Field(None, description="Валюта")
    payment_of_tolls: Optional[str] = Field(None, description="Признак оплаты дорожных сборов")
    previous: Optional[str] = Field(None, description="ID предыдущей карты")
    next: Optional[str] = Field(None, description="ID следующей карты")

    @validator("date_last_usage", "date_released", pre=True)
    def empty_str_to_none(cls, v):
        if v in ("", None):
            return None
        return v


class CardDetailData(BaseModel):
    total_count: int = Field(..., description="Количество записей")
    result: List[CardDetail] = Field(..., description="Список карт")


class CardDetailResponse(BaseModel):
    status: dict = Field(..., description="Статус ответа")
    data: CardDetailData = Field(..., description="Основные данные")
    timestamp: int = Field(..., description="Метка времени сервера")


# ==========================
#блокировка/разблокировка карт и ресет пин кода
# ==========================
class BoolResponse(BaseModel):
    status: dict = Field(..., description="Статус запроса")
    data: bool = Field(..., description="Флаг результата операции (True — успех)")
    timestamp: int = Field(..., description="Метка времени сервера")


class IDListResponse(BaseModel):
    status: dict = Field(..., description="Статус запроса")
    data: List[str] = Field(..., description="ID карт, которые были заблокированы/разблокированы")
    timestamp: int = Field(..., description="Метка времени сервера")

# ==========================
#список карт (v2)
# ==========================

class CardV2Item(BaseModel):
    """Информация об одной топливной карте договора."""

    id: str = Field(..., description="Уникальный идентификатор карты")
    group_id: Optional[str] = Field(None, description="ID группы карт, если назначена")
    group_name: Optional[str] = Field(None, description="Название группы карт")
    contract_id: str = Field(..., description="ID договора, к которому принадлежит карта")
    contract_name: Optional[str] = Field(None, description="Название договора")
    number: str = Field(..., description="Номер топливной карты")
    status: str = Field(..., description="Системное значение статуса карты")
    status_name: Optional[str] = Field(None, description="Отображаемое имя статуса (например 'Активна')")
    comment: Optional[str] = Field(None, description="Комментарий, установленный пользователем")
    product: str = Field(..., description="Тип продукта, например 'limit' или 'wallet'")
    product_name: Optional[str] = Field(None, description="Отображаемое имя продукта")
    carrier: str = Field(..., description="Тип носителя карты ('Plastic' или 'Virtual Card')")
    carrier_name: Optional[str] = Field(None, description="Название типа носителя карты")
    platon: bool = Field(..., description="Признак наличия поддержки Platon (оплата проезда)")
    avtodor: bool = Field(..., description="Признак наличия поддержки Автодора")
    sync_group_state: Optional[str] = Field(None, description="Состояние синхронизации группы карт")
    users: List[str] = Field(default_factory=list, description="Список ID пользователей, привязанных к карте")
    mpc: bool = Field(..., description="Признак наличия мультипроцессингового центра (mpc)")


class CardsV2Data(BaseModel):
    """Основной объект данных для списка карт (v2)."""

    total_count: int = Field(..., description="Общее количество найденных карт")
    result: List[CardV2Item] = Field(..., description="Список карт договора")


class CardsV2Response(BaseModel):
    """Ответ API метода GET /v2/cards."""

    status: dict = Field(..., description="Объект статуса (например {'code': 200})")
    data: CardsV2Data = Field(..., description="Основные данные (список карт)")
    timestamp: int = Field(..., description="Метка времени ответа (Unix timestamp)")