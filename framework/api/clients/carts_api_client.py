from framework.api.clients.base_api_client import BaseApiClient
from framework.api.models.requests import AddCartRequest, UpdateCartRequest
from framework.api.response.api_response import ApiResponse


class CartsApiClient(BaseApiClient):
    def get_user_carts(self, user_id: int) -> ApiResponse:
        return self._get(("/carts" + "/user") + f"/{user_id}")

    def get_cart_by_id(self, cart_id: int) -> ApiResponse:
        return self._get("/carts" + f"/{cart_id}")

    def create_cart(self, payload: AddCartRequest) -> ApiResponse:
        return self._post(
            "/carts" + "/add",
            json=payload.model_dump(by_alias=True),
        )

    def update_cart(self, cart_id: int, payload: UpdateCartRequest) -> ApiResponse:
        return self._put(
            "/carts" + f"/{cart_id}",
            json=payload.model_dump(by_alias=True),
        )

    def delete_cart(self, cart_id: int) -> ApiResponse:
        return self._delete("/carts" + f"/{cart_id}")
