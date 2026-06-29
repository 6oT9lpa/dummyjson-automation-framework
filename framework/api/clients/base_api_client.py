from typing import Any

import requests

from framework.api.response.api_response import ApiResponse
from framework.core.logger import get_logger
from framework.core.settings import ConfigManager


class BaseApiClient:
    def __init__(self) -> None:
        config = ConfigManager().config
        self._base_url = config.base_url.rstrip("/")
        self._timeout = config.timeout
        self._session = requests.Session()
        self._logger = get_logger("framework")

    def _get(self, path: str, **kwargs: Any) -> ApiResponse:
        return self._request("GET", path, **kwargs)

    def _post(self, path: str, **kwargs: Any) -> ApiResponse:
        return self._request("POST", path, **kwargs)

    def _put(self, path: str, **kwargs: Any) -> ApiResponse:
        return self._request("PUT", path, **kwargs)

    def _patch(self, path: str, **kwargs: Any) -> ApiResponse:
        return self._request("PATCH", path, **kwargs)

    def _delete(self, path: str, **kwargs: Any) -> ApiResponse:
        return self._request("DELETE", path, **kwargs)

    def _request(self, method: str, path: str, **kwargs: Any) -> ApiResponse:
        url = self._build_url(path)
        request_kwargs = self._prepare_request_kwargs(kwargs)

        self._log_request(method, url, request_kwargs)
        response = self._session.request(
            method=method,
            url=url,
            timeout=self._timeout,
            **request_kwargs,
        )
        self._log_response(response)

        return ApiResponse(response)

    def _build_url(self, path: str) -> str:
        return f"{self._base_url}{path}"

    @staticmethod
    def _bearer_headers(access_token: str | None) -> dict[str, str]:
        if access_token is None:
            return {}

        return {"Authorization": f"Bearer {access_token}"}

    @staticmethod
    def _prepare_request_kwargs(kwargs: dict[str, Any]) -> dict[str, Any]:
        return {key: value for key, value in kwargs.items() if value is not None}

    def _log_request(self, method: str, url: str, kwargs: dict[str, Any]) -> None:
        self._logger.info(
            "API request: method=%s, url=%s, headers=%s, body=%s",
            method,
            url,
            self._sanitize(kwargs.get("headers", {})),
            self._sanitize(kwargs.get("json")),
        )

    def _log_response(self, response: requests.Response) -> None:
        self._logger.info(
            "API response: status_code=%s, body=%s",
            response.status_code,
            self._sanitize_response_body(response),
        )

    def _sanitize_response_body(self, response: requests.Response) -> Any:
        try:
            return self._sanitize(response.json())
        except ValueError:
            return response.text

    def _sanitize(self, value: Any) -> Any:
        if isinstance(value, dict):
            return {
                key: self._mask_sensitive_value(key, item)
                for key, item in value.items()
            }

        if isinstance(value, list):
            return [self._sanitize(item) for item in value]

        return value

    def _mask_sensitive_value(self, key: str, value: Any) -> Any:
        return self._sanitize(value)