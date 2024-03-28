from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.enrollment import create_enrollment, delete_enrollment, get_enrollment
from schemas.enrollment import EnrollmentRequestSchema, EnrollmentResponseSchema
from utils.logger import logger
from utils.tracer import tracer

router = APIGatewayRouter()
tags = ["Enrollment"]


@router.post("/", tags=tags)
@tracer.capture_method
def _create_enrollment(body: EnrollmentRequestSchema) -> EnrollmentResponseSchema:
    logger.info(body.model_dump)

    return create_enrollment(body)


@router.get("/<page-size>", tags=tags)
@tracer.capture_method
def _get_enrollment(page_size: int) -> list[EnrollmentResponseSchema]:
    return get_enrollment(page_size)


@router.delete("/id/<id>", tags=tags)
@tracer.capture_method
def _delete_enrollment(id: str) -> None:
    return delete_enrollment(id)
