from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.responses import CartResponse
from framework.models.test_data import TestData


def test_delete_cart(
    step,
    carts_api_client: CartsApiClient,
    test_data: TestData,
) -> None:
    cart_id = test_data.dummyjson.carts.cart_id

    step("Delete cart")
    response = carts_api_client.delete_cart(cart_id)

    step("Check deleted cart response")
    response.should_have_status(200)
    cart_response = response.as_model(CartResponse)

    assert cart_response.id == cart_id
    assert cart_response.is_deleted is True
    assert cart_response.deleted_on
