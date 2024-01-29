from datetime import datetime, timedelta

from aws_lambda_powertools.event_handler.exceptions import InternalServerError, NotFoundError, UnauthorizedError
from jwt import PyJWKError
from models import UserModel
from pynamodb.exceptions import DoesNotExist
from schemas.auth import AuthenticateUserRequestSchema, TokenResponse, UserRequestSchema, UserResponseSchema
from utils.jwt import create_jwt_token


def create_user(data: UserRequestSchema) -> UserResponseSchema:
    model = UserModel(**data.model_dump(exclude_none=True))

    model.save()

    return model.to_simple_dict()


def authenticate_user(data: AuthenticateUserRequestSchema) -> TokenResponse:
    try:
        user = UserModel.get(UserModel.email == data.email)

        if user.password == data.password:
            token_data = {"sub": user.id, "exp": datetime.utcnow() + timedelta(hours=6)}
            token = create_jwt_token(token_data)

            return TokenResponse(
                user_id=user.id,
                access_token=token,
                token_type="bearer",
            )
        else:
            raise UnauthorizedError(status_code=401, detail="Senha incorreta")
    except DoesNotExist:
        raise NotFoundError(status_code=404, detail="Usuário não encontrado")
    except PyJWKError:
        raise InternalServerError(status_code=500, detail="Erro ao gerar token")
