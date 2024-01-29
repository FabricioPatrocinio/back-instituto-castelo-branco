from models.enrollment import EnrollmentModel, EnrollmentStudentModel
from schemas.enrollment import (
    EnrollmentRequestSchema,
    EnrollmentResponseSchema,
    EnrollmentStudentRequestSchema,
    EnrollmentStudentResponseSchema,
)
from utils.emails.enrollment_student import send_email_with_html_template


def create_enrollment(data: EnrollmentRequestSchema) -> EnrollmentResponseSchema:
    model = EnrollmentModel(**data.model_dump())

    return model.to_simple_dict()


def get_enrollment(page_size: int) -> list[EnrollmentResponseSchema]:
    model = EnrollmentModel.scan(limit=page_size, page_size=page_size)

    return model


def delete_enrollment(id: str) -> None:
    model = EnrollmentModel.get(hash_key=id)
    model.delete()


def create_enrollment_student(data: EnrollmentStudentRequestSchema) -> EnrollmentStudentResponseSchema:
    model = EnrollmentStudentModel(**data.model_dump())

    model.save()

    send_email_with_html_template(model.to_simple_dict())

    return model.to_simple_dict()


def get_enrollment_student(page_size: int) -> list[EnrollmentStudentResponseSchema]:
    model = EnrollmentStudentModel.scan(limit=page_size, page_size=page_size)

    return model


def delete_enrollment_student(id: str) -> None:
    model = EnrollmentStudentModel.get(hash_key=id)
    model.delete()
