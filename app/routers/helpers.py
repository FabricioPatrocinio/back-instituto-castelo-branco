from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.presigned_url import generate_presigned_url
from schemas import UrlPresignedResponseSchema
from utils.jwt import JwtAuthMiddleware
from utils.tracer import tracer

router = APIGatewayRouter()
tags = ["Helpers"]


@router.get(rule="/generate-presigned-url", tags=tags, middlewares=[JwtAuthMiddleware()])
@tracer.capture_method
def _generate_presigned_url() -> UrlPresignedResponseSchema:
    return generate_presigned_url()
