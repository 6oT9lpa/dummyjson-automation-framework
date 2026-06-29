from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.responses import CartsResponse
from framework.models.test_data import TestData


def test_get_user_carts(
    step,
    carts_api_client: CartsApiClient,
    test_data: TestData,
) -> None:
    user_id = test_data.dummyjson.carts.user_id

    step("Get carts by user id")
    response = carts_api_client.get_user_carts(user_id)

    step("Check user carts response")
    response.should_have_status(200)
    carts_response = response.as_model(CartsResponse)

    assert carts_response.carts
    assert all(cart.user_id == user_id for cart in carts_response.carts)
