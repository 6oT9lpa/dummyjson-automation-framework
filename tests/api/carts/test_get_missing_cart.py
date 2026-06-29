from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.responses import ApiErrorResponse
from framework.models.test_data import TestData


def test_get_missing_cart(
    step,
    carts_api_client: CartsApiClient,
    test_data: TestData,
) -> None:
    missing_cart_id = test_data.dummyjson.carts.missing_cart_id

    step("Get cart by non-existing id")
    response = carts_api_client.get_cart_by_id(missing_cart_id)

    step("Check not found response")
    response.should_have_status(404)
    error_response = response.as_model(ApiErrorResponse)

    assert "not found" in error_response.message.lower()
