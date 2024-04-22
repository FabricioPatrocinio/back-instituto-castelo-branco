from http import HTTPStatus

from aws_lambda_powertools.event_handler.exceptions import ServiceError


class EmailAlreadyExistsError(ServiceError):
    def __init__(self):
        super().__init__(status_code=HTTPStatus.CONFLICT, msg="O email já existe")
