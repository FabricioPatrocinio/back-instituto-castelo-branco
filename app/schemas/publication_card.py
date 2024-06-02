from datetime import datetime
from uuid import UUID

from schemas import BaseSchema


class PublicationCardRequestSchema(BaseSchema):
    id: UUID | None = None
    title: str
    paragraph: str
    img_name: str | None = None
    link: str | None = None
    text_button_submit: str | None = None


class PublicationCardResponseSchema(PublicationCardRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None


class PublicationCardUpdateSchema(BaseSchema):
    id: UUID
    title: str | None = None
    paragraph: str | None = None
    img_name: str | None = None
    link: str | None = None
    text_button_submit: str | None = None
