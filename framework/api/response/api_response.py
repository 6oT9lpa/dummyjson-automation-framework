from typing import TypeVar

import requests
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class ApiResponse:
    def __init__(self, response: requests.Response) -> None:
        self._response = response

    @property
    def status_code(self) -> int:
        return self._response.status_code

    @property
    def text(self) -> str:
        return self._response.text

    @property
    def raw(self) -> requests.Response:
        return self._response

    def json(self) -> dict:
        return self._response.json()

    def as_model(self, model: type[T]) -> T:
        return model.model_validate(self.json())

    def should_have_status(self, expected_status: int) -> None:
        assert self.status_code == expected_status, (
            f"Expected status code {expected_status}, "
            f"actual status code {self.status_code}. Response body: {self.text}"
        )
