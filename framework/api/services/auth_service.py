from framework.api.clients.auth_api_client import AuthApiClient
from framework.api.models.requests import LoginRequest
from framework.api.models.responses import LoginResponse


class AuthService:
    def __init__(self, auth_api_client: AuthApiClient) -> None:
        self._auth_api_client = auth_api_client

    def get_token(self, payload: LoginRequest) -> str:
        response = self._auth_api_client.login(payload)
        response.should_have_status(200)

        return response.as_model(LoginResponse).access_token
