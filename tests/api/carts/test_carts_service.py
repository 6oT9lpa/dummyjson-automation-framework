from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.services.carts_service import CartsService
from framework.models.test_data import TestData


def test_carts_service_get_cart(
    step,
    carts_api_client: CartsApiClient,
    test_data: TestData,
) -> None:
    cart_id = test_data.dummyjson.carts.cart_id
    carts_service = CartsService(carts_api_client)

    step("Get existing cart through service layer")
    cart = carts_service.get_cart(cart_id)

    assert cart.id == cart_id
    assert cart.products
