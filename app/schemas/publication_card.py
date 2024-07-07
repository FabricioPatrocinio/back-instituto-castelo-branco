from datetime import datetime
from uuid import UUID

from schemas import BaseSchema


class PublicationCardRequestSchema(BaseSchema):
    id: UUID | None = None
    topic: UUID | str | None = None
    title: str
    paragraph: str
    img_name: str | None = None
    link: str | None = None
    is_internal_link: bool | None = False
    is_form_with_responsible: bool | None = False
    text_button_submit: str | None = None


class PublicationCardResponseSchema(PublicationCardRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None


class PublicationCardUpdateSchema(BaseSchema):
    id: UUID
    topic: UUID | str | None = None
    title: str | None = None
    paragraph: str | None = None
    img_name: str | None = None
    link: str | None = None
    text_button_submit: str | None = None
