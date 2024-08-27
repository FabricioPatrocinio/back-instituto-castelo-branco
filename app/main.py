from aws_lambda_powertools.event_handler.exceptions import ServiceError
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from routers.api import app
from utils.logger import logger
from utils.tracer import tracer


@app.exception_handler(ServiceError)
def handle_service_error(e: ServiceError):
    return {"message": str(e)}, e.status_code


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
