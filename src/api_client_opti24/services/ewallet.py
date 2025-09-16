from ..decorators import api_method


class EwalletMixin:
    """
    Методы для работы с электронными кошельками (Ewallet).
    """

    @api_method(require_session=True, default_version="v1")
    async def set_card_product(
            self,
            *,
            contract_id: str | None = None,
            card_ids: list[str],
            product: str,
            api_version: str = "v1",
    ) -> dict:
        """
        Изменить тип карты (лимитная ↔ электронный кошелек).
        product: "limit" или "wallet"
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для set_card_product")

        body = {
            "contract_id": cid,
            "card_id": str(card_ids).replace("'", '"'),
            "product": product,
        }

        return await self._request(
            "post",
            "setCardProduct",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v1")
    async def move_to_card(
            self,
            *,
            contract_id: str | None = None,
            card_id: str,
            amount: float,
            api_version: str = "v1",
    ) -> dict:
        """
        Перевести деньги со счета договора на электронный кошелек карты.
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для move_to_card")

        body = {"contract_id": cid, "card_id": card_id, "amount": amount}

        return await self._request(
            "post",
            "moveToCard",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )

    @api_method(require_session=True, default_version="v1")
    async def move_to_contract(
            self,
            *,
            contract_id: str | None = None,
            card_id: str,
            amount: float,
            api_version: str = "v1",
    ) -> dict:
        """
        Перевести деньги с электронного кошелька карты обратно на договор.
        """
        cid = contract_id or self.contract_id
        if not cid:
            raise ValueError("contract_id обязателен для move_to_contract")

        body = {"contract_id": cid, "card_id": card_id, "amount": amount}

        return await self._request(
            "post",
            "moveToContract",
            api_version=api_version,
            headers=self._headers(include_session=True),
            data=body,
        )
