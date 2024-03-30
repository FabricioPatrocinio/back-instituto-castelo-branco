from models.enrollment import EnrollmentModel
from schemas.enrollment import EnrollmentRequestSchema, EnrollmentResponseSchema


def create_enrollment(data: EnrollmentRequestSchema) -> EnrollmentResponseSchema:
    model = EnrollmentModel(**data.model_dump())

    return model.to_simple_dict()


def get_enrollment(page_size: int) -> list[EnrollmentResponseSchema]:
    model = EnrollmentModel.scan(limit=page_size, page_size=page_size)

    return model


def delete_enrollment(id: str) -> None:
    model = EnrollmentModel.get(hash_key=id)
    model.delete()
