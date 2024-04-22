from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field, field_validator
from schemas import BaseSchema
from utils.cryptographic import encrypt


class AuthenticateUserRequestSchema(BaseSchema):
    email: EmailStr
    password: str


class UserRequestSchema(BaseSchema):
    name: str
    email: EmailStr
    password: str
    phone: str

    @field_validator("password", mode="after")
    @classmethod
    def _encrypt(cls, value: str | EmailStr) -> str | EmailStr:
        return encrypt(value)


class UserResponseSchema(UserRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None
    password: str | None = Field(exclude=True)


class TokenResponse(BaseSchema):
    user_id: str
    access_token: str
    token_type: str
