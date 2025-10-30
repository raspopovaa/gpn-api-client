from ..decorators import api_method
from ..models.ewallet import (
    SetCardProductResponse,
    MoveToCardResponse,
    MoveToContractResponse,
)
from ..logger import logger

class EwalletMixin:
    """
    Методы для работы с электронными кошельками (Ewallet).

    Электронный кошелёк — это тип карты, обслуживание которой производится не из средств договора,
    а из отдельного кошелькового счёта. Пользователь может:
      • менять тип карты (лимитная ↔ электронный кошелёк);
      • переводить средства со счёта договора на кошелёк;
      • переводить средства обратно с кошелька на договор.
    """

    # ============================================================
    #Изменить тип продукта карты
    # ============================================================

    @api_method(require_session=True, default_version="v1")
    async def set_card_product(
            self,
            *,
            contract_id: str | None = None,
            card_ids: list[str],
            product: str,
            api_version: str = "v1",
    ) -> SetCardProductResponse:
        """
        Изменить тип карты (лимитная ↔ электронный кошелёк).

        Args:
            contract_id: Идентификатор договора (если не указан — берётся из сессии).
            card_ids: Список ID карт для изменения.
            product: Тип продукта ("limit" или "wallet").
            api_version: Версия API (по умолчанию v1).

        Returns:
            SetCardProductResponse: Результат изменения продукта карт.
        """
        cid = contract_id or self.contract_id
        if not cid:
            logger.debug("contract_id обязателен для move_to_contract")
            raise ValueError("contract_id обязателен для set_card_product")

        body = {
            "contract_id": cid,
            "card_id": str(card_ids).replace("'", '"'),  # API ожидает JSON-список в строке
            "product": product,
        }

        data = await self._request(
            "post",
            "setCardProduct",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        return SetCardProductResponse(**data)

    # ============================================================
    # Перевести деньги с договора на кошелёк
    # ============================================================

    @api_method(require_session=True, default_version="v1")
    async def move_to_card(
            self,
            *,
            contract_id: str | None = None,
            card_id: str,
            amount: float,
            api_version: str = "v1",
    ) -> MoveToCardResponse:
        """
        Перевести деньги со счёта договора на электронный кошелёк карты.

        Args:
            contract_id: Идентификатор договора.
            card_id: Идентификатор карты-кошелька.
            amount: Сумма перевода.
            api_version: Версия API (по умолчанию v1).

        Returns:
            MoveToCardResponse: Результат перевода.
        """
        cid = contract_id or self.contract_id
        if not cid:
            logger.debug("contract_id обязателен для move_to_contract")
            raise ValueError("contract_id обязателен для move_to_card")

        body = {"contract_id": cid, "card_id": card_id, "amount": amount}

        data = await self._request(
            "post",
            "moveToCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        return MoveToCardResponse(**data)

    # ============================================================
    # Перевести деньги с кошелька на договор
    # ============================================================

    @api_method(require_session=True, default_version="v1")
    async def move_to_contract(
            self,
            *,
            contract_id: str | None = None,
            card_id: str,
            amount: float,
            api_version: str = "v1",
    ) -> MoveToContractResponse:
        """
        Перевести деньги с электронного кошелька карты обратно на договор.

        Args:
            contract_id: Идентификатор договора.
            card_id: Идентификатор карты.
            amount: Сумма перевода.
            api_version: Версия API (по умолчанию v1).

        Returns:
            MoveToContractResponse: Результат перевода.
        """
        cid = contract_id or self.contract_id
        if not cid:
            logger.debug("contract_id обязателен для move_to_contract")
            raise ValueError("contract_id обязателен для move_to_contract")

        body = {"contract_id": cid, "card_id": card_id, "amount": amount}

        data = await self._request(
            "post",
            "moveToContract",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

        return MoveToContractResponse(**data)

