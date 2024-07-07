from datetime import datetime
from uuid import UUID

from schemas import BaseSchema


class TopicsRequestSchema(BaseSchema):
    id: UUID | None = None
    title: str
    order_sequence: int = 0


class TopicsResponseSchema(TopicsRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None


class TopicsUpdateSchema(BaseSchema):
    id: UUID
    title: str | None = None
    order_sequence: int | None = None
