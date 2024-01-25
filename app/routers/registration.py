from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from aws_lambda_powertools.metrics import MetricUnit
from controllers.registration import update_registration
from schemas.registration import RegistrationBaseSchema, RegistrationSchema
from utils.logger import logger
from utils.metrics import metrics
from utils.tracer import tracer

router = APIGatewayRouter()


@router.patch("/create")
@tracer.capture_method
def _update_matricula(body: RegistrationBaseSchema) -> RegistrationSchema:
    metrics.add_metric(name="criacaoDeMatriculas", unit=MetricUnit.Count, value=1)

    logger.info(body.model_dump)

    return update_registration(body)
