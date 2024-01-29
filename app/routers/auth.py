from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from aws_lambda_powertools.metrics import MetricUnit
from controllers.auth import authenticate_user, create_user
from schemas.auth import AuthenticateUserRequestSchema, TokenResponse, UserRequestSchema, UserResponseSchema
from utils.metrics import metrics
from utils.tracer import tracer

router = APIGatewayRouter()


@router.get("/token")
@tracer.capture_method
def _generate_presigned_url(data: AuthenticateUserRequestSchema) -> TokenResponse:
    metrics.add_metric(name="generateTokenAccess", unit=MetricUnit.Count, value=1)

    return authenticate_user(data)


@router.get("/create")
@tracer.capture_method
def _create_user(data: UserRequestSchema) -> UserResponseSchema:
    metrics.add_metric(name="createUser", unit=MetricUnit.Count, value=1)

    return create_user(data)
