from aws_lambda_powertools.event_handler.exceptions import NotFoundError
from aws_lambda_powertools.event_handler.router import APIGatewayRouter
from controllers.publication_card import (
    create_publication_card,
    delete_publication_card,
    get_all_publication_cards,
    get_publication_card,
)
from schemas.publication_card import PublicationCardRequestSchema, PublicationCardResponseSchema
from utils.jwt import JwtAuthMiddleware
from utils.logger import logger
from utils.tracer import tracer

router = APIGatewayRouter()
tags = ["Publications card from home"]


@router.post(
    rule="/", tags=tags, summary="Cria uma publicacao do formato de card na home", middlewares=[JwtAuthMiddleware()]
)
@tracer.capture_method
def _create_publication_card(body: PublicationCardRequestSchema) -> PublicationCardResponseSchema:
    # TODO: Implementar o auth no swagger, pois a lib nao faz automaticamente
    # REF: https://docs.powertools.aws.dev/lambda/python/latest/core/event_handler/api_gateway/#customizing_api_metadatapy
    logger.info(body.model_dump)

    return create_publication_card(body)


@router.get(
    rule="/id/<id>",
    tags=tags,
    summary="Pega uma publicacao no formato de card na home",
    middlewares=[JwtAuthMiddleware()],
)
@tracer.capture_method
def _get_publication_card(id: str) -> PublicationCardResponseSchema:
    if data := get_publication_card(id):
        return data

    raise NotFoundError("Publication card not found")


@router.get(
    rule="/get-all/limit/<limit>/page-size/<page_size>",
    tags=tags,
    summary="Pega todas as publicacoes por tamanho de paginacao",
)
@tracer.capture_method
def _get_all_publication_cards(limit: int, page_size: int) -> list[PublicationCardResponseSchema]:
    publication_cards = get_all_publication_cards(limit, page_size)

    return publication_cards


@router.delete(
    rule="/id/<id>", tags=tags, summary="Deleta uma publicacao no formato de card", middlewares=[JwtAuthMiddleware()]
)
@tracer.capture_method
def _delete_publication_card(id: str) -> None:
    return delete_publication_card(id)
