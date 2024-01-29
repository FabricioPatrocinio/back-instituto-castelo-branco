from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, field_validator
from schemas import BaseSchema
from utils.cryptographic import decrypt, encrypt


class AuthenticateUserRequestSchema(BaseSchema):
    email: EmailStr
    password: str

    @field_validator("email", "password", mode="after")
    @classmethod
    def parse_cpf(cls, value: str | EmailStr) -> str | EmailStr:
        return encrypt(value)


class UserRequestSchema(BaseSchema):
    name: str
    email: EmailStr
    password: str
    phone: str

    @field_validator("email", "password", mode="after")
    @classmethod
    def parse_cpf(cls, value: str | EmailStr) -> str | EmailStr:
        return encrypt(value)


class UserResponseSchema(UserRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None

    @field_validator("email", "password", mode="before")
    @classmethod
    def parse_cpf(cls, value: str | EmailStr) -> str | EmailStr:
        return decrypt(value)


class TokenResponse(BaseSchema):
    user_id: str
    access_token: str
    token_type: str
