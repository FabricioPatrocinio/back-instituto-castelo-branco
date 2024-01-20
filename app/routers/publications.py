from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from aws_lambda_powertools.metrics import MetricUnit
from controllers.publications import create_publication
from schemas.publications import PublicationsBaseSchema, PublicationsSchema
from utils.logger import logger
from utils.metrics import metrics
from utils.tracer import tracer

router = APIGatewayRouter()


@router.post("/create")
@tracer.capture_method
def _create_publications(body: PublicationsBaseSchema) -> PublicationsSchema:
    metrics.add_metric(name="criacaoDePublicacoes", unit=MetricUnit.Count, value=1)

    logger.info(body)

    return create_publication(body)
