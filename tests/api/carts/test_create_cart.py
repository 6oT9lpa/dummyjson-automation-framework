from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.requests import AddCartRequest
from framework.api.models.responses import CartResponse


def test_create_cart(
    step,
    carts_api_client: CartsApiClient,
    add_cart_request: AddCartRequest,
) -> None:
    step("Create cart")
    response = carts_api_client.create_cart(add_cart_request)

    step("Check created cart response")
    response.should_have_status(201)
    cart_response = response.as_model(CartResponse)

    assert cart_response.user_id == add_cart_request.user_id
    assert cart_response.products[0].id == add_cart_request.products[0].id
    assert cart_response.products[0].quantity == add_cart_request.products[0].quantity
