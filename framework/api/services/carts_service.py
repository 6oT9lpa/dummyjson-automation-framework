from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.responses import CartResponse


class CartsService:
    def __init__(self, carts_api_client: CartsApiClient) -> None:
        self._carts_api_client = carts_api_client

    def get_existing_cart(self, cart_id: int) -> CartResponse:
        response = self._carts_api_client.get_cart_by_id(cart_id)
        response.should_have_status(200)

        return response.as_model(CartResponse)

    def get_cart(self, cart_id: int) -> CartResponse:
        return self.get_existing_cart(cart_id)
