import logging
from typing import Optional, Dict, Any, Literal

from .services.Invites import InviteMixin
from .services.auth import AuthMixin
from .services.cards import CardsMixin
from .services.reports import ReportsMixin
from .services.transactions import TransactionsMixin
from .services.card_group import CardGroupsMixin
from .services.contract import ContractMixin
from .services.ewallet import EwalletMixin
from .services.limits import LimitsMixin
from .services.region_limits import RegionLimitsMixin
from .services.restrictions import RestrictionsMixin
from .transport import AsyncTransport
from datetime import datetime
from .logger import logger


class APIClient(
    AuthMixin,
    CardsMixin,
    ReportsMixin,
    TransactionsMixin,
    ContractMixin,
    EwalletMixin,
    LimitsMixin,
    RestrictionsMixin,
    RegionLimitsMixin,
    CardGroupsMixin,
    InviteMixin
):
    def __init__(self, base_url: str, api_key: str, login: str, password: str):
        self.api_key = api_key
        self.login = login
        self.password = password
        self.session_id: Optional[str] = None
        self.contract_id: Optional[str] = None

        self.transport = AsyncTransport(base_url, client=self)

    def _headers(self, include_session: bool = False, content_type_json: Literal[True, False] = False) -> Dict[str, str]:
        headers = {
            "api_key": self.api_key,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/json" if content_type_json else "application/x-www-form-urlencoded",
        }
        if include_session and self.session_id:
            headers["session_id"] = self.session_id
        if self.contract_id:
            headers["contract_id"] = self.contract_id
        return headers

    async def _request(self, *args, **kwargs):
        logger.debug("Sending request with args: %s, kwargs: %s", args, kwargs)
        result = await self.transport.request(*args, **kwargs)
        logger.debug("Received response: %s", result)
        return result