from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime


class ContractInfo(BaseModel):
    id: str
    number: str


class AuthUserResponse(BaseModel):
    session_id: str
    contracts: List[ContractInfo]


class AuthError(BaseModel):
    code: str
    message: str


class AuthErrorResponse(BaseModel):
    error: AuthError


class LogoffSuccessResponse(BaseModel):
    success: bool
    message: str


class LogoffResponse(BaseModel):
    data: LogoffSuccessResponse


class UsageStatsResponse(BaseModel):
    total_calls: int
    today_calls: int
    last_call_time: datetime


class GetInfoResponse(BaseModel):
    data: UsageStatsResponse