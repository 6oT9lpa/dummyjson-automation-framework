from framework.api.clients.auth_api_client import AuthApiClient
from framework.api.models.responses import AuthUserResponse
from framework.models.test_data import TestData


def test_get_current_user_with_token(
    step,
    auth_api_client: AuthApiClient,
    access_token: str,
    test_data: TestData,
) -> None:
    step("Get current authorized user with bearer token")
    response = auth_api_client.get_current_user(access_token)

    step("Check authorized user response")
    response.should_have_status(200)
    user_response = response.as_model(AuthUserResponse)
    expected_user = test_data.dummyjson.auth.expected_user

    assert user_response.id == expected_user.id
    assert user_response.username == expected_user.username
