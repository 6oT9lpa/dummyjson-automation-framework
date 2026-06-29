from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.responses import CartResponse
from framework.models.test_data import TestData


def test_get_cart(
    step,
    carts_api_client: CartsApiClient,
    test_data: TestData,
) -> None:
    cart_id = test_data.dummyjson.carts.cart_id

    step("Get cart")
    response = carts_api_client.get_cart_by_id(cart_id)

    step("Check cart response")
    response.should_have_status(200)
    cart_response = response.as_model(CartResponse)

    assert cart_response.id == cart_id
    assert cart_response.products
