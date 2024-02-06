from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.enrollment import (
    create_enrollment,
    create_enrollment_student,
    delete_enrollment,
    delete_enrollment_student,
    get_enrollment,
    get_enrollment_student,
)
from schemas.enrollment import (
    EnrollmentRequestSchema,
    EnrollmentResponseSchema,
    EnrollmentStudentRequestSchema,
    EnrollmentStudentResponseSchema,
)
from utils.logger import logger
from utils.tracer import tracer

router = APIGatewayRouter()


@tracer.capture_method
def _create_enrollment(body: EnrollmentRequestSchema) -> EnrollmentResponseSchema:
    logger.info(body.model_dump)

    return create_enrollment(body)


@router.get("/<page-size>")
@tracer.capture_method
def _get_enrollment(page_size: int) -> list[EnrollmentResponseSchema]:
    return get_enrollment(page_size)


@router.delete("/id/<id>")
@tracer.capture_method
def _delete_enrollment(id: str) -> None:
    return delete_enrollment(id)


@router.post("/enrollment-student")
@tracer.capture_method
def _create_enrollment_student(body: EnrollmentStudentRequestSchema) -> EnrollmentStudentResponseSchema:
    logger.info(body.model_dump)

    return create_enrollment_student(body)


@router.get("/enrollment-student/<page-size>")
@tracer.capture_method
def _get_enrollment_student(page_size: int) -> list[EnrollmentStudentResponseSchema]:
    return get_enrollment_student(page_size)


@router.delete("/enrollment-student/id/<id>")
@tracer.capture_method
def _delete_enrollment_student(id: str) -> None:
    return delete_enrollment_student(id)
