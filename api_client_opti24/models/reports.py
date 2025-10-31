from pydantic import BaseModel, Field
from typing import List, Optional, Any


# === Общие модели ===

class ReportParameterMenuValue(BaseModel):
    """Значения меню для параметра отчета."""
    labels: Optional[str] = Field(None, description="Отображаемое имя пункта меню")
    values: Optional[str] = Field(None, description="Значение пункта меню")


class ReportParameter(BaseModel):
    """Параметр отчета (например, дата, карта, договор)."""
    name: str = Field(..., description="Имя параметра, используемое в запросах")
    value: Optional[Any] = Field(None, description="Значение параметра")
    label: Optional[str] = Field(None, description="Отображаемое название параметра")
    default_value: Optional[str] = Field(None, description="Значение по умолчанию")
    menu_values: Optional[List[ReportParameterMenuValue]] = Field(
        None, description="Список возможных значений для выбора из меню"
    )
    type: Optional[str] = Field(None, description="Тип параметра (например, date, Contract, Group)")


class ReportItem(BaseModel):
    """Описание доступного отчета (v2)."""
    id: str = Field(..., description="Идентификатор отчета")
    name: str = Field(..., description="Название отчета")
    formats: List[str] = Field(..., description="Список поддерживаемых форматов (pdf, xlsx, csv и т.д.)")
    parameters: List[ReportParameter] = Field(..., description="Список параметров отчета")


class ReportList(BaseModel):
    """Ответ метода /v2/reports — список доступных отчетов."""
    total_count: int = Field(..., description="Количество доступных отчетов")
    result: List[ReportItem] = Field(..., description="Массив отчетов")


# === Заказ отчета ===

class ReportOrderParams(BaseModel):
    """Параметры заказа отчета."""
    start_date: Optional[str] = Field(None, description="Дата начала периода")
    end_date: Optional[str] = Field(None, description="Дата окончания периода")
    id_agreement: Optional[str] = Field(None, description="Список ID договоров")
    id_card: Optional[List[str]] = Field(None, description="Список карт")
    card_group_code: Optional[List[str]] = Field(None, description="Список групп карт")
    id_client: Optional[List[str]] = Field(None, description="Список клиентов")
    additional: Optional[dict] = Field(None, description="Дополнительные параметры")


class ReportOrderRequest(BaseModel):
    """Тело запроса для заказа отчета (v2)."""
    id: str = Field(..., description="Идентификатор отчета")
    format: str = Field(..., description="Формат отчета (pdf, xlsx и т.д.)")
    emails: Optional[str] = Field(None, description="Email-адреса для отправки отчета")
    params: ReportOrderParams = Field(..., description="Параметры отчета")


class ReportOrderResponse(BaseModel):
    """Ответ на заказ отчета (v2)."""
    job_id: List[str] = Field(..., description="Идентификаторы созданных заданий на генерацию отчета")


# === Список заказанных отчетов ===

class ReportJobItem(BaseModel):
    """Элемент списка заказанных отчетов."""
    date: str = Field(..., description="Дата создания заказа отчета")
    client_id: Optional[str] = Field(None, description="ID клиента")
    user_id: Optional[str] = Field(None, description="ID пользователя")
    contract_id: Optional[str] = Field(None, description="ID договора")
    contract_name: Optional[str] = Field(None, description="Название договора")
    job_id: str = Field(..., description="Идентификатор задания (Job ID)")
    report_name: str = Field(..., description="Название отчета")
    report_format: str = Field(..., description="Формат отчета (pdf, xlsx и т.д.)")
    available_after: Optional[int] = Field(None, description="Количество секунд до доступности отчета")


class ReportJobList(BaseModel):
    """Ответ со списком заказанных отчетов (v1/v2)."""
    total_count: Optional[int] = Field(None, description="Количество найденных отчетов")
    result: List[ReportJobItem] = Field(..., description="Список заказанных отчетов")


# === Генерация отчета ===

class ReportFileResponse(BaseModel):
    """Ответ при генерации файла отчета."""
    content: Optional[bytes] = Field(None, description="Бинарное содержимое файла (application/octet-stream)")
    format: Optional[str] = Field(None, description="Формат файла (pdf, xlsx, csv и т.д.)")
    filename: Optional[str] = Field(None, description="Имя файла отчета")
    size: Optional[int] = Field(None, description="Размер файла в байтах")


# === v1 методы ===

class ReportV1OrderResponse(BaseModel):
    """Ответ для v1 метода /reports."""
    report_ids: List[str] = Field(..., description="ID заказанных отчетов")


class ReportV1JobItem(BaseModel):
    """Элемент списка ранее заказанных отчетов (v1)."""
    date: str = Field(..., description="Дата создания отчета")
    client_id: Optional[str] = Field(None, description="ID клиента")
    user_id: Optional[str] = Field(None, description="ID пользователя")
    contract_id: Optional[str] = Field(None, description="ID договора")
    job_id: str = Field(..., description="Идентификатор задания (Job ID)")
    report_name: str = Field(..., description="Название отчета")
    report_format: str = Field(..., description="Формат отчета (pdf, xlsx, xml и т.д.)")


class ReportV1JobList(BaseModel):
    """Список заказанных отчетов (v1)."""
    jobs: List[ReportV1JobItem] = Field(..., description="Массив заказанных отчетов")
