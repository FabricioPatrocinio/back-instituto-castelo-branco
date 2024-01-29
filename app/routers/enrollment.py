from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from aws_lambda_powertools.metrics import MetricUnit
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
from utils.metrics import metrics
from utils.tracer import tracer

router = APIGatewayRouter()


@tracer.capture_method
def _create_enrollment(body: EnrollmentRequestSchema) -> EnrollmentResponseSchema:
    metrics.add_metric(name="criacaoDeMatriculas", unit=MetricUnit.Count, value=1)

    logger.info(body.model_dump)

    return create_enrollment(body)


@router.get("/<page-size>")
@tracer.capture_method
def _get_enrollment(page_size: int) -> list[EnrollmentResponseSchema]:
    metrics.add_metric(name="listaMatriculas", unit=MetricUnit.Count, value=1)

    return get_enrollment(page_size)


@router.delete("/id/<id>")
@tracer.capture_method
def _delete_enrollment(id: str) -> None:
    metrics.add_metric(name="deletarMatricula", unit=MetricUnit.Count, value=1)

    return delete_enrollment(id)


@router.post("/enrollment-student")
@tracer.capture_method
def _create_enrollment_student(body: EnrollmentStudentRequestSchema) -> EnrollmentStudentResponseSchema:
    metrics.add_metric(name="criacaoDeMatriculasEstudantes", unit=MetricUnit.Count, value=1)

    logger.info(body.model_dump)

    return create_enrollment_student(body)


@router.get("/enrollment-student/<page-size>")
@tracer.capture_method
def _get_enrollment_student(page_size: int) -> list[EnrollmentStudentResponseSchema]:
    metrics.add_metric(name="listaMatriculasEstudantes", unit=MetricUnit.Count, value=1)

    return get_enrollment_student(page_size)


@router.delete("/enrollment-student/id/<id>")
@tracer.capture_method
def _delete_enrollment_student(id: str) -> None:
    metrics.add_metric(name="deletarMatriculaEstudante", unit=MetricUnit.Count, value=1)

    return delete_enrollment_student(id)
