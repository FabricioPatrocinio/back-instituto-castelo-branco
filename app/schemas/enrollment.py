from datetime import datetime
from uuid import UUID

from pydantic import EmailStr
from schemas import BaseSchema


class EnrollmentRequestSchema(BaseSchema):
    active: bool = False
    emails: list[EmailStr]
    value: float
    title: str
    paragraph: str
    expires_at: datetime


class EnrollmentResponseSchema(EnrollmentRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None
