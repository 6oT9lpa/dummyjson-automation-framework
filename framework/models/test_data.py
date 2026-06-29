from pydantic import BaseModel, ConfigDict, Field, field_validator


class AuthCredentials(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    username: str
    password_parts: tuple[str, ...] = Field(min_length=1)
    expires_in_mins: int = Field(default=30, alias="expiresInMins")

    @property
    def password(self) -> str:
        return "".join(self.password_parts)


class ExpectedAuthUser(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    username: str
    email: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    gender: str
    image: str


class AuthData(BaseModel):
    valid_user: AuthCredentials
    wrong_password: str
    expected_user: ExpectedAuthUser


class CartProductData(BaseModel):
    id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class CartsData(BaseModel):
    user_id: int = Field(gt=0)
    cart_id: int = Field(gt=0)
    missing_cart_id: int = Field(gt=0)
    product: CartProductData
    updated_product: CartProductData


class UserData(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: int = Field(gt=0, lt=120)
    salary: int = Field(ge=0)
    department: str


class DummyJsonData(BaseModel):
    auth: AuthData
    carts: CartsData
    users: tuple[UserData, ...] = ()

    @field_validator("users")
    @classmethod
    def validate_users_not_empty(
        cls,
        value: tuple[UserData, ...],
    ) -> tuple[UserData, ...]:
        if not value:
            raise ValueError("users list cannot be empty")

        return value


class TestData(BaseModel):
    dummyjson: DummyJsonData
