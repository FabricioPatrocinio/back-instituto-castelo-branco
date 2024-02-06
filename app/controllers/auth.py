from datetime import datetime, timedelta

from aws_lambda_powertools.event_handler.exceptions import InternalServerError, NotFoundError, UnauthorizedError
from jwt import PyJWKError
from models.auth import UserModel
from pynamodb.exceptions import DoesNotExist
from schemas.auth import AuthenticateUserRequestSchema, TokenResponse, UserRequestSchema, UserResponseSchema
from utils.cryptographic import decrypt
from utils.jwt import create_jwt_token


def create_user(data: UserRequestSchema) -> UserResponseSchema:
    model = UserModel(**data.model_dump(exclude_none=True))

    model.save()

    return model.to_simple_dict()


def authenticate_user(data: AuthenticateUserRequestSchema) -> TokenResponse:
    try:
        user = UserModel.email_index.query(data.email).next()

        if decrypt(user.password) == data.password:
            token_data = {"sub": user.id, "exp": datetime.utcnow() + timedelta(hours=6)}
            token = create_jwt_token(token_data)

            return TokenResponse(
                user_id=user.id,
                access_token=token,
                token_type="bearer",
            )
        else:
            raise UnauthorizedError(msg=f"Senha incorreta DB:{user.password} REQUEST: {data.password}")
    except (DoesNotExist, StopIteration):
        raise NotFoundError(msg="Usuário não encontrado")
    except PyJWKError:
        raise InternalServerError(msg="Erro ao gerar token")
