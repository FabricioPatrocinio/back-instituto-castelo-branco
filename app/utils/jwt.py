import jwt
from aws_lambda_powertools.event_handler.exceptions import UnauthorizedError
from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from settings import settings

secret_key = settings.JWT_SECRET_KEY
algorithm = settings.JWT_ALGORITHM


def create_jwt_token(data: dict) -> str:
    return jwt.encode(data, secret_key, algorithm=algorithm)


def authenticate_jwt(token: str) -> dict:
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])

        return payload
    except jwt.JWTError:
        return None


def jwt_auth_middleware(router: APIGatewayRouter) -> dict:
    # from aws_lambda_powertools.utilities.typing import LambdaContext
    # token = event.get("headers", {}).get("Authorization", "").replace("Bearer ", "")

    token: str = router.current_event.get_header_value(name="Authorization", case_sensitive=True)

    if payload := authenticate_jwt(token):
        return payload

    raise UnauthorizedError(msg="Unauthorized")
