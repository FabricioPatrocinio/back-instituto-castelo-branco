from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, Field, field_validator
from schemas import BaseSchema
from utils.cryptographic import decrypt, encrypt


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


class EnrollmentStudentRequestSchema(BaseSchema):
    name: str
    address: str
    email: EmailStr
    phone: str
    student_cpf: str = Field(min_length=11, max_length=14)
    student_rg: str = Field(min_length=7, max_length=9)
    grade: int
    school_name: str
    financial_responsible_name: str | None = None
    financial_responsible_cpf: str | None = Field(default=None, min_length=11, max_length=14)

    @field_validator(
        "email",
        "phone",
        "student_cpf",
        "student_rg",
        "financial_responsible_name",
        "financial_responsible_cpf",
        mode="after",
    )
    @classmethod
    def parse_cpf(cls, value: str | EmailStr) -> str | EmailStr:
        return encrypt(value)


class EnrollmentStudentResponseSchema(EnrollmentStudentRequestSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime | None = None

    @field_validator(
        "email",
        "phone",
        "student_cpf",
        "student_rg",
        "financial_responsible_name",
        "financial_responsible_cpf",
        mode="before",
    )
    @classmethod
    def parse_cpf(cls, value: str | EmailStr) -> str | EmailStr:
        return decrypt(value)
