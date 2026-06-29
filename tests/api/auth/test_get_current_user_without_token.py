from framework.api.clients.auth_api_client import AuthApiClient
from framework.api.models.responses import ApiErrorResponse


def test_get_current_user_without_token(
    step,
    auth_api_client: AuthApiClient,
) -> None:
    step("Get current authorized user without bearer token")
    response = auth_api_client.get_current_user()

    step("Check unauthorized response")
    response.should_have_status(401)
    error_response = response.as_model(ApiErrorResponse)

    assert error_response.message
