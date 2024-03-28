from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.enrollment import create_enrollment_student, delete_enrollment_student, get_enrollment_student
from schemas.enrollment import EnrollmentStudentRequestSchema, EnrollmentStudentResponseSchema
from utils.logger import logger
from utils.tracer import tracer

router = APIGatewayRouter()
tags = ["Enrollment Student"]


@router.post("/", tags=tags)
@tracer.capture_method
def _create_enrollment_student(body: EnrollmentStudentRequestSchema) -> EnrollmentStudentResponseSchema:
    logger.info(body.model_dump)

    return create_enrollment_student(body)


@router.get("/<page-size>", tags=tags)
@tracer.capture_method
def _get_enrollment_student(page_size: int) -> list[EnrollmentStudentResponseSchema]:
    return get_enrollment_student(page_size)


@router.delete("/id/<id>", tags=tags)
@tracer.capture_method
def _delete_enrollment_student(id: str) -> None:
    return delete_enrollment_student(id)
