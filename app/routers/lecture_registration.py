from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.lecture_registration import create_lecture_registration
from schemas.lecture_registration import LectureRegistrationRequestSchema, LectureRegistrationResponseSchema
from utils.logger import logger
from utils.tracer import tracer

router = APIGatewayRouter()
tags = ["Lecture Registration"]


@router.post("/", tags=tags)
@tracer.capture_method
def _create_lecture_registration(body: LectureRegistrationRequestSchema) -> LectureRegistrationResponseSchema:
    logger.info(body.model_dump)

    return create_lecture_registration(body)
