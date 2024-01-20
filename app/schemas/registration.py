from datetime import datetime
from uuid import UUID

from schemas import BaseSchema


class RegistrationBaseSchema(BaseSchema):
    id: UUID
    active: bool = False


class RegistrationSchema(RegistrationBaseSchema):
    created_at: datetime
    updated_at: datetime
