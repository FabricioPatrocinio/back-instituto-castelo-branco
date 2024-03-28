from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.publications import create_publication, delete_publication, get_publications
from schemas.publications import PublicationsBaseSchema, PublicationsSchema
from utils.logger import logger
from utils.tracer import tracer

router = APIGatewayRouter()
tags = ["Publications"]


@router.post("/create", tags=tags)
@tracer.capture_method
def _create_publication(body: PublicationsBaseSchema) -> PublicationsSchema:
    logger.info(body)

    return create_publication(body)


@router.get("/<page_size>", tags=tags)
@tracer.capture_method
def _get_publications(page_size: int) -> list[PublicationsSchema]:
    return get_publications(page_size)


@router.delete("/id/<id>", tags=tags)
@tracer.capture_method
def _delete_publication(id: str) -> None:
    return delete_publication(id)
