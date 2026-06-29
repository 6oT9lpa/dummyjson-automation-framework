from framework.api.clients.auth_api_client import AuthApiClient
from framework.api.models.requests import LoginRequest
from framework.api.models.responses import LoginResponse
from framework.models.test_data import TestData


def test_login_success(
    step,
    auth_api_client: AuthApiClient,
    valid_login_request: LoginRequest,
    test_data: TestData,
) -> None:
    step("Login user with valid credentials")
    response = auth_api_client.login(valid_login_request)

    step("Check successful login response")
    response.should_have_status(200)
    content_type = response.raw.headers.get("content-type", "")
    login_response = response.as_model(LoginResponse)

    assert "application/json" in content_type.lower()
    assert login_response.username == test_data.dummyjson.auth.expected_user.username
    assert login_response.access_token
    assert login_response.refresh_token
