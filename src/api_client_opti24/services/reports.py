from ..logger import logger
from typing import List, Dict, Optional
from ..decorators import api_method
from src.api_client_opti24.models.reports import ReportList, ReportJobList

class ReportsMixin:
    """
    Методы для работы с отчетами (v1 и v2).
    """

    # -------- v2 --------
    @api_method(require_session=True, default_version="v2")
    async def get_reports(
            self,
            *,
            api_version: str = "v2",
    ) -> ReportList:
        """
        Получить список доступных отчетов (v2).
        """
        raw = await self._request(
            "get",
            "reports",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return ReportList(**raw.get("data", {}))

    @api_method(require_session=True, default_version="v2")
    async def order_report(
            self,
            *,
            report_id: str,
            format: str,
            params: Dict,
            emails: Optional[List[str]] = None,
            api_version: str = "v2",
    ) -> dict:
        """
        Заказать отчет (на email или по ссылке).
        """
        body = {"id": report_id, "format": format, "params": params}
        if emails:
            body["emails"] = emails

        return await self._request(
            "post",
            "reports",
            api_version=api_version,
            headers=self._headers(include_session=True),
            json=body,
        )

    @api_method(require_session=True, default_version="v2")
    async def get_report_jobs(
            self,
            *,
            api_version: str = "v2",
    ) -> ReportJobList:
        """
        Получить список заказанных отчетов (v2).
        """
        raw = await self._request(
            "get",
            "reports/jobs",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return ReportJobList(**raw.get("data", {}))

    @api_method(require_session=True, default_version="v2")
    async def download_report_file(
            self,
            *,
            job_id: str,
            api_version: str = "v2",
    ) -> bytes:
        """
        Скачать файл отчета (по job_id).

        ⚠️ Важно: успешный запрос возможен только спустя ~300 секунд
        после заказа отчета.
        """
        self.logger.info(f"Скачивание отчета (job_id={job_id}, api_version={api_version})")

        content = await self.transport.request_stream(
            "get",
            f"/vip/{api_version}/reports/jobs/{job_id}",
            headers=self._headers(include_session=True),
        )

        self.logger.info(f"Отчет (job_id={job_id}) успешно загружен, размер={len(content)} байт")
        return content

    # -------- v1 (устаревшие методы, но поддерживаем) --------
    @api_method(require_session=True, default_version="v1")
    async def order_report_v1(
            self,
            *,
            contract_id: str,
            start: str,
            end: str,
            report_format: str,
            email: Optional[str] = None,
            cards_list: Optional[List[str]] = None,
            group_id: Optional[List[str]] = None,
            archive: bool = False,
            api_version: str = "v1",
    ) -> dict:
        """
        Заказ отчета (v1) – email или файл.
        """
        params = {
            "contract_id": contract_id,
            "start": start,
            "end": end,
            "report_format": report_format,
        }
        if email:
            params["email"] = email
        if cards_list:
            params["cards_list"] = str(cards_list).replace("'", '"')
        if group_id:
            params["group_id"] = str(group_id).replace("'", '"')
        if archive:
            params["archive"] = "true"

        return await self._request(
            "get",
            "reports",
            api_version=api_version,
            headers=self._headers(include_session=True),
            params=params,
        )

    @api_method(require_session=True, default_version="v1")
    async def get_report_job_list_v1(
            self,
            *,
            api_version: str = "v1",
    ) -> List[dict]:
        """
        Получить список заказанных отчетов (v1).
        """
        raw = await self._request(
            "get",
            "getReportJobList",
            api_version=api_version,
            headers=self._headers(include_session=True),
        )
        return raw.get("data", [])

    @api_method(require_session=True, default_version="v1")
    async def download_report_file_v1(
            self,
            *,
            job_id: str,
            archive: bool = False,
            api_version: str = "v1",
    ) -> bytes:
        """
        Скачать файл отчета (v1).
        """
        params = {"job_id": job_id}
        if archive:
            params["archive"] = "true"

        return await self.transport.request_stream(
            "get",
            f"/vip/{api_version}/getReportFile",
            headers=self._headers(include_session=True),
            params=params,
        )