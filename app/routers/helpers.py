from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from aws_lambda_powertools.metrics import MetricUnit
from controllers.presigned_url import generate_presigned_url
from schemas import UrlPresignedResponseSchema
from utils.jwt import jwt_auth_middleware
from utils.metrics import metrics
from utils.tracer import tracer

router = APIGatewayRouter()


@router.get("/generate-presigned-url", middlewares=[jwt_auth_middleware])
@tracer.capture_method
def _generate_presigned_url() -> UrlPresignedResponseSchema:
    metrics.add_metric(name="generatePresignedUrl", unit=MetricUnit.Count, value=1)

    return generate_presigned_url()
