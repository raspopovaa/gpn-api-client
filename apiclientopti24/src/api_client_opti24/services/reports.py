import logging

from ..decorators import api_method
from apiclientopti24.config import LOG_LEVEL, LOGGER_FILE
log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
logging.basicConfig(
    level=log_level,
    filename=LOGGER_FILE,
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("reports")

class ReportsMixin:
    @api_method(require_session=True, default_version="v2")
    async def get_reports(self, api_version: str = "v2") -> dict:
        return await self._request("get", "reports", api_version=api_version, headers=self._headers(include_session=True))

    @api_method(require_session=True, default_version="v2")
    async def order_report(self, report_id: str, report_format: str, params: dict, emails: list[str] | None = None, api_version: str = "v2") -> dict:
        body = {"id": report_id, "format": report_format, "params": params}
        if emails:
            body["emails"] = emails
        return await self._request("post", "reports", api_version=api_version, headers=self._headers(include_session=True, content_type_json=True), json=body)

    @api_method(require_session=True, default_version="v2")
    async def get_report_jobs(self, api_version: str = "v2") -> dict:
        return await self._request("get", "reports/jobs", api_version=api_version, headers=self._headers(include_session=True))

    @api_method(require_session=True, default_version="v2")
    async def download_report(self, job_id: str, api_version: str = "v2"):
        async for chunk in await self._request("get", f"reports/jobs/{job_id}", api_version=api_version, headers=self._headers(include_session=True), stream=True):
            yield chunk
