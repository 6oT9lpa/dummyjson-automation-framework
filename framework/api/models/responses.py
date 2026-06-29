from pydantic import BaseModel, ConfigDict, Field


class AuthUserResponse(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    username: str
    email: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    gender: str
    image: str


class LoginResponse(AuthUserResponse):
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")


class CartProductResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: int
    quantity: int


class CartResponse(BaseModel):
    model_config = ConfigDict(extra="allow", populate_by_name=True)

    id: int
    products: list[CartProductResponse] = Field(default_factory=list)
    user_id: int | None = Field(default=None, alias="userId")
    is_deleted: bool | None = Field(default=None, alias="isDeleted")
    deleted_on: str | None = Field(default=None, alias="deletedOn")


class CartsResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    carts: list[CartResponse] = Field(default_factory=list)
    total: int
    skip: int
    limit: int


class ApiErrorResponse(BaseModel):
    model_config = ConfigDict(extra="allow")

    message: str
