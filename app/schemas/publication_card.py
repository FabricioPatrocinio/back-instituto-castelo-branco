from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field, field_validator
from schemas import BaseSchema


class PublicationCardRequestSchema(BaseSchema):
    active: bool = False
    title: str
    emails: list[EmailStr]
    paragraph: str
    expires_at: datetime | None = Field(None, description="Data de expiracao para controlar tempo de visualizacao")
    img_id: UUID | None = None
    link: str | None = None

    @field_validator("img_id")
    def parser_uuid(cls, value) -> str:
        if value:
            return str(value)

        return value


class PublicationCardResponseSchema(PublicationCardRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None


class PublicationCardUpdateSchema(BaseSchema):
    active: bool = None
    emails: list[EmailStr] | None = None
    value: float | None = None
    title: str | None = None
    paragraph: str | None = None
    expires_at: datetime | None = None
    img_id: UUID | None = None
    link: str | None = None
