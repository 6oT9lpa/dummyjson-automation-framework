from pydantic import BaseModel, ConfigDict, Field


class LoginRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    username: str
    password: str
    expires_in_mins: int = Field(default=30, alias="expiresInMins")


class CartProductRequest(BaseModel):
    id: int = Field(gt=0)
    quantity: int = Field(gt=0)


class AddCartRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: int = Field(alias="userId", gt=0)
    products: list[CartProductRequest] = Field(min_length=1)


class UpdateCartRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    should_merge: bool = Field(default=True, alias="merge")
    products: list[CartProductRequest] = Field(min_length=1)
