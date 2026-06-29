from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.requests import UpdateCartRequest
from framework.api.models.responses import CartResponse
from framework.models.test_data import TestData


def test_update_cart(
    step,
    carts_api_client: CartsApiClient,
    update_cart_request: UpdateCartRequest,
    test_data: TestData,
) -> None:
    cart_id = test_data.dummyjson.carts.cart_id
    expected_product = update_cart_request.products[0]

    step("Update cart")
    response = carts_api_client.update_cart(cart_id, update_cart_request)

    step("Check updated cart response")
    response.should_have_status(200)
    cart_response = response.as_model(CartResponse)

    assert cart_response.id == cart_id
    assert any(product.id == expected_product.id for product in cart_response.products)
