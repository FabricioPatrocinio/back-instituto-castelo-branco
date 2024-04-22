import jwt
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response
from aws_lambda_powertools.event_handler.exceptions import UnauthorizedError
from aws_lambda_powertools.event_handler.middlewares import BaseMiddlewareHandler, NextMiddleware
from jwt.exceptions import PyJWTError
from settings import settings

secret_key = settings.JWT_SECRET_KEY
algorithm = settings.JWT_ALGORITHM


def create_jwt_token(data: dict) -> str:
    return jwt.encode(data, secret_key, algorithm=algorithm)


def authenticate_jwt(token: str) -> dict:
    try:
        payload = jwt.decode(token.replace("Bearer ", ""), secret_key, algorithms=[algorithm])

        return payload
    except PyJWTError:
        return None


class JwtAuthMiddleware(BaseMiddlewareHandler):
    def handler(self, app: APIGatewayRestResolver, next_middleware: NextMiddleware) -> Response:
        token: str = app.current_event.get_header_value(name="Authorization", case_sensitive=True)

        if not authenticate_jwt(token):
            raise UnauthorizedError(msg="Nao autorizado!")

        return next_middleware(app)
