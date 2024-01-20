from datetime import datetime
from uuid import UUID

from schemas import BaseSchema


class PublicationsBaseSchema(BaseSchema):
    title: str
    paragraph: str
    file_path: str


class PublicationsSchema(PublicationsBaseSchema):
    id: str | UUID
    created_at: datetime
    updated_at: datetime
