from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ReportParameter(BaseModel):
    """Параметр отчета."""

    name: str
    value: Optional[Any] = None
    label: Optional[str] = None
    default_value: Optional[str] = None
    menu_values: Optional[List[Dict[str, Any]]] = None
    type: Optional[str] = None


class Report(BaseModel):
    """Описание доступного отчета."""

    id: str
    name: str
    formats: List[str]
    parameters: List[ReportParameter] = Field(default_factory=list)


class ReportList(BaseModel):
    """Список доступных отчетов."""

    total_count: int = Field(default=0)
    result: List[Report] = Field(default_factory=list)


class ReportJob(BaseModel):
    """Информация о заказанном отчете."""

    date: str
    client_id: str
    user_id: str
    contract_id: str
    contract_name: Optional[str] = None
    job_id: str
    report_name: str
    report_format: str
    available_after: Optional[int] = 0


class ReportJobList(BaseModel):
    """Список заказанных отчетов."""

    total_count: int = Field(default=0)
    result: List[ReportJob] = Field(default_factory=list)
