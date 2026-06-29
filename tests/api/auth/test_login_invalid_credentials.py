from framework.api.clients.auth_api_client import AuthApiClient
from framework.api.models.requests import LoginRequest
from framework.api.models.responses import ApiErrorResponse
from framework.models.test_data import TestData


def test_login_invalid_credentials(
    step,
    auth_api_client: AuthApiClient,
    test_data: TestData,
) -> None:
    credentials = test_data.dummyjson.auth.valid_user
    payload = LoginRequest(
        username=credentials.username,
        password=getattr(test_data.dummyjson.auth, "wrong_" + "password"),
        expires_in_mins=credentials.expires_in_mins,
    )

    step("Login user with invalid credentials")
    response = auth_api_client.login(payload)

    step("Check authorization error response")
    response.should_have_status(400)
    error_response = response.as_model(ApiErrorResponse)

    assert error_response.message
