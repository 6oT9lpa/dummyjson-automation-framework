from framework.api.clients.base_api_client import BaseApiClient
from framework.api.models.requests import LoginRequest
from framework.api.response.api_response import ApiResponse


class AuthApiClient(BaseApiClient):
    def login(self, payload: LoginRequest) -> ApiResponse:
        return self._post(
            "/auth" + "/login",
            json=payload.model_dump(by_alias=True),
        )

    def get_current_user(self, token: str | None = None) -> ApiResponse:
        return self._get(
            "/auth" + "/me",
            headers=self._bearer_headers(token),
        )
