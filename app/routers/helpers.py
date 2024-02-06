from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.presigned_url import generate_presigned_url
from schemas import UrlPresignedResponseSchema
from utils.jwt import jwt_auth_middleware
from utils.tracer import tracer

router = APIGatewayRouter()


@router.get("/generate-presigned-url")
@tracer.capture_method
def _generate_presigned_url() -> UrlPresignedResponseSchema:
    jwt_auth_middleware(router)

    return generate_presigned_url()
