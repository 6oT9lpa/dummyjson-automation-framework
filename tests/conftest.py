import time

import pytest

from framework.api.clients.auth_api_client import AuthApiClient
from framework.api.clients.carts_api_client import CartsApiClient
from framework.api.models.requests import (
    AddCartRequest,
    CartProductRequest,
    LoginRequest,
    UpdateCartRequest,
)
from framework.api.services.auth_service import AuthService
from framework.core.logger import get_logger
from framework.core.settings import TestDataManager
from framework.models.test_data import TestData

logger = get_logger("tests")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, f"rep_{call.when}", outcome.get_result())


@pytest.fixture(autouse=True)
def test_logging(request):
    start_time = time.monotonic()
    logger.info("Test started: %s", request.node.nodeid)

    yield

    duration = time.monotonic() - start_time
    report = getattr(request.node, "rep_call", None)
    status = report.outcome if report is not None else "unknown"
    logger.info("Test finished: %s, status=%s, duration=%.2fs", request.node.nodeid, status, duration)


@pytest.fixture
def step(request):
    counter = {"value": 0}

    def _step(text: str) -> None:
        counter["value"] += 1
        logger.info("Step %s: %s | test=%s", counter["value"], text, request.node.nodeid)

    return _step


@pytest.fixture
def test_data() -> TestData:
    return TestDataManager().data


@pytest.fixture
def auth_api_client() -> AuthApiClient:
    return AuthApiClient()


@pytest.fixture
def carts_api_client() -> CartsApiClient:
    return CartsApiClient()


@pytest.fixture
def auth_service(auth_api_client: AuthApiClient) -> AuthService:
    return AuthService(auth_api_client)


@pytest.fixture
def valid_login_request(test_data: TestData) -> LoginRequest:
    credentials = test_data.dummyjson.auth.valid_user

    return LoginRequest(
        username=credentials.username,
        password=credentials.password,
        expires_in_mins=credentials.expires_in_mins,
    )


@pytest.fixture
def access_token(auth_service: AuthService, valid_login_request: LoginRequest) -> str:
    return auth_service.get_token(valid_login_request)


@pytest.fixture
def add_cart_request(test_data: TestData) -> AddCartRequest:
    cart_data = test_data.dummyjson.carts
    product = CartProductRequest.model_validate(cart_data.product.model_dump())

    return AddCartRequest(user_id=cart_data.user_id, products=[product])


@pytest.fixture
def update_cart_request(test_data: TestData) -> UpdateCartRequest:
    product = CartProductRequest.model_validate(test_data.dummyjson.carts.updated_product.model_dump())

    return UpdateCartRequest(products=[product])
