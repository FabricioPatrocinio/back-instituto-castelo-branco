from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.auth import authenticate_user, create_user
from schemas.auth import AuthenticateUserRequestSchema, TokenResponse, UserRequestSchema, UserResponseSchema
from utils.tracer import tracer

router = APIGatewayRouter()


@router.post("/token")
@tracer.capture_method
def _authenticate_user(data: AuthenticateUserRequestSchema) -> TokenResponse:
    return authenticate_user(data).model_dump()


@router.post("/create")
@tracer.capture_method
def _create_user(data: UserRequestSchema) -> UserResponseSchema:
    return create_user(data)
